from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import workspace_form, login_form

if __name__ == "__main__":
    app = QApplication(sys.argv)
    workspace = workspace_form.QMainWindow()
    login = login_form.QMainWindow()

    ui_workspace = workspace_form.Ui_WorkSpace_window()
    ui_login = login_form.Ui_Login_Window()

    ui_workspace.SetupUi(workspace)
    ui_login.SetupUi(login)

    login.show()
    workspace.show()

    sys.exit(app.exec_())