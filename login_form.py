from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Login_Window(object):

    def setupUi(self, Login_Window):
        Login_Window.setObjectName("Login_Window")
        Login_Window.setEnabled(True)
        Login_Window.setGeometry(730, 300, 490, 370)
        Login_Window.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        Login_Window.setFont(font)
        Login_Window.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(Login_Window)
        self.centralwidget.setObjectName("centralwidget")

        self.automation_label = QtWidgets.QLabel(self.centralwidget)
        self.automation_label.setGeometry(QtCore.QRect(10, 10, 471, 81))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.automation_label.setFont(font)
        self.automation_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.automation_label.setObjectName("automation_label")

        self.log_label = QtWidgets.QLabel(self.centralwidget)
        self.log_label.setGeometry(QtCore.QRect(90, 310, 311, 51))
        self.log_label.setFrameShape(QtWidgets.QFrame.HLine)
        self.log_label.setText("")
        self.log_label.setObjectName("log_label")

        self.login_Button = QtWidgets.QPushButton(self.centralwidget)
        self.login_Button.setGeometry(QtCore.QRect(180, 270, 131, 38))
        self.login_Button.setObjectName("login_Button")
        self.login_Button.clicked.connect(lambda: self.Login_Button())

        self.username = QtWidgets.QLabel(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(76, 120, 91, 22))
        self.username.setObjectName("username")

        self.username_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.username_lineEdit.setGeometry(QtCore.QRect(190, 110, 221, 36))
        self.username_lineEdit.setFrame(True)
        self.username_lineEdit.setObjectName("username_lineEdit")

        self.Password = QtWidgets.QLabel(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(80, 160, 81, 22))
        self.Password.setObjectName("Password")

        self.password_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_lineEdit.setGeometry(QtCore.QRect(190, 150, 221, 36))
        self.password_lineEdit.setFrame(True)
        self.password_lineEdit.setObjectName("password_lineEdit")

        Login_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login_Window)
        QtCore.QMetaObject.connectSlotsByName(Login_Window)

    def retranslateUi(self, Login_Window):
        _translate = QtCore.QCoreApplication.translate
        Login_Window.setWindowTitle(_translate("Login_Window", "Login page"))
        self.login_Button.setToolTip(_translate("Login_Window", "login button"))
        self.login_Button.setText(_translate("Login_Window", "Login"))
        self.username.setText(_translate("Login_Window", "Username:"))
        self.Password.setText(_translate("Login_Window", "Password:"))
        self.password_lineEdit.setToolTip(_translate("Login_Window", "Enter your password"))
        self.username_lineEdit.setToolTip(_translate("Login_Window", "Enter your username"))
        self.automation_label.setText(_translate("Login_Window", "Automation Welcome!"))

    def Update_Label_Size(self, label):
        label.adjustSize()

    def Login_Button(self):
        self.log_label.setText("Login was Successful")
        self.Update_Label_Size(self.log_label)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Login_Window = QtWidgets.QMainWindow()
    ui = Ui_Login_Window()
    ui.setupUi(Login_Window)
    Login_Window.show()
    sys.exit(app.exec_())