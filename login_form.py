from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLineEdit
import sys
import client

class Ui_Login_Window(object):

    def SetupUi(self, Login_Window):
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
        self.log_label.setGeometry(QtCore.QRect(167, 310, 311, 51))
        self.log_label.setText("")
        self.log_label.setObjectName("log_label")

        self.login_Button = QtWidgets.QPushButton(self.centralwidget)
        self.login_Button.setGeometry(QtCore.QRect(180, 270, 131, 38))
        self.login_Button.setObjectName("login_Button")
        ################### login_Button Signal #####################
        self.login_Button.clicked.connect(lambda: self.Login_Button())

        self.username = QtWidgets.QLabel(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(76, 120, 91, 22))
        self.username.setObjectName("username")

        self.username_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.username_lineEdit.setGeometry(QtCore.QRect(190, 110, 221, 36))
        self.username_lineEdit.setFrame(True)
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.username_lineEdit.setPlaceholderText("Enter your username")

        self.password = QtWidgets.QLabel(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(80, 160, 81, 22))
        self.password.setObjectName("Password")

        self.password_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_lineEdit.setGeometry(QtCore.QRect(190, 150, 221, 36))
        self.password_lineEdit.setFrame(True)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.password_lineEdit.setPlaceholderText("Enter your password")
        self.password_lineEdit.setEchoMode(QLineEdit.Password)

        self.server_address_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.server_address_lineEdit.setGeometry(QtCore.QRect(190, 190, 130, 36))
        self.server_address_lineEdit.setFrame(True)
        self.server_address_lineEdit.setObjectName("server_address_lineEdit")
        self.server_address_lineEdit.setPlaceholderText("Ip Address")

        self.server_port_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.server_port_lineEdit.setGeometry(QtCore.QRect(330, 190, 81, 36))
        self.server_port_lineEdit.setFrame(True)
        self.server_port_lineEdit.setObjectName("server_port_lineEdit")
        self.server_port_lineEdit.setPlaceholderText("Port")

        self.server_port_ip1 = QtWidgets.QLabel(self.centralwidget)
        self.server_port_ip1.setGeometry(QtCore.QRect(85, 200, 81, 22))
        self.server_port_ip1.setObjectName("server_port_ip1")

        self.server_port_ip2 = QtWidgets.QLabel(self.centralwidget)
        self.server_port_ip2.setGeometry(QtCore.QRect(323, 196, 81, 22))
        self.server_port_ip2.setObjectName("server_port_ip2")

        Login_Window.setCentralWidget(self.centralwidget)

        self.RetranslateUi(Login_Window)
        QtCore.QMetaObject.connectSlotsByName(Login_Window)

    def RetranslateUi(self, Login_Window):
        _translate = QtCore.QCoreApplication.translate
        Login_Window.setWindowTitle(_translate("Login_Window", "Login page"))
        self.login_Button.setToolTip(_translate("Login_Window", "login button"))
        self.login_Button.setText(_translate("Login_Window", "Login"))
        self.username.setText(_translate("Login_Window", "Username:"))
        self.password.setText(_translate("Login_Window", "Password:"))
        self.password_lineEdit.setToolTip(_translate("Login_Window", "Enter your password"))
        self.username_lineEdit.setToolTip(_translate("Login_Window", "Enter your username"))
        self.server_address_lineEdit.setToolTip(_translate("Login_Window","Enter IP Address of server"))
        self.server_port_lineEdit.setToolTip(_translate("Login_Window", "Enter Port of server"))
        self.automation_label.setText(_translate("Login_Window", "Automation Welcome!"))
        self.server_port_ip1.setText(_translate("Login_Window", "Ip : Port"))
        self.server_port_ip2.setText(_translate("Login_Window", ":"))

    # def Update_Label_Size(self, label):
    #     label.adjustSize()

    def Login_Button(self):
        Login_Window.close()

        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        ip = self.server_address_lineEdit.text()
        port = int(self.server_port_lineEdit.text())

        Client = client.Client()
        Client.Connect_and_authenticate_to_server(ip, port, username, password)
        report = Client.Report

        if report == False:
            self.Show_notify_fail_login()

    def Show_notify_fail_login(self):
        msg = QMessageBox()
        msg.setText("Login was Failed")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Retry)
        msg.setDefaultButton(QMessageBox.Retry)
        msg.setDetailedText("Sorry server is down :( Connection refused, please try again")
        msg.buttonClicked.connect(lambda: Login_Window.show())
        msg.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Login_Window = QtWidgets.QMainWindow()
    ui = Ui_Login_Window()
    ui.SetupUi(Login_Window)
    Login_Window.show()
    sys.exit(app.exec_())