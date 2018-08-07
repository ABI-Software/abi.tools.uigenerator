from abi.tools.generatesettings import GenerateSettingsDialog

__version__ = '0.3.0'

import os
import argparse

try:
    from PySide import QtGui
    from PySide import QtCore
except ImportError:
    from PySide2 import QtCore
    from PySide2 import QtWidgets as QtGui

ORGANISATION = 'abi'
ORGANISATION_DOMAIN = 'abi.auckland.ac.nz'


class GenerateCommon(QtGui.QDialog):

    def closeEvent(self, event):
        self._save_settings()
        event.accept()

    def _load_settings(self):
        self.resize(self._settings.value('size', QtCore.QSize(270, 225)))
        self.move(self._settings.value('pos', QtCore.QPoint(50, 50)))

    def _save_settings(self):
        self._settings.setValue('size', self.size())
        self._settings.setValue('pos', self.pos())
        self._src_dir_settings.save(self._settings)

    def _make_connections(self):
        self._ui.settings_pushButton.clicked.connect(self._settings_clicked)

    def _settings_initial_location(self):
        parent_size = self.size()
        parent_pos = self.pos()
        settings_size = parent_size - QtCore.QSize(100, 100)
        settings_pos = parent_pos + QtCore.QPoint(50, 50)
        return settings_size, settings_pos

    def _settings_clicked(self):
        dlg = GenerateSettingsDialog(self, __version__, self._settings)

        initial_size, initial_pos = self._settings_initial_location()
        dlg.resize(self._settings.value('settings_size', initial_size))
        dlg.move(self._settings.value('settings_pos', initial_pos))

        dlg.exec_()

        self._settings.setValue('settings_size', dlg.size())
        self._settings.setValue('settings_pos', dlg.pos())


class FileOptions(object):
    def __init__(self, file_name):
        self._file_name = file_name
        self._side_by_side_output = True
        self._out_dir = ''
        self._repair_resource_string = ''

    def get_file_name(self):
        return self._file_name

    def is_side_by_side_output(self):
        return self._side_by_side_output

    def set_side_by_side_output(self, value=True):
        self._side_by_side_output = value

    def get_out_dir(self):
        return self._out_dir

    def set_out_dir(self, value):
        self._out_dir = value

    def get_repair_resource_string(self):
        return self._repair_resource_string

    def set_repair_resource_string(self, value):
        self._repair_resource_string = value

    def __repr__(self):
        return 'FileOptions: {0}'.format(self._out_dir)


class SrcDirSettings(object):

    def __init__(self, src_dir):
        self._src_dir = src_dir
        self._current_file = ''
        self._file_listing = {}

    def add_file_listings(self, listings):
        for item in listings:
            if item not in self._file_listing:
                self._file_listing[item] = FileOptions(item)

    def get_src_dir(self):
        return self._src_dir

    def get_current_file(self):
        return self._current_file

    def set_current_file(self, value):
        self._current_file = value

    def is_side_by_side_output(self):
        return self._file_listing[self._current_file].is_side_by_side_output()

    def set_side_by_side_output(self, value=True):
        self._file_listing[self._current_file].set_side_by_side_output(value)

    def get_out_dir(self):
        return self._file_listing[self._current_file].get_out_dir()

    def set_out_dir(self, value):
        self._file_listing[self._current_file].set_out_dir(value)

    def get_repair_resource_string(self):
        return self._file_listing[self._current_file].get_repair_resource_string()

    def set_repair_resource_string(self, value):
        self._file_listing[self._current_file].set_repair_resource_string(value)

    def load(self, settings):
        settings.beginGroup(self._src_dir)
        self.set_current_file(settings.value('current_file', ''))
        if settings.contains('current_index'):
            settings.remove('current_index')

        size = settings.beginReadArray('file_options')
        for index in range(size):
            settings.setArrayIndex(index)
            file_name = settings.value('file_name', '')
            file_options = FileOptions(file_name)
            file_options.set_repair_resource_string(settings.value('repair_resource_string', ''))
            file_options.set_out_dir(settings.value('out_dir', ''))
            file_options.set_side_by_side_output(settings.value('side_by_side', 'true') == 'true')
            self._file_listing[file_name] = file_options
        settings.endArray()

        if self._current_file not in self._file_listing:
            for key in self._file_listing:
                self._current_file = key
                break

        settings.endGroup()

    def save(self, settings):
        settings.beginGroup(self._src_dir)
        settings.setValue('current_file', self.get_current_file())

        settings.beginWriteArray('file_options')
        for index, file_name in enumerate(self._file_listing):
            file_options = self._file_listing[file_name]
            settings.setArrayIndex(index)
            settings.setValue('file_name', file_options.get_file_name())
            settings.setValue('out_dir', file_options.get_out_dir())
            settings.setValue('side_by_side', file_options.is_side_by_side_output())
            settings.setValue('repair_resource_string', file_options.get_repair_resource_string())
        settings.endArray()

        settings.endGroup()


def setup_application(app, app_name):

    app.setOrganizationName(ORGANISATION)
    app.setOrganizationDomain(ORGANISATION_DOMAIN)
    app.setApplicationName(app_name)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("src_dir", nargs='?', default=os.getcwd(),
                        help="the directory to search (recursively) for ui files.")
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s {version}'.format(version=__version__))
    return parser.parse_args()
