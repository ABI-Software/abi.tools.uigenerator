

import os
import sys
import fnmatch
import platform

from abi.tools.generatecommon import ORGANISATION, ORGANISATION_DOMAIN, GenerateCommon, setup_application, \
    parse_arguments, SrcDirSettings

try:
    from PySide import QtGui
    from PySide import QtCore
    from pysideuic import compileUi
    from abi.tools.ui.ui_qrcfileconverter import Ui_QrcFileConverterDialog
except ImportError:
    from PySide2 import QtCore
    from PySide2 import QtWidgets as QtGui
    from pyside2uic import compileUi
    from abi.tools.ui.ui2_qrcfileconverter import Ui_QrcFileConverterDialog


def find_qrc_files(search_dir):
    matches = []
    for root, dirnames, filenames in os.walk(search_dir):
        for filename in fnmatch.filter(filenames, '*.qrc'):
            matches.append(os.path.join(root, filename))

    return matches


class QrcFileConverterDialog(GenerateCommon):

    def __init__(self, src_root_dir):
        super(QrcFileConverterDialog, self).__init__()
        self._ui = Ui_QrcFileConverterDialog()
        self._ui.setupUi(self)

        self._src_dir_settings = SrcDirSettings(src_root_dir)

        if platform.system() == 'Darwin':
            organisation_string = ORGANISATION_DOMAIN
        else:
            organisation_string = ORGANISATION
        self._settings = QtCore.QSettings(QtCore.QSettings.IniFormat, QtCore.QSettings.UserScope,
                                          organisation_string, 'uigenerator')
        self._settings.setFallbacksEnabled(False)
        self._load_settings()

        self._update_ui()
        self._make_connections()

    def _update_ui(self):
        src_dir = self._src_dir_settings.get_src_dir()
        files = find_qrc_files(src_dir)
        self._ui.uiFile_comboBox.addItems([os.path.relpath(name, src_dir) for name in files])
        self._ui.uiFile_comboBox.setCurrentIndex(self._src_dir_settings.get_current_file())
        self._ui.uiFile_pushButton.setEnabled(self._ui.uiFile_comboBox.count() > 0)
        side_by_side = self._src_dir_settings.is_side_by_side_output()
        self._ui.sideBySide_groupBox.setChecked(side_by_side)
        self._side_by_side_changed(side_by_side)
        self._ui.outDir_lineEdit.setText(self._src_dir_settings.get_out_dir())

    def _make_connections(self):
        self._ui.uiFile_pushButton.clicked.connect(self._convert)
        self._ui.uiFile_comboBox.currentIndexChanged.connect(self._src_dir_settings.set_current_file)
        self._ui.sideBySide_groupBox.toggled.connect(self._side_by_side_changed)
        self._ui.outDir_pushButton.clicked.connect(self._choose_output_directory)

    def _side_by_side_changed(self, state):
        self._ui.outDir_lineEdit.setEnabled(not state)
        self._ui.outDir_pushButton.setEnabled(not state)
        self._ui.outDir_label.setEnabled(not state)
        self._src_dir_settings.set_side_by_side_output(state)

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
                self._ui.screen_label.setText(pre_compile_text + '\n\nCompiled.')


def main():

    app = QtGui.QApplication(sys.argv)

    setup_application(app, 'qrcgenerator')
    args = parse_arguments()

    src_root_dir = os.path.realpath(args.src_dir)
    os.chdir(src_root_dir)

    dialog = QrcFileConverterDialog(src_root_dir)
    dialog.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
