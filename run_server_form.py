# PyQt5 have 620 class and 6000 method
# QtCore use for working with files, directories, URL protocols, ...
# QtGui use for working with graphical content like font-size, sentence-size, ...
# QtWidgets for working with widgets_UI like buttons, labels, combobox, ...
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
import sys
import admin

class Ui_Run_server_Window():

    def SetupUi(self, Run_server_Window):
        Run_server_Window.setObjectName("Run_server_Window")
        Run_server_Window.setEnabled(True)
        Run_server_Window.setGeometry(700, 300, 490, 420)
        Run_server_Window.setMaximumSize(QtCore.QSize(490, 420))
        Run_server_Window.setMinimumSize(QtCore.QSize(490, 420))

        font = QtGui.QFont()
        font.setPointSize(12)
        Run_server_Window.setFont(font)
        Run_server_Window.setToolTip("")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/2252295991582004497-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/7774226221582004489-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/12355707351582004488-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        Run_server_Window.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(Run_server_Window)
        self.centralwidget.setObjectName("centralwidget")

        self.automation_label = QtWidgets.QLabel(self.centralwidget)
        self.automation_label.setGeometry(QtCore.QRect(10, 10, 471, 81))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.automation_label.setFont(font)
        self.automation_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.automation_label.setObjectName("automation_label")

        self.run_Button = QtWidgets.QPushButton(self.centralwidget)
        self.run_Button.setGeometry(QtCore.QRect(127, 340, 110, 38))
        self.run_Button.setObjectName("run_Button")
        self.run_Button.setIcon(icon1)
        ################### login_Button Signal #####################
        self.run_Button.clicked.connect(lambda: self.Run_Button())

        self.close_Button = QtWidgets.QPushButton(self.centralwidget)
        self.close_Button.setGeometry(QtCore.QRect(247, 340, 110, 38))
        self.close_Button.setObjectName("close_Button")
        self.close_Button.setIcon(icon2)
        ################### close_Button Signal #####################
        self.close_Button.clicked.connect(lambda: self.Close_Button())

        self.hostname = QtWidgets.QLabel(self.centralwidget)
        self.hostname.setGeometry(QtCore.QRect(76, 120, 91, 22))
        self.hostname.setObjectName("hostname")

        self.hostname_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.hostname_lineEdit.setGeometry(QtCore.QRect(190, 110, 221, 36))
        self.hostname_lineEdit.setFrame(True)
        self.hostname_lineEdit.setObjectName("hostname_lineEdit")
        self.hostname_lineEdit.setPlaceholderText("Enter hostname")

        self.password = QtWidgets.QLabel(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(80, 160, 81, 22))
        self.password.setObjectName("Password")

        self.password_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_lineEdit.setGeometry(QtCore.QRect(190, 150, 221, 36))
        self.password_lineEdit.setFrame(True)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.password_lineEdit.setPlaceholderText("Enter password")
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

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

        # self.admin_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        # self.admin_radioButton.setGeometry(QtCore.QRect(190, 230, 160, 28))
        # self.admin_radioButton.setObjectName("admin_radioButton")
        # self.admin_radioButton.setChecked(True or False)
        # self.admin_radioButton.setIcon(QtGui.QIcon('url'))
        # self.admin_radioButton.setIconSize(QtCore.QSize(40,40))
        # self.admin_radioButton.toggled.connect(lambda: self.Admin_radiobutton())
        #
        # self.user_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        # self.user_radioButton.setGeometry(QtCore.QRect(190, 250, 160, 28))
        # self.user_radioButton.setObjectName("user_radioButton")
        # self.user_radioButton.setChecked(True)
        # self.user_radioButton.toggled.connect(lambda: self.User_radiobutton())

        # self.password2_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        # self.password2_lineEdit.setGeometry(QtCore.QRect(190, 280, 221, 36))
        # self.password2_lineEdit.setFrame(True)
        # self.password2_lineEdit.setObjectName("password_lineEdit")
        # self.password2_lineEdit.setPlaceholderText("Administration password")
        # self.password2_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        # self.password2_lineEdit.setReadOnly(True)

        self.server_port_ip1 = QtWidgets.QLabel(self.centralwidget)
        self.server_port_ip1.setGeometry(QtCore.QRect(85, 200, 81, 22))
        self.server_port_ip1.setObjectName("server_port_ip1")

        self.server_port_ip2 = QtWidgets.QLabel(self.centralwidget)
        self.server_port_ip2.setGeometry(QtCore.QRect(323, 196, 10, 20))
        self.server_port_ip2.setObjectName("server_port_ip2")

        self.status_bar = QtWidgets.QStatusBar(self.centralwidget)
        self.status_bar.setGeometry(QtCore.QRect(5, 392, 490, 20))
        self.status_bar.setObjectName("status_bar")

        Run_server_Window.setCentralWidget(self.centralwidget)

        self.RetranslateUi(Run_server_Window)
        QtCore.QMetaObject.connectSlotsByName(Run_server_Window)

    def RetranslateUi(self, Run_server_Window):
        _translate = QtCore.QCoreApplication.translate
        Run_server_Window.setWindowTitle(_translate("Run_server_Window", "Start server"))
        self.run_Button.setToolTip(_translate("Run_server_Window", "Run button"))
        self.run_Button.setText(_translate("Run_server_Window", "Run"))
        self.close_Button.setToolTip(_translate("Run_server_Window", "Close button"))
        self.close_Button.setText(_translate("Run_server_Window", "Close"))
        self.hostname.setText(_translate("Run_server_Window", "Hostname:"))
        self.password.setText(_translate("Run_server_Window", "Password:"))
        self.password_lineEdit.setToolTip(_translate("Run_server_Window", "Enter password"))
        self.hostname_lineEdit.setToolTip(_translate("Run_server_Window", "Enter hostname"))
        self.server_address_lineEdit.setToolTip(_translate("Run_server_Window","Enter IP Address"))
        self.server_port_lineEdit.setToolTip(_translate("Run_server_Window", "Enter Port"))
        self.automation_label.setText(_translate("Login_Window", "Start server Welcome!"))
        self.server_port_ip1.setText(_translate("Run_server_Window", "Ip : Port"))
        self.server_port_ip2.setText(_translate("Run_server_Window", ":"))
        # self.admin_radioButton.setText(_translate("Run_server_Window", "I'm Administrator"))
        # self.user_radioButton.setText(_translate("Login_Window", "I'm Normal user"))
        self.status_bar.showMessage(_translate("Login_Window", "status: ok"))

    def Run_Button(self):
        Run_server_Window.close()
        hostname = self.hostname_lineEdit.text()
        passwd = self.password_lineEdit.text()
        ip = self.server_address_lineEdit.text()
        port = self.server_port_lineEdit.text()
        # Run_server_page can handle input : hostname, passwd, ip, port
        if (hostname == "") or (passwd == ""):
            self.Show_notify_bad_input("1")
        elif (len(ip) < 7) or (len(ip) >= 16) or (ip == ""):
            self.Show_notify_bad_input("2")
        elif port == "":
            self.Show_notify_bad_input("3")
        elif int(port) <= 0 or int(port) > 65536:
            self.Show_notify_bad_input("3")
        else:
            A = admin.Admin()
            report = A.Start_server(hostname, passwd, ip, int(port))
            if report == False: # if hostname/password don't exist on db this line can help me.
                self.Show_notify_fail_run("1")
            elif report == "internal error": # if ip/port cannot bind to server this line can help me.
                self.Show_notify_fail_run("2")

    def Close_Button(self):
        Run_server_Window.close()

    def Show_notify_fail_run(self, flag): # Internal function
        if flag == "1":
            self.status_bar.showMessage("status: running error")
            msg = QMessageBox()
            msg.setWindowTitle("Notify")
            msg.setText("running operation failed")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Retry)
            msg.setDefaultButton(QMessageBox.Retry)
            msg.setDetailedText("Please check your hostname/password or ip/port, please try again")
            msg.buttonClicked.connect(lambda: Run_server_Window.show())
            msg.exec_()
        if flag == "2":
            self.status_bar.showMessage("status: running error")
            msg = QMessageBox()
            msg.setWindowTitle("Notify")
            msg.setText("running operation failed")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Retry)
            msg.setDefaultButton(QMessageBox.Retry)
            msg.setDetailedText("ip/port cannot bind to server, please change it")
            msg.buttonClicked.connect(lambda: Run_server_Window.show())
            msg.exec_()

    def Show_notify_bad_input(self, flag):
        self.status_bar.showMessage("status: empty field error")
        if flag == "1": # hostname or password
            msg = QMessageBox()
            msg.setWindowTitle("Notify")
            msg.setText("Please fill hostname or password field!")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.buttonClicked.connect(lambda: Run_server_Window.show())
            msg.exec_()
        elif flag == "2": # ip
            msg = QMessageBox()
            msg.setWindowTitle("Notify")
            msg.setText("Ip Address format is wrong!")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.buttonClicked.connect(lambda: Run_server_Window.show())
            msg.exec_()
        elif flag == "3": # port
            msg = QMessageBox()
            msg.setWindowTitle("Notify")
            msg.setText("Port have invalid range!")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.buttonClicked.connect(lambda: Run_server_Window.show())
            msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)  # create a application and get it system argument.
    Run_server_Window = QMainWindow()  # create a main window.
    ui = Ui_Run_server_Window()
    ui.SetupUi(Run_server_Window)
    Run_server_Window.show()
    sys.exit(app.exec_())  # OS can know my app.