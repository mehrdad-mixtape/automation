from PyQt5 import QtCore, QtGui, QtWidgets # PyQt5 have 620 class and 6000 method
# QtCore use for working with files, directories, URL protocols, ...
# QtGui use for working with graphical content like font-size, sentence-size, ...
# QtWidgets for working with widgets_UI like buttons, labels, combobox, ...
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
import sys
import admin, normal_user

class Ui_Login_Window():

    def SetupUi(self, Login_Window):
        Login_Window.setObjectName("Login_Window")
        Login_Window.setEnabled(True)
        Login_Window.setGeometry(700, 300, 490, 420)
        Login_Window.setMaximumSize(QtCore.QSize(490, 420))
        Login_Window.setMinimumSize(QtCore.QSize(490, 420))

        font = QtGui.QFont()
        font.setPointSize(12)
        Login_Window.setFont(font)
        Login_Window.setToolTip("")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/2252295991582004497-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login_Window.setWindowIcon(icon)

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
        self.login_Button.setGeometry(QtCore.QRect(127, 340, 110, 38))
        self.login_Button.setObjectName("login_Button")
        ################### login_Button Signal #####################
        self.login_Button.clicked.connect(lambda: self.Login_Button())

        self.close_Button = QtWidgets.QPushButton(self.centralwidget)
        self.close_Button.setGeometry(QtCore.QRect(247, 340, 110, 38))
        self.close_Button.setObjectName("close_Button")
        ################### close_Button Signal #####################
        self.close_Button.clicked.connect(lambda: self.Close_Button())

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

        self.password1_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.password1_lineEdit.setGeometry(QtCore.QRect(190, 150, 221, 36))
        self.password1_lineEdit.setFrame(True)
        self.password1_lineEdit.setObjectName("password_lineEdit")
        self.password1_lineEdit.setPlaceholderText("Enter your password")
        self.password1_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.server_address_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.server_address_lineEdit.setGeometry(QtCore.QRect(190, 190, 130, 36))
        self.server_address_lineEdit.setFrame(True)
        self.server_address_lineEdit.setObjectName("server_address_lineEdit")
        self.server_address_lineEdit.setPlaceholderText("127.0.0.1")

        self.server_port_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.server_port_lineEdit.setGeometry(QtCore.QRect(330, 190, 81, 36))
        self.server_port_lineEdit.setFrame(True)
        self.server_port_lineEdit.setObjectName("server_port_lineEdit")
        self.server_port_lineEdit.setPlaceholderText("Port")

        self.admin_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.admin_radioButton.setGeometry(QtCore.QRect(190, 230, 160, 28))
        self.admin_radioButton.setObjectName("admin_radioButton")
        # self.admin_radioButton.setChecked(True or False)
        # self.admin_radioButton.setIcon(QtGui.QIcon('url'))
        # self.admin_radioButton.setIconSize(QtCore.QSize(40,40))
        self.admin_radioButton.toggled.connect(lambda: self.Admin_radiobutton())

        self.user_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.user_radioButton.setGeometry(QtCore.QRect(190, 250, 160, 28))
        self.user_radioButton.setObjectName("user_radioButton")
        self.user_radioButton.setChecked(True)
        self.user_radioButton.toggled.connect(lambda: self.User_radiobutton())

        self.password2_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.password2_lineEdit.setGeometry(QtCore.QRect(190, 280, 221, 36))
        self.password2_lineEdit.setFrame(True)
        self.password2_lineEdit.setObjectName("password_lineEdit")
        self.password2_lineEdit.setPlaceholderText("Administration password")
        self.password2_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password2_lineEdit.setReadOnly(True)

        self.server_port_ip1 = QtWidgets.QLabel(self.centralwidget)
        self.server_port_ip1.setGeometry(QtCore.QRect(85, 200, 81, 22))
        self.server_port_ip1.setObjectName("server_port_ip1")

        self.server_port_ip2 = QtWidgets.QLabel(self.centralwidget)
        self.server_port_ip2.setGeometry(QtCore.QRect(323, 196, 10, 20))
        self.server_port_ip2.setObjectName("server_port_ip2")

        self.status_bar = QtWidgets.QStatusBar(self.centralwidget)
        self.status_bar.setGeometry(QtCore.QRect(5, 392, 490, 20))
        self.status_bar.setObjectName("status_bar")

        Login_Window.setCentralWidget(self.centralwidget)

        self.RetranslateUi(Login_Window)
        QtCore.QMetaObject.connectSlotsByName(Login_Window)

    def RetranslateUi(self, Login_Window):
        _translate = QtCore.QCoreApplication.translate
        Login_Window.setWindowTitle(_translate("Login_Window", "Login page"))
        self.login_Button.setToolTip(_translate("Login_Window", "login button"))
        self.login_Button.setText(_translate("Login_Window", "Login"))
        self.close_Button.setToolTip(_translate("Login_Window", "Close button"))
        self.close_Button.setText(_translate("Login_Window", "Close"))
        self.username.setText(_translate("Login_Window", "Username:"))
        self.password.setText(_translate("Login_Window", "Password:"))
        self.password1_lineEdit.setToolTip(_translate("Login_Window", "Enter your password"))
        self.password2_lineEdit.setToolTip(_translate("Login_Window", "Administration password"))
        self.username_lineEdit.setToolTip(_translate("Login_Window", "Enter your username"))
        self.server_address_lineEdit.setToolTip(_translate("Login_Window","Enter IP Address of server"))
        self.server_port_lineEdit.setToolTip(_translate("Login_Window", "Enter Port of server"))
        self.automation_label.setText(_translate("Login_Window", "Login page Welcome!"))
        self.server_port_ip1.setText(_translate("Login_Window", "Ip : Port"))
        self.server_port_ip2.setText(_translate("Login_Window", ":"))
        self.admin_radioButton.setText(_translate("Login_Window", "I'm Administrator"))
        self.user_radioButton.setText(_translate("Login_Window", "I'm Normal user"))
        self.status_bar.showMessage(_translate("Login_Window", "status: ok"))

    def Login_Button(self):
        Login_Window.close()
        username = self.username_lineEdit.text()
        passwd1 = self.password1_lineEdit.text()
        passwd2 = self.password2_lineEdit.text()
        ip = self.server_address_lineEdit.text()
        port = self.server_port_lineEdit.text()
        # login_page can handle input : username, password, ip, port
        if (username == "") or (passwd1 == ""):
            self.Show_notify_bad_input("1")
        elif (len(ip) < 7) or (len(ip) >= 16) or (ip == ""):
            self.Show_notify_bad_input("2")
        elif port == "":
            self.Show_notify_bad_input("3")
        elif int(port) <= 0 or int(port) > 65536:
            self.Show_notify_bad_input("3")
        elif (passwd2 == "") and (self.password2_lineEdit.isReadOnly() == False):
            self.Show_notify_bad_input("4")
        else: # ok admin want's to login or normal user?.
            if self.password2_lineEdit.isReadOnly() == False:
                Admin = admin.Admin()
                report = Admin.Login(ip, int(port), username, passwd1 + passwd2, 'admin') # passwd2 is not empty
                if report == False: # if server shuts down or cannot give service or authentication was failed this line can help me.
                    self.Show_notify_fail_login("1")
                elif report == 'Connection closed': # if user send 'exit' to server, server send me Connection closed and I can see a notify.
                    self.Show_notify_fail_login("2")

            elif self.password2_lineEdit.isReadOnly() == True:
                User = normal_user.Normal_user()
                report = User.Login(ip, int(port), username, passwd1, 'normal_user') # passwd2 is empty
                if report == False: # if server shuts down or cannot give service or authentication was failed this line can help me.
                    self.Show_notify_fail_login("1")
                elif report == 'Connection closed': # if user send 'exit' to server, server send me Connection closed and I can see a notify.
                    self.Show_notify_fail_login("2")

    def Close_Button(self):
        Login_Window.close()

    def Admin_radiobutton(self):
        if self.password2_lineEdit.isReadOnly() == True:
            self.password2_lineEdit.setReadOnly(False)
        self.status_bar.showMessage('status: please fill the Administration password')

    def User_radiobutton(self):
        if self.password2_lineEdit.isReadOnly() == False:
            self.password2_lineEdit.setReadOnly(True)
        self.status_bar.showMessage('status: ok')

    def Show_notify_fail_login(self, flag): # Internal function
        if flag == "1":
            self.status_bar.showMessage("status: login error")
            msg = QMessageBox()
            msg.setWindowTitle("Notify")
            msg.setText("Login failed")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Retry)
            msg.setDefaultButton(QMessageBox.Retry)
            msg.setDetailedText("Please check your username/password or ip/port or server maybe shutdown, please try again")
            msg.buttonClicked.connect(lambda: Login_Window.show())
            msg.exec_()
        elif flag == "2":
            msg = QMessageBox()
            msg.setWindowTitle("Notify")
            msg.setText("You are Logout from server goodbye :)")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.exec_()
            Login_Window.show()

    def Show_notify_bad_input(self, flag):
        self.status_bar.showMessage("status: empty field error")
        if flag == "1": # username or password
            msg = QMessageBox()
            msg.setWindowTitle("Notify")
            msg.setText("Please fill username or password field!")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.buttonClicked.connect(lambda: Login_Window.show())
            msg.exec_()
        elif flag == "2": # ip
            msg = QMessageBox()
            msg.setWindowTitle("Notify")
            msg.setText("Ip Address format is wrong!")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.buttonClicked.connect(lambda: Login_Window.show())
            msg.exec_()
        elif flag == "3": # port
            msg = QMessageBox()
            msg.setWindowTitle("Notify")
            msg.setText("Port have invalid range!")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.buttonClicked.connect(lambda: Login_Window.show())
            msg.exec_()
        if flag == "4": # administration password
            msg = QMessageBox()
            msg.setWindowTitle("Notify")
            msg.setText("Please fill Administration password field!")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.buttonClicked.connect(lambda: Login_Window.show())
            msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)  # create a application and get it system argument.
    Login_Window = QMainWindow()  # create a main window.
    ui = Ui_Login_Window()
    ui.SetupUi(Login_Window)
    Login_Window.show()
    sys.exit(app.exec_())  # OS can know my app.