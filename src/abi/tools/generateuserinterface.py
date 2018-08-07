
import os
import sys
import fnmatch
import platform
import xml.etree.ElementTree as ET

from abi.tools.generatecommon import ORGANISATION, ORGANISATION_DOMAIN, SrcDirSettings, setup_application, \
    parse_arguments, GenerateCommon

try:
    from PySide import QtGui
    from PySide import QtCore
    from pysideuic import compileUi
    from abi.tools.ui.ui_uifileconverter import Ui_UIFileConverterDialog
except ImportError:
    from PySide2 import QtCore
    from PySide2 import QtWidgets as QtGui
    from pyside2uic import compileUi
    from abi.tools.ui.ui2_uifileconverter import Ui_UIFileConverterDialog


class UiFileConverterDialog(GenerateCommon):

    def __init__(self, src_root_dir):
        super(UiFileConverterDialog, self).__init__()
        self._ui = Ui_UIFileConverterDialog()
        self._ui.setupUi(self)

        if platform.system() == 'Darwin':
            organisation_string = ORGANISATION_DOMAIN
        else:
            organisation_string = ORGANISATION
        self._settings = QtCore.QSettings(QtCore.QSettings.IniFormat, QtCore.QSettings.UserScope,
                                          organisation_string, 'uigenerator')
        self._settings.setFallbacksEnabled(False)

        self._make_connections()

        self._src_dir_settings = SrcDirSettings(src_root_dir)
        self._load_settings()

        self._setup_ui()
        self._update_ui()

    def _setup_ui(self):
        self._src_dir_settings.load(self._settings)
        src_dir = self._src_dir_settings.get_src_dir()
        files = find_ui_files(src_dir)
        relative_file_names = [os.path.relpath(name, src_dir) for name in files]
        self._src_dir_settings.add_file_listings(relative_file_names)
        self._ui.uiFile_comboBox.blockSignals(True)
        self._ui.uiFile_comboBox.addItems(relative_file_names)
        self._ui.uiFile_comboBox.blockSignals(False)

    def _update_ui(self):
        current_file_name = self._src_dir_settings.get_current_file()
        if self._ui.uiFile_comboBox.currentText() != current_file_name:
            index_of_current_file = self._ui.uiFile_comboBox.findText(current_file_name)
            self._ui.uiFile_comboBox.setCurrentIndex(index_of_current_file)
        self._ui.uiFile_pushButton.setEnabled(self._ui.uiFile_comboBox.count() > 0)
        side_by_side = self._src_dir_settings.is_side_by_side_output()
        self._ui.sideBySide_groupBox.setChecked(side_by_side)
        self._update_side_by_side(side_by_side)
        self._ui.outDir_lineEdit.setText(self._src_dir_settings.get_out_dir())
        self._update_patch_resources_import()

    def _update_patch_resources_import(self):
        self._ui.patchResourcesImport_groupBox.setEnabled(_includes_resources(self._ui.uiFile_comboBox.currentText()))
        repair_resource_string = self._src_dir_settings.get_repair_resource_string()
        self._ui.repairString_lineEdit.setText(repair_resource_string)

    def _update_side_by_side(self, state):
        self._ui.outDir_lineEdit.setEnabled(not state)
        self._ui.outDir_pushButton.setEnabled(not state)
        self._ui.outDir_label.setEnabled(not state)
        self._src_dir_settings.set_side_by_side_output(state)

    def _ui_file_changed(self, current_index):
        text = self._ui.uiFile_comboBox.currentText()
        self._src_dir_settings.set_current_file(text)
        self._update_ui()

    def _repair_string_changed(self, new_text):
        self._src_dir_settings.set_repair_resource_string(new_text)

    def _make_connections(self):
        super(UiFileConverterDialog, self)._make_connections()
        self._ui.uiFile_pushButton.clicked.connect(self._convert)
        self._ui.uiFile_comboBox.currentIndexChanged.connect(self._ui_file_changed)
        self._ui.sideBySide_groupBox.toggled.connect(self._update_side_by_side)
        self._ui.repairString_lineEdit.textChanged.connect(self._repair_string_changed)
        self._ui.outDir_pushButton.clicked.connect(self._choose_output_directory)

    def _choose_output_directory(self):
        selected_directory = QtGui.QFileDialog.getExistingDirectory()
        if selected_directory:
            self._ui.outDir_lineEdit.setText(selected_directory)
            self._src_dir_settings.set_out_dir(selected_directory)

    def _convert(self):
        src_dir = self._src_dir_settings.get_src_dir()
        ui_file = self._ui.uiFile_comboBox.currentText()

        abs_path_to_ui_file = os.path.join(src_dir, ui_file)
        ui_file_directory = os.path.dirname(abs_path_to_ui_file)

        file_root_name = os.path.splitext(os.path.basename(ui_file))[0]
        if self._src_dir_settings.is_side_by_side_output():
            out_directory = ui_file_directory
        else:
            out_directory = self._src_dir_settings.get_out_dir()

        abs_path_to_out_file = os.path.join(out_directory, 'ui_' + file_root_name + '.py')

        with open(ui_file, 'r') as f:
            with open(abs_path_to_out_file, 'w') as g:
                pre_compile_text = 'Compiling ui file \n\t"%s"\n and writing out to \n\t"%s".'\
                                   % (abs_path_to_ui_file, abs_path_to_out_file)
                self._ui.screen_label.setText(pre_compile_text)
                compileUi(f, g, from_imports=True)
                self._ui.screen_label.setText(pre_compile_text + '\n\nSuccess.')

        repair_resource_string = self._src_dir_settings.get_repair_resource_string()

        if repair_resource_string:
            with open(abs_path_to_out_file, 'r') as f:
                content = f.read()

            modified_content = content.replace('from . import resources_rc', repair_resource_string)

            with open(abs_path_to_out_file, 'w') as f:
                f.write(modified_content)


def _includes_resources(file_name):
    tree = ET.parse(file_name)
    element = tree.find('resources')
    if element is None:
        return False

    for sub_element in element:
        if 'location' in sub_element.attrib:
            return sub_element.attrib['location'].endswith('.qrc')

    return False


def find_ui_files(search_dir):
    matches = []
    for root, dirnames, filenames in os.walk(search_dir):
        for filename in fnmatch.filter(filenames, '*.ui'):
            matches.append(os.path.join(root, filename))

    return matches


def main():

    app = QtGui.QApplication(sys.argv)

    setup_application(app, 'uigenerator')
    args = parse_arguments()

    src_root_dir = os.path.realpath(args.src_dir)
    os.chdir(src_root_dir)

    dialog = UiFileConverterDialog(src_root_dir)
    dialog.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
