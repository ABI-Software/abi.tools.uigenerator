
try:
    from PySide import QtGui
    from PySide import QtCore
    from abi.tools.ui.ui_settingsdialog import Ui_SettingsDialog
except ImportError:
    from PySide2 import QtCore
    from PySide2 import QtWidgets as QtGui
    from abi.tools.ui.ui2_settingsdialog import Ui_SettingsDialog


class GenerateSettingsDialog(QtGui.QDialog):

    def __init__(self, parent, version, settings):
        super(GenerateSettingsDialog, self).__init__(parent)
        self._ui = Ui_SettingsDialog()
        self._ui.setupUi(self)

        self._ui.versionDisplay_label.setText(version)
        known_locations = settings.childGroups()
        known_locations_string = '\n'.join(known_locations)
        self._ui.registeredLocations_plainTextEdit.insertPlainText(known_locations_string)
