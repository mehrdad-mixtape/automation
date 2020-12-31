# PyQt5 have 620 class and 6000 method
# QtCore use for working with files, directories, URL protocols, ...
# QtGui use for working with graphical content like font-size, sentence-size, ...
# QtWidgets for working with widgets_UI like buttons, labels, combobox, ...
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
import sys, time, os
import admin, normal_user

class Ui_WorkSpace_window(object):
    def __init__(self):
        self.user = object # this user can be Admin or normal_user

    def SetupUi_workspace(self, WorkSpace_window):
        WorkSpace_window.setObjectName("WorkSpace_window")
        WorkSpace_window.resize(1000, 700)
        WorkSpace_window.setGeometry(490, 170, 1000, 700)
        WorkSpace_window.setMinimumSize(QtCore.QSize(1000, 700))
        WorkSpace_window.setMaximumSize(QtCore.QSize(1000, 700))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        WorkSpace_window.setFont(font)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/2252295991582004497-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/7774226221582004489-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/469704211582004494-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/1388560951582004484-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/18070417311582004489-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icon/4609047631582004492-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icon/8474278001582004491-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icon/12355707351582004488-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icon/2058131601582004490-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icon/15586770221582004499-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icon/14458160321582004493-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icon/14787197661582004498-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icon/1959125971582004485-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        WorkSpace_window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(WorkSpace_window)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 981, 621))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        ################################ Tabs ################################################
        self.tabWidget = QtWidgets.QTabWidget(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        #-------------------------------- Login Tab -----------------------------------------#
        self.login_tab = QtWidgets.QWidget()
        self.login_tab.setObjectName("login_tab")

        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.automation_label = QtWidgets.QLabel(self.login_tab)
        self.automation_label.setGeometry(QtCore.QRect(20, 90, 936, 80))
        self.automation_label.setFont(font)
        self.automation_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.automation_label.setObjectName("automation_label")

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.username = QtWidgets.QLabel(self.login_tab)
        self.username.setGeometry(QtCore.QRect(290, 190, 91, 22))
        self.username.setFont(font)
        self.username.setObjectName("username")

        self.username_lineEdit = QtWidgets.QLineEdit(self.login_tab)
        self.username_lineEdit.setGeometry(QtCore.QRect(400, 190, 221, 36))
        self.username_lineEdit.setFrame(True)
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.username_lineEdit.setPlaceholderText("Enter your username")

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.password = QtWidgets.QLabel(self.login_tab)
        self.password.setGeometry(QtCore.QRect(290, 230, 81, 22))
        self.password.setFont(font)
        self.password.setObjectName("Password")

        self.password1_lineEdit = QtWidgets.QLineEdit(self.login_tab)
        self.password1_lineEdit.setGeometry(QtCore.QRect(400, 230, 221, 36))
        self.password1_lineEdit.setFrame(True)
        self.password1_lineEdit.setObjectName("password_lineEdit")
        self.password1_lineEdit.setPlaceholderText("Enter your password")
        self.password1_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.server_port_ip1 = QtWidgets.QLabel(self.login_tab)
        self.server_port_ip1.setGeometry(QtCore.QRect(290, 270, 81, 22))
        self.server_port_ip1.setFont(font)
        self.server_port_ip1.setObjectName("server_port_ip1")

        self.server_port_ip2 = QtWidgets.QLabel(self.login_tab)
        self.server_port_ip2.setGeometry(QtCore.QRect(533, 276, 10, 20))
        self.server_port_ip2.setFont(font)
        self.server_port_ip2.setObjectName("server_port_ip2")

        self.server_address_lineEdit = QtWidgets.QLineEdit(self.login_tab)
        self.server_address_lineEdit.setGeometry(QtCore.QRect(400, 270, 130, 36))
        self.server_address_lineEdit.setFrame(True)
        self.server_address_lineEdit.setObjectName("server_address_lineEdit")
        self.server_address_lineEdit.setPlaceholderText("127.0.0.1")

        self.server_port_lineEdit = QtWidgets.QLineEdit(self.login_tab)
        self.server_port_lineEdit.setGeometry(QtCore.QRect(540, 270, 81, 36))
        self.server_port_lineEdit.setFrame(True)
        self.server_port_lineEdit.setObjectName("server_port_lineEdit")
        self.server_port_lineEdit.setPlaceholderText("Port")

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.admin_radioButton = QtWidgets.QRadioButton(self.login_tab)
        self.admin_radioButton.setGeometry(QtCore.QRect(400, 310, 165, 28))
        self.admin_radioButton.setObjectName("admin_radioButton")
        self.admin_radioButton.setIcon(icon2)
        self.admin_radioButton.setFont(font)
        ###################### remember place setChecked on user_radiobutton #############
        self.admin_radioButton.setChecked(True)
        # self.admin_radioButton.setChecked(True or False)
        # self.admin_radioButton.setIconSize(QtCore.QSize(40,40))
        self.admin_radioButton.toggled.connect(lambda: self.Admin_radiobutton())

        self.user_radioButton = QtWidgets.QRadioButton(self.login_tab)
        self.user_radioButton.setGeometry(QtCore.QRect(400, 330, 160, 28))
        self.user_radioButton.setObjectName("user_radioButton")
        self.user_radioButton.setIcon(icon3)
        self.user_radioButton.setFont(font)
        self.user_radioButton.toggled.connect(lambda: self.User_radiobutton())

        self.password2_lineEdit = QtWidgets.QLineEdit(self.login_tab)
        self.password2_lineEdit.setGeometry(QtCore.QRect(400, 360, 221, 36))
        self.password2_lineEdit.setFrame(True)
        self.password2_lineEdit.setObjectName("password_lineEdit")
        self.password2_lineEdit.setPlaceholderText("Administration password")
        self.password2_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password2_lineEdit.setReadOnly(True)

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.login_Button = QtWidgets.QPushButton(self.login_tab)
        self.login_Button.setObjectName("login_Button")
        self.login_Button.setIcon(icon1)
        self.login_Button.setFont(font)
        self.login_Button.setGeometry(QtCore.QRect(350, 420, 110, 38))
        ################### login_Button Signal #####################
        self.login_Button.clicked.connect(lambda: self.Login_Button())

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.close_Button = QtWidgets.QPushButton(self.login_tab)
        self.close_Button.setObjectName("close_Button")
        self.close_Button.setIcon(icon7)
        self.close_Button.setFont(font)
        self.close_Button.setGeometry(QtCore.QRect(470, 420, 110, 38))
        ################### close_Button Signal #####################
        self.close_Button.clicked.connect(lambda: self.Close_Button())

        ######################################
        ######################################
        ######################################
        ######################################
        self.username_lineEdit.setText('MixTape')
        self.password1_lineEdit.setText('123')
        self.password2_lineEdit.setText('45')
        self.server_address_lineEdit.setText('127.0.0.1')
        self.server_port_lineEdit.setText('4444')
        ######################################
        ######################################
        ######################################
        ######################################

        self.tabWidget.addTab(self.login_tab, "")
        #------------------------------------------------------------------------------------#
        #-------------------------------- Monitoring Tab ------------------------------------#
        self.monitoring_tab = QtWidgets.QWidget()
        self.monitoring_tab.setObjectName("monitoring_tab")
        self.monitoring_tab.setDisabled(True)

        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.groupBox_logging = QtWidgets.QGroupBox(self.monitoring_tab)
        self.groupBox_logging.setGeometry(QtCore.QRect(410, 10, 561, 571))
        self.groupBox_logging.setFont(font)
        self.groupBox_logging.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.groupBox_logging.setMouseTracking(False)
        self.groupBox_logging.setAutoFillBackground(False)
        self.groupBox_logging.setFlat(False)
        self.groupBox_logging.setCheckable(False)
        self.groupBox_logging.setObjectName("groupBox_logging")

        self.comboBox_log_category = QtWidgets.QComboBox(self.groupBox_logging)
        self.comboBox_log_category.setGeometry(QtCore.QRect(230, 50, 221, 36))
        self.comboBox_log_category.setObjectName("comboBox_log_category")
        self.comboBox_log_category.addItems(['Login','Action'])
        ########################### comboBox_script Signal ###########################
        self.comboBox_log_category.activated.connect(lambda: self.Load_comboBox_log_filter())

        self.comboBox_log_filter = QtWidgets.QComboBox(self.groupBox_logging)
        self.comboBox_log_filter.setGeometry(QtCore.QRect(230, 90, 221, 36))
        self.comboBox_log_filter.setObjectName("comboBox_log_filter")

        self.label_log_category = QtWidgets.QLabel(self.groupBox_logging)
        self.label_log_category.setGeometry(QtCore.QRect(80, 51, 111, 31))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_log_category.setFont(font)
        self.label_log_category.setObjectName("label_log_category")

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.listView_logs = QtWidgets.QListWidget(self.groupBox_logging)
        self.listView_logs.setGeometry(QtCore.QRect(10, 221, 541, 341))
        self.listView_logs.setFont(font)
        self.listView_logs.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.listView_logs.setObjectName("listView_logs")

        self.label_log_filter = QtWidgets.QLabel(self.groupBox_logging)
        self.label_log_filter.setGeometry(QtCore.QRect(80, 91, 91, 31))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_log_filter.setFont(font)
        self.label_log_filter.setObjectName("label_log_filter")

        self.lineEdit_filter = QtWidgets.QLineEdit(self.groupBox_logging)
        self.lineEdit_filter.setGeometry(QtCore.QRect(230, 130, 221, 36))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)

        self.pushButton_show_log = QtWidgets.QPushButton(self.groupBox_logging)
        self.pushButton_show_log.setGeometry(QtCore.QRect(230, 170, 221, 38))
        self.pushButton_show_log.setFont(font)
        self.pushButton_show_log.setIcon(icon1)
        self.pushButton_show_log.setObjectName("pushButton_show_log")
        ################### pushButton_show_log Signal #####################
        self.pushButton_show_log.clicked.connect(lambda: self.Show_log_Button())

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lineEdit_filter.setFont(font)
        self.lineEdit_filter.setObjectName("lineEdit_filter")
        self.label_filter = QtWidgets.QLabel(self.groupBox_logging)
        self.label_filter.setGeometry(QtCore.QRect(80, 131, 111, 31))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_filter.setFont(font)
        self.label_filter.setObjectName("label_filter")
        self.groupBox_hardware = QtWidgets.QGroupBox(self.monitoring_tab)
        self.groupBox_hardware.setGeometry(QtCore.QRect(0, 10, 401, 571))

        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.groupBox_hardware.setFont(font)
        self.groupBox_hardware.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.groupBox_hardware.setObjectName("groupBox_hardware")

        self.label_CPU = QtWidgets.QLabel(self.groupBox_hardware)
        self.label_CPU.setGeometry(QtCore.QRect(40, 110, 67, 22))
        self.label_CPU.setObjectName("label_CPU")

        self.label_mem = QtWidgets.QLabel(self.groupBox_hardware)
        self.label_mem.setGeometry(QtCore.QRect(40, 160, 81, 22))
        self.label_mem.setObjectName("label_mem")

        self.label_disk = QtWidgets.QLabel(self.groupBox_hardware)
        self.label_disk.setGeometry(QtCore.QRect(40, 210, 67, 22))
        self.label_disk.setObjectName("label_disk")

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)

        self.progressBar_cpu = QtWidgets.QProgressBar(self.groupBox_hardware)
        self.progressBar_cpu.setGeometry(QtCore.QRect(130, 110, 231, 24))
        self.progressBar_cpu.setFont(font)
        self.progressBar_cpu.setProperty("value", 24)
        self.progressBar_cpu.setObjectName("progressBar_cpu")

        self.progressBar_memory = QtWidgets.QProgressBar(self.groupBox_hardware)
        self.progressBar_memory.setGeometry(QtCore.QRect(130, 160, 231, 24))
        self.progressBar_memory.setFont(font)
        self.progressBar_memory.setProperty("value", 24)
        self.progressBar_memory.setObjectName("progressBar_memory")

        self.progressBar_disk = QtWidgets.QProgressBar(self.groupBox_hardware)
        self.progressBar_disk.setGeometry(QtCore.QRect(130, 210, 231, 24))
        self.progressBar_disk.setFont(font)
        self.progressBar_disk.setProperty("value", 24)
        self.progressBar_disk.setObjectName("progressBar_disk")

        self.groupBox = QtWidgets.QGroupBox(self.groupBox_hardware)
        self.groupBox.setGeometry(QtCore.QRect(20, 260, 361, 191))
        self.groupBox.setObjectName("groupBox")

        self.progressBar_net_up = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar_net_up.setGeometry(QtCore.QRect(120, 50, 221, 24))
        self.progressBar_net_up.setFont(font)
        self.progressBar_net_up.setProperty("value", 24)
        self.progressBar_net_up.setObjectName("progressBar_net_up")

        self.progressBar_net_down = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar_net_down.setGeometry(QtCore.QRect(120, 100, 221, 24))
        self.progressBar_net_down.setFont(font)
        self.progressBar_net_down.setProperty("value", 24)
        self.progressBar_net_down.setObjectName("progressBar_net_down")

        self.progressBar_net_band = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar_net_band.setGeometry(QtCore.QRect(120, 150, 221, 24))
        self.progressBar_net_band.setFont(font)
        self.progressBar_net_band.setProperty("value", 24)
        self.progressBar_net_band.setObjectName("progressBar_net_band")

        self.label_net_up = QtWidgets.QLabel(self.groupBox)
        self.label_net_up.setGeometry(QtCore.QRect(20, 50, 67, 22))
        self.label_net_up.setObjectName("label_net_up")

        self.label_net_down = QtWidgets.QLabel(self.groupBox)
        self.label_net_down.setGeometry(QtCore.QRect(20, 100, 91, 22))
        self.label_net_down.setObjectName("label_net_down")

        self.label_net_band = QtWidgets.QLabel(self.groupBox)
        self.label_net_band.setGeometry(QtCore.QRect(20, 150, 101, 22))
        self.label_net_band.setObjectName("label_net_band")

        self.tabWidget.addTab(self.monitoring_tab, "")
        # -------------------------------------------------------------------------------#
        # ------------------------------- Script Tab ------------------------------------#
        self.script_tab = QtWidgets.QWidget()
        self.script_tab.setObjectName("script_tab")
        self.script_tab.setDisabled(True)

        self.label_script = QtWidgets.QLabel(self.script_tab)
        self.label_script.setGeometry(QtCore.QRect(20, 20, 67, 31))

        font = QtGui.QFont()
        font.setItalic(False)
        self.label_script.setFont(font)
        self.label_script.setObjectName("label_script")

        self.comboBox_script = QtWidgets.QComboBox(self.script_tab)
        self.comboBox_script.setGeometry(QtCore.QRect(90, 20, 201, 36))
        self.comboBox_script.setObjectName("comboBox_script")
        ########################### comboBox_script Signal ###########################
        self.comboBox_script.activated.connect(lambda: self.Load_lineEdit_path_script())

        self.label_path_script = QtWidgets.QLabel(self.script_tab)
        self.label_path_script.setGeometry(QtCore.QRect(310, 20, 41, 31))
        self.label_path_script.setFont(font)
        self.label_path_script.setObjectName("label_path_script")

        self.lineEdit_path_script = QtWidgets.QLineEdit(self.script_tab)
        self.lineEdit_path_script.setGeometry(QtCore.QRect(370, 20, 591, 36))

        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_path_script.setFont(font)
        self.lineEdit_path_script.setReadOnly(True)
        self.lineEdit_path_script.setObjectName("lineEdit_path_script")

        self.textEdit_script = QtWidgets.QTextEdit(self.script_tab)
        self.textEdit_script.setGeometry(QtCore.QRect(10, 100, 951, 431))

        font = QtGui.QFont()
        font.setItalic(False)
        self.textEdit_script.setFont(font)
        self.textEdit_script.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit_script.setObjectName("textEdit_script")

        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_create_script = QtWidgets.QPushButton(self.script_tab)
        self.pushButton_create_script.setGeometry(QtCore.QRect(860, 540, 99, 38))
        self.pushButton_create_script.setFont(font)
        self.pushButton_create_script.setIcon(icon8)
        self.pushButton_create_script.setObjectName("pushButton_create_script")
        ##################### create_script Signal #####################
        self.pushButton_create_script.clicked.connect(lambda: self.Create_script_Button())

        self.pushButton_edit_script = QtWidgets.QPushButton(self.script_tab)
        self.pushButton_edit_script.setGeometry(QtCore.QRect(750, 540, 99, 38))
        self.pushButton_edit_script.setFont(font)
        self.pushButton_edit_script.setIcon(icon9)
        self.pushButton_edit_script.setObjectName("pushButton_edit_script")
        ##################### edit_script Signal #####################
        self.pushButton_edit_script.clicked.connect(lambda: self.Edit_script_Button())

        self.pushButton_delete_script = QtWidgets.QPushButton(self.script_tab)
        self.pushButton_delete_script.setGeometry(QtCore.QRect(640, 540, 99, 38))
        self.pushButton_delete_script.setFont(font)
        self.pushButton_delete_script.setIcon(icon10)
        self.pushButton_delete_script.setObjectName("pushButton_delete_script")
        ##################### delete_script Signal #####################
        self.pushButton_delete_script.clicked.connect(lambda: self.Delete_script_Button())

        self.pushButton_update_script = QtWidgets.QPushButton(self.script_tab)
        self.pushButton_update_script.setGeometry(QtCore.QRect(530, 540, 99, 38))
        self.pushButton_update_script.setFont(font)
        self.pushButton_update_script.setIcon(icon11)
        self.pushButton_update_script.setObjectName("pushButton_update_script")
        ##################### update_script Signal #####################
        self.pushButton_update_script.clicked.connect(lambda: self.Update_script_Button())

        self.pushButton_launch_script = QtWidgets.QPushButton(self.script_tab)
        self.pushButton_launch_script.setGeometry(QtCore.QRect(10, 540, 99, 38))
        self.pushButton_launch_script.setFont(font)
        self.pushButton_launch_script.setIcon(icon12)
        self.pushButton_launch_script.setObjectName("pushButton_launch_script")
        ##################### launch_script Signal #####################
        self.pushButton_launch_script.clicked.connect(lambda: self.Launch_script_Button())

        self.tabWidget.addTab(self.script_tab, "")
        #-------------------------------------------------------------------------------#

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        WorkSpace_window.setCentralWidget(self.centralwidget)
        # ------------------------------- Menu bar -------------------------------------#
        self.menubar = QtWidgets.QMenuBar(WorkSpace_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 34))
        self.menubar.setObjectName("menubar")

        self.menuNew = QtWidgets.QMenu(self.menubar)
        self.menuNew.setObjectName("menuNew")

        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")

        self.menuDelete = QtWidgets.QMenu(self.menubar)
        self.menuDelete.setObjectName("menuDelete")

        self.menuRemote = QtWidgets.QMenu(self.menubar)
        self.menuRemote.setObjectName("menuRemote")

        self.menuConnection = QtWidgets.QMenu(self.menubar)
        self.menuConnection.setObjectName("menuConnection")

        WorkSpace_window.setMenuBar(self.menubar)

        self.actionNew = QtWidgets.QAction(WorkSpace_window)
        self.actionNew.setIcon(icon3)
        self.actionNew.setObjectName("actionNew")
        ######################## actionSSH trigger ##########################
        self.actionNew.triggered.connect(lambda: self.AcNew())

        self.actionNew_server = QtWidgets.QAction(WorkSpace_window)
        self.actionNew_server.setIcon(icon4)
        self.actionNew_server.setObjectName("actionNew_server")
        ######################## actionSSH trigger ##########################
        self.actionNew_server.triggered.connect(lambda: self.AcNewserv())

        self.actionEdit = QtWidgets.QAction(WorkSpace_window)
        self.actionEdit.setIcon(icon3)
        self.actionEdit.setObjectName("actionEdit")
        ######################## actionSSH trigger ##########################
        self.actionEdit.triggered.connect(lambda: self.AcEdit())

        self.actionDelete = QtWidgets.QAction(WorkSpace_window)
        self.actionDelete.setIcon(icon3)
        self.actionDelete.setObjectName("actionDelete")
        self.actionDelete.triggered.connect(lambda: self.AcDel())
        ######################## actionSSH trigger ##########################

        self.actionSSH = QtWidgets.QAction(WorkSpace_window)
        self.actionSSH.setIcon(icon5)
        self.actionSSH.setObjectName("actionSSH")
        ######################## actionSSH trigger ##########################
        self.actionSSH.triggered.connect(lambda: self.AcRemote())

        self.actionConnection = QtWidgets.QAction(WorkSpace_window)
        self.actionConnection.setIcon(icon6)
        self.actionConnection.setObjectName("actionConnection")
        ######################## actionConnection trigger ##########################
        self.actionConnection.triggered.connect(lambda: self.AcConnection())

        self.menuNew.addAction(self.actionNew)
        self.menuNew.addAction(self.actionNew_server)

        self.menuEdit.addAction(self.actionEdit)

        self.menuDelete.addAction(self.actionDelete)

        self.menuRemote.addAction(self.actionSSH)

        self.menuConnection.addAction(self.actionConnection)

        self.menubar.addAction(self.menuNew.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuDelete.menuAction())
        self.menubar.addAction(self.menuRemote.menuAction())
        self.menubar.addAction(self.menuConnection.menuAction())

        self.menuNew.setDisabled(True)
        self.menuEdit.setDisabled(True)
        self.menuDelete.setDisabled(True)
        self.menuConnection.setDisabled(True)
        # ------------------------------- Status bar ------------------------------------#
        self.statusbar = QtWidgets.QStatusBar(WorkSpace_window)
        self.statusbar.setObjectName("statusbar")
        WorkSpace_window.setStatusBar(self.statusbar)

        self.RetranslateUi_workspace(WorkSpace_window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(WorkSpace_window)

    def RetranslateUi_workspace(self, WorkSpace_window):
        _translate = QtCore.QCoreApplication.translate
        WorkSpace_window.setWindowTitle(_translate("WorkSpace_window", "Workspace"))

        self.login_Button.setToolTip(_translate("WorkSpace_window", "login button"))
        self.login_Button.setText(_translate("WorkSpace_window", "Login"))

        self.close_Button.setToolTip(_translate("WorkSpace_window", "Close button"))
        self.close_Button.setText(_translate("WorkSpace_window", "Close"))

        self.username.setText(_translate("WorkSpace_window", "Username:"))
        self.username_lineEdit.setToolTip(_translate("WorkSpace_window", "Enter your username"))

        self.password.setText(_translate("WorkSpace_window", "Password:"))
        self.password1_lineEdit.setToolTip(_translate("WorkSpace_window", "Enter your password"))
        self.password2_lineEdit.setToolTip(_translate("WorkSpace_window", "Administration password"))

        self.server_address_lineEdit.setToolTip(_translate("WorkSpace_window", "Enter IP Address of server"))
        self.server_port_lineEdit.setToolTip(_translate("WorkSpace_window", "Enter Port of server"))

        self.automation_label.setText(_translate("WorkSpace_window", "                     Login Tab Welcome!                     "))

        self.server_port_ip1.setText(_translate("WorkSpace_window", "Ip : Port"))
        self.server_port_ip2.setText(_translate("WorkSpace_window", ":"))

        self.admin_radioButton.setText(_translate("WorkSpace_window", "I'm Administrator"))
        self.user_radioButton.setText(_translate("WorkSpace_window", "I'm Normal user"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.login_tab), _translate("WorkSpace_window", "Login"))

        self.groupBox_logging.setToolTip(_translate("WorkSpace_window", "Logging status section"))
        self.groupBox_logging.setTitle(_translate("WorkSpace_window", "  Logging Status"))

        self.comboBox_log_category.setToolTip(_translate("WorkSpace_window", "Select log category"))
        self.comboBox_log_filter.setToolTip(_translate("WorkSpace_window", "Select log filter"))

        self.label_log_category.setText(_translate("WorkSpace_window", "Log Category:"))

        self.listView_logs.setToolTip(_translate("WorkSpace_window", "Log view"))

        self.label_log_filter.setText(_translate("WorkSpace_window", "Log Filter:"))

        self.pushButton_show_log.setToolTip(_translate("WorkSpace_window", "Show log button"))
        self.pushButton_show_log.setText(_translate("WorkSpace_window", "Show"))

        self.lineEdit_filter.setToolTip(_translate("WorkSpace_window", "Type your filter"))
        self.lineEdit_filter.setPlaceholderText(_translate("WorkSpace_window", "Type your filter ex: mixtape"))

        self.label_filter.setText(_translate("WorkSpace_window", "Filter Value:"))

        self.groupBox_hardware.setToolTip(_translate("WorkSpace_window", "Hardware status section"))
        self.groupBox_hardware.setTitle(_translate("WorkSpace_window", "  Hardware Status"))

        self.label_CPU.setToolTip(_translate("WorkSpace_window", "CPU"))
        self.label_CPU.setText(_translate("WorkSpace_window", "CPU:"))

        self.label_mem.setToolTip(_translate("WorkSpace_window", "Memory"))
        self.label_mem.setText(_translate("WorkSpace_window", "Memory:"))

        self.label_disk.setToolTip(_translate("WorkSpace_window", "Disk"))
        self.label_disk.setText(_translate("WorkSpace_window", "Disk:"))

        self.progressBar_cpu.setToolTip(_translate("WorkSpace_window", "Cpu usage"))
        self.progressBar_memory.setToolTip(_translate("WorkSpace_window", "Memory usage"))
        self.progressBar_disk.setToolTip(_translate("WorkSpace_window", "Disk usage"))

        self.groupBox.setTitle(_translate("WorkSpace_window", "  Network:"))

        self.progressBar_net_up.setToolTip(_translate("WorkSpace_window", "Network upload status"))
        self.progressBar_net_down.setToolTip(_translate("WorkSpace_window", "Network download status"))
        self.progressBar_net_band.setToolTip(_translate("WorkSpace_window", "Network bandwidth status"))

        self.label_net_up.setToolTip(_translate("WorkSpace_window", "Upload"))
        self.label_net_up.setText(_translate("WorkSpace_window", "Upload:"))

        self.label_net_down.setToolTip(_translate("WorkSpace_window", "Download"))
        self.label_net_down.setText(_translate("WorkSpace_window", "Download:"))

        self.label_net_band.setToolTip(_translate("WorkSpace_window", "Bandwidth"))
        self.label_net_band.setText(_translate("WorkSpace_window", "Bandwidth:"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.monitoring_tab), _translate("WorkSpace_window", "Monitoring"))

        self.label_script.setToolTip(_translate("WorkSpace_window", "Scripts list"))
        self.label_script.setText(_translate("WorkSpace_window", "Scripts:"))

        self.comboBox_script.setToolTip(_translate("WorkSpace_window", "Select your script"))

        self.label_path_script.setToolTip(_translate("WorkSpace_window", "Script path"))
        self.label_path_script.setText(_translate("WorkSpace_window", "path:"))

        self.lineEdit_path_script.setToolTip(_translate("WorkSpace_window", "Script path"))
        self.lineEdit_path_script.setPlaceholderText(_translate("WorkSpace_window", "path://"))

        self.textEdit_script.setToolTip(_translate("WorkSpace_window", "Text edit script"))

        self.pushButton_create_script.setToolTip(_translate("WorkSpace_window", "Create script"))
        self.pushButton_create_script.setText(_translate("WorkSpace_window", "Create"))

        self.pushButton_edit_script.setToolTip(_translate("WorkSpace_window", "Edit script"))
        self.pushButton_edit_script.setText(_translate("WorkSpace_window", "Edit"))

        self.pushButton_delete_script.setToolTip(_translate("WorkSpace_window", "Delete script"))
        self.pushButton_delete_script.setText(_translate("WorkSpace_window", "Delete"))

        self.pushButton_update_script.setToolTip(_translate("WorkSpace_window", "Update script"))
        self.pushButton_update_script.setText(_translate("WorkSpace_window", "Update"))

        self.pushButton_launch_script.setToolTip(_translate("WorkSpace_window", "Launch script"))
        self.pushButton_launch_script.setText(_translate("WorkSpace_window", "Launch"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.script_tab), _translate("WorkSpace_window", "Script"))

        self.menuNew.setTitle(_translate("WorkSpace_window", "New"))
        self.menuEdit.setTitle(_translate("WorkSpace_window", "Edit"))
        self.menuDelete.setTitle(_translate("WorkSpace_window", "Delete"))
        self.menuRemote.setTitle(_translate("WorkSpace_window", "Remote"))
        self.menuConnection.setTitle((_translate("WorkSpace_window", "Connection")))

        self.statusbar.setToolTip(_translate("WorkSpace_window", "Status bar section"))

        self.actionNew.setText(_translate("WorkSpace_window", "some one"))
        self.actionNew_server.setText(_translate("WorkSpace_window", "Server"))

        self.actionEdit.setText(_translate("WorkSpace_window", "Edit some one"))

        self.actionDelete.setText(_translate("WorkSpace_window", "Delete some one"))

        self.actionSSH.setText(_translate("WorkSpace_window", "SSH"))

        self.actionConnection.setText(_translate("WorkSpace_window", "Close Connection"))

    ################ Button ##################
    def Login_Button(self):
        username = self.username_lineEdit.text()
        passwd1 = self.password1_lineEdit.text()
        passwd2 = self.password2_lineEdit.text()
        ip = self.server_address_lineEdit.text()
        port = self.server_port_lineEdit.text()
        # login_tab can handle input : username, password, ip, port
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
            if self.password2_lineEdit.isReadOnly() == True:
                self.user = admin.Admin()
                report = self.user.Login(ip, int(port), username, passwd1 + passwd2, 'admin') # passwd2 is not empty

                if report == 'C_F': # if server shuts down or cannot give service or authentication was failed this line can help me.
                    self.Show_notify_fail_login("1")
                elif report == 'A_F':
                    self.Show_notify_fail_login("2")
                elif report == 'A_S':
                    self.Show_notify_fail_login("4")
                    self.login_tab.setDisabled(True)
                    self.monitoring_tab.setDisabled(False)
                    self.script_tab.setDisabled(False)
                    self.menuNew.setDisabled(False)
                    self.menuEdit.setDisabled(False)
                    self.menuDelete.setDisabled(False)
                    self.menuConnection.setDisabled(False)
                    self.statusbar.showMessage(f'status: {username}, you login to the server successfully')
                    self.Load_combobox_script()

            elif self.password2_lineEdit.isReadOnly() == False:
                self.user = normal_user.User()
                report = self.user.Login(ip, int(port), username, passwd1, 'normal_user') # passwd2 is empty

                if report == 'C_F':  # if server shuts down or cannot give service or authentication was failed this line can help me.
                    self.Show_notify_fail_login("1")
                elif report == 'A_F':
                    self.Show_notify_fail_login("2")
                elif report == 'A_S':
                    self.Show_notify_fail_login("4")
                    self.login_tab.setDisabled(True)
                    self.monitoring_tab.setDisabled(False)
                    self.script_tab.setDisabled(False)
                    self.menuAdmin.setDisabled(False)
                    self.menuServer.setDisabled(False)
                    self.menuUser.setDisabled(False)
                    self.menuConnection.setDisabled(False)
                    self.statusbar.showMessage(f'status: {username}, you login to the server successfully')
                    self.Load_combobox_script()
    def Close_Button(self):
        workspace_window.close()
    def Show_log_Button(self):
        if self.comboBox_log_category.currentText() == 'Login':

            log_list = self.user.Get_Login_log(self.comboBox_log_filter.currentText(), self.lineEdit_filter.text())

            self.listView_logs.clear()

            if log_list != []:
                for dict in log_list:
                    for key in dict:
                        if key == 'date':
                            self.listView_logs.insertItem(0, f'Date: {dict[key]}')
                        elif key == 'content':
                            self.listView_logs.insertItem(1, f'Content: {dict[key]}')
                        elif key == 'user':
                            self.listView_logs.insertItem(2, f'User: {dict[key]}')
                        elif key == 'workspace':
                            self.listView_logs.insertItem(3, f'Workspace: {dict[key]}')
                            self.listView_logs.insertItem(4, '\n')
            else:
                self.listView_logs.insertItem(0, 'Your query have no result, please try again')

        elif self.comboBox_log_category.currentText() == 'Action':

            log_list = self.user.Get_Action_log(self.comboBox_log_filter.currentText(), self.lineEdit_filter.text())

            self.listView_logs.clear()

            if log_list != []:
                for dict in log_list:
                    for key in dict:
                        if key == 'date':
                            self.listView_logs.insertItem(0, f'Date: {dict[key]}')
                        elif key == 'content':
                            self.listView_logs.insertItem(1, f'Content: {dict[key]}')
                        elif key == 'user':
                            self.listView_logs.insertItem(2, f'User: {dict[key]}')
                        elif key == 'workspace':
                            self.listView_logs.insertItem(3, f'Workspace: {dict[key]}')
                            self.listView_logs.insertItem(4, '\n')
            else:
                self.listView_logs.insertItem(0, 'Your query have no result, please try again')
    def Create_script_Button(self):
        self.textEdit_script.clear()
        self.textEdit_script.canPaste()
        self.pushButton_edit_script.setDisabled(True)
        self.pushButton_create_script.setDisabled(True)
        self.pushButton_delete_script.setDisabled(True)
        self.pushButton_update_script.setDisabled(False)
        self.pushButton_launch_script.setDisabled(True)
        create_script_window.show()

        pass
    def Edit_script_Button(self):
        self.statusbar.showMessage(f"Dear {self.username_lineEdit.text()}, please save your changes with press update button")
        self.textEdit_script.clear()
        self.textEdit_script.canPaste()
        self.comboBox_script.setDisabled(True)
        self.pushButton_edit_script.setDisabled(True)
        self.pushButton_create_script.setDisabled(True)
        self.pushButton_delete_script.setDisabled(True)
        self.pushButton_update_script.setDisabled(False)
        self.pushButton_launch_script.setDisabled(True)

        script_content = self.user.Edit_script(self.comboBox_script.currentText())
        self.textEdit_script.setText(script_content)
    def Delete_script_Button(self):
        result = self.user.Delete_script(self.comboBox_script.currentText())
        if result != False:
            self.statusbar.showMessage(f"Dear {self.username_lineEdit.text()}, current script deleted")
            self.Load_combobox_script()
        else:
            self.statusbar.showMessage(f"Dear {self.username_lineEdit.text()}, current script not found")
    def Update_script_Button(self):
        self.statusbar.showMessage(f"Dear {self.username_lineEdit.text()}, all changes saved on server")
        self.comboBox_script.setDisabled(False)
        self.user.Update_script(self.comboBox_script.currentText(), self.textEdit_script.toPlainText())
        self.pushButton_edit_script.setDisabled(False)
        self.pushButton_create_script.setDisabled(False)
        self.pushButton_delete_script.setDisabled(False)
        self.pushButton_update_script.setDisabled(True)
        self.pushButton_launch_script.setDisabled(False)
    def Launch_script_Button(self):
        self.user.Launch_script(self.comboBox_script.currentText())
        self.statusbar.showMessage(f"Dear {self.username_lineEdit.text()}, {self.comboBox_script.currentText()} launched successfully")

    ################ combobox ##################
    def Load_comboBox_log_filter(self):
        if self.comboBox_log_category.currentText() == 'Login':
            self.comboBox_log_filter.clear()
            self.comboBox_log_filter.addItems(['year', 'mouth', 'day', 'hour', 'username', 'workspace'])
        elif self.comboBox_log_category.currentText() == 'Action':
            self.comboBox_log_filter.clear()
            self.comboBox_log_filter.addItems(['year', 'mouth', 'day', 'hour', 'owner', 'workspace'])
    def Load_combobox_script(self):
        self.comboBox_script.clear()
        for dict in self.user.Load_all_script():
            for key in dict:
                if key == 'script_name':
                    self.comboBox_script.addItem(dict[key])
    def Load_lineEdit_path_script(self):
        self.pushButton_update_script.setDisabled(True)
        self.textEdit_script.clear()
        report = self.user.Load_path_script(self.comboBox_script.currentText())
        self.lineEdit_path_script.setText(report + self.comboBox_script.currentText())

    ################ radio Button ##################
    def Admin_radiobutton(self):
        if self.password2_lineEdit.isReadOnly() == True:
            self.password2_lineEdit.setReadOnly(False)
        self.statusbar.showMessage('status: please fill the Administration password')
    def User_radiobutton(self):
        if self.password2_lineEdit.isReadOnly() == False:
            self.password2_lineEdit.setReadOnly(True)
        self.statusbar.showMessage('status: ok')

    ################ action Menu bar ##################
    def AcNew(self):
        self.monitoring_tab.setDisabled(True)
        self.script_tab.setDisabled(True)
        create_new_window.show()
    def AcNewserv(self):
        self.monitoring_tab.setDisabled(True)
        self.script_tab.setDisabled(True)
        create_new_server_window.show()
    def AcEdit(self):
        self.monitoring_tab.setDisabled(True)
        self.script_tab.setDisabled(True)
        update_window.show()
    def AcDel(self):
        self.monitoring_tab.setDisabled(True)
        self.script_tab.setDisabled(True)
        delete_window.show()
    def AcRemote(self):
        os.system('Konsole || gnome-terminal')
    def AcConnection(self):
        self.user.Send_msg('exit')
        self.Show_notify_fail_login("3")
        workspace_window.close()

    ################ notify ##################
    def Show_notify_fail_login(self, flag): # Internal function
        if flag == "1":
            self.statusbar.showMessage("status: Connection Error")
            msg = QMessageBox()
            msg.setWindowTitle("Notify")
            msg.setText("Connection failed")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Retry)
            msg.setDefaultButton(QMessageBox.Retry)
            msg.setDetailedText("Please check your <internet connection> or <Server maybe is shutdown>, Try Again")
            msg.exec_()
        elif flag == "2":
            self.statusbar.showMessage("status: Authentication Error")
            msg = QMessageBox()
            msg.setWindowTitle("Notify")
            msg.setText("Authentication failed")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Retry)
            msg.setDefaultButton(QMessageBox.Retry)
            msg.setDetailedText("Please check your <username/password> or <ip/port>, Try again")
            msg.exec_()
        elif flag == "3":
            msg = QMessageBox()
            msg.setWindowTitle("Notify")
            msg.setText("You are Logout from the server successfully, bye")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.exec_()
        elif flag == "4":
            msg = QMessageBox()
            msg.setWindowTitle("Notify")
            msg.setText("You are login to the server successfully")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.exec_()
    def Show_notify_bad_input(self, flag):
        self.statusbar.showMessage("status: empty field error")
        if flag == "1": # username or password
            msg = QMessageBox()
            msg.setWindowTitle("Notify")
            msg.setText("Please fill username or password field!")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.exec_()
        elif flag == "2": # ip
            msg = QMessageBox()
            msg.setWindowTitle("Notify")
            msg.setText("Ip Address format is wrong!")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.exec_()
        elif flag == "3": # port
            msg = QMessageBox()
            msg.setWindowTitle("Notify")
            msg.setText("Port have invalid range!")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.exec_()
        elif flag == "4": # administration password
            msg = QMessageBox()
            msg.setWindowTitle("Notify")
            msg.setText("Please fill Administration password field!")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.exec_()
        elif flag == "5":
            msg = QMessageBox()
            msg.setWindowTitle("Notify")
            msg.setText("Please fill all field")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.exec_()

class Ui_Create_script_Window(object):

    def SetupUi_create_script(self, Create_script_Window):
        Create_script_Window.setObjectName("Create_script_Window")
        Create_script_Window.resize(552, 182)
        Create_script_Window.setGeometry(700, 300, 552, 182)
        Create_script_Window.setMinimumSize(QtCore.QSize(552, 182))
        Create_script_Window.setMaximumSize(QtCore.QSize(552, 182))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI/../icon/2252295991582004497-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Create_script_Window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Create_script_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 91, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 20, 67, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 67, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_script_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_script_name.setGeometry(QtCore.QRect(110, 20, 171, 31))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lineEdit_script_name.setFont(font)
        self.lineEdit_script_name.setObjectName("lineEdit_script_name")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(370, 20, 171, 31))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 80, 531, 36))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.pushButton_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancel.setGeometry(QtCore.QRect(440, 130, 99, 38))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("UI/../icon/12355707351582004488-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_cancel.setIcon(icon1)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        ############################ Cancel Signal ############################
        self.pushButton_cancel.clicked.connect(lambda: self.Cancel_Button())

        self.pushButton_ok = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ok.setGeometry(QtCore.QRect(330, 130, 99, 38))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("UI/../icon/7774226221582004489-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_ok.setIcon(icon2)
        self.pushButton_ok.setObjectName("pushButton_ok")
        ############################ Ok Signal ############################
        self.pushButton_ok.clicked.connect(lambda: self.Ok_Button())

        Create_script_Window.setCentralWidget(self.centralwidget)

        self.RetranslateUi_create_script(Create_script_Window)
        QtCore.QMetaObject.connectSlotsByName(Create_script_Window)

    def RetranslateUi_create_script(self, Create_script_Window):
        _translate = QtCore.QCoreApplication.translate
        Create_script_Window.setWindowTitle(_translate("Create_script_Window", "Create script"))
        Create_script_Window.setToolTip(_translate("Create_script_Window", "Create script window"))
        self.label.setText(_translate("Create_script_Window", "Script name:"))
        self.label_2.setText(_translate("Create_script_Window", "Usability:"))
        self.label_3.setText(_translate("Create_script_Window", "path:"))
        self.lineEdit_script_name.setToolTip(_translate("Create_script_Window", "Enter script_name.py"))
        self.lineEdit_script_name.setPlaceholderText(_translate("Create_script_Window", "script name"))
        self.lineEdit_2.setToolTip(_translate("Create_script_Window", "Enter script usability"))
        self.lineEdit_2.setPlaceholderText(_translate("Create_script_Window", "usability"))
        self.lineEdit_3.setToolTip(_translate("Create_script_Window", "Enter path script"))
        self.lineEdit_3.setPlaceholderText(_translate("Create_script_Window", "path:"))
        self.pushButton_cancel.setText(_translate("Create_script_Window", "Cancel"))
        self.pushButton_ok.setText(_translate("Create_script_Window", "OK"))

    def Ok_Button(self):
        script_name = self.lineEdit_script_name.text()
        usability = self.lineEdit_2.text()
        path = self.lineEdit_3.text()
        ui_1.pushButton_edit_script.setDisabled(False)
        ui_1.pushButton_create_script.setDisabled(True)
        ui_1.pushButton_delete_script.setDisabled(True)
        ui_1.pushButton_update_script.setDisabled(True)
        ui_1.pushButton_launch_script.setDisabled(True)
        ui_1.user.Create_script(script_name, path, usability)
        ui_1.Load_combobox_script()
        ui_1.statusbar.showMessage(f"Dear {self.username_lineEdit.text()}, new {script_name} create")
        create_script_window.close()
    def Cancel_Button(self):
        ui_1.pushButton_edit_script.setDisabled(False)
        ui_1.pushButton_create_script.setDisabled(False)
        ui_1.pushButton_delete_script.setDisabled(False)
        ui_1.pushButton_update_script.setDisabled(True)
        ui_1.pushButton_launch_script.setDisabled(False)
        create_script_window.close()

class Ui_Create_New_Window(object):
    def SetupUi_create_new(self, Create_New_Window):
        Create_New_Window.setObjectName("Create_New_Window")
        Create_New_Window.resize(400, 700)
        Create_New_Window.setGeometry(88, 170, 400, 700)
        Create_New_Window.setMinimumSize(QtCore.QSize(400, 700))
        Create_New_Window.setMaximumSize(QtCore.QSize(400, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/2252295991582004497-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Create_New_Window.setWindowIcon(icon)
        Create_New_Window.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(Create_New_Window)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_ok = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ok.setGeometry(QtCore.QRect(180, 650, 99, 38))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/7774226221582004489-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_ok.setIcon(icon1)
        self.pushButton_ok.setObjectName("pushButton_ok")
        ############################ Ok Signal ############################
        self.pushButton_ok.clicked.connect(lambda: self.Ok_Button())

        self.pushButton_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancel.setGeometry(QtCore.QRect(290, 650, 99, 38))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/12355707351582004488-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_cancel.setIcon(icon2)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        ############################ Cancel Signal ############################
        self.pushButton_cancel.clicked.connect(lambda: self.Cancel_Button())

        self.lineEdit_Username = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Username.setGeometry(QtCore.QRect(160, 80, 211, 36))
        self.lineEdit_Username.setObjectName("lineEdit_Username")
        self.label_Username = QtWidgets.QLabel(self.centralwidget)
        self.label_Username.setGeometry(QtCore.QRect(40, 90, 81, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Username.setFont(font)
        self.label_Username.setObjectName("label_Username")
        self.lineEdit_Password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Password.setGeometry(QtCore.QRect(160, 120, 211, 36))
        self.lineEdit_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.lineEdit_Fname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Fname.setGeometry(QtCore.QRect(160, 160, 211, 36))
        self.lineEdit_Fname.setObjectName("lineEdit_Fname")
        self.lineEdit_Lname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Lname.setGeometry(QtCore.QRect(160, 200, 211, 36))
        self.lineEdit_Lname.setObjectName("lineEdit_Lname")
        self.label_Password = QtWidgets.QLabel(self.centralwidget)
        self.label_Password.setGeometry(QtCore.QRect(40, 130, 81, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Password.setFont(font)
        self.label_Password.setObjectName("label_Password")
        self.label_Fname = QtWidgets.QLabel(self.centralwidget)
        self.label_Fname.setGeometry(QtCore.QRect(40, 170, 81, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Fname.setFont(font)
        self.label_Fname.setObjectName("label_Fname")
        self.label_Lname = QtWidgets.QLabel(self.centralwidget)
        self.label_Lname.setGeometry(QtCore.QRect(40, 210, 81, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Lname.setFont(font)
        self.label_Lname.setObjectName("label_Lname")
        self.label_Bdate = QtWidgets.QLabel(self.centralwidget)
        self.label_Bdate.setGeometry(QtCore.QRect(40, 250, 81, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Bdate.setFont(font)
        self.label_Bdate.setObjectName("label_Bdate")
        self.lineEdit_Email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Email.setGeometry(QtCore.QRect(160, 510, 211, 36))
        self.lineEdit_Email.setObjectName("lineEdit_Email")
        self.lineEdit_Phone = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Phone.setGeometry(QtCore.QRect(160, 550, 211, 36))
        self.lineEdit_Phone.setObjectName("lineEdit_Phone")
        self.label_Email = QtWidgets.QLabel(self.centralwidget)
        self.label_Email.setGeometry(QtCore.QRect(40, 520, 67, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Email.setFont(font)
        self.label_Email.setObjectName("label_Email")
        self.label_Phone = QtWidgets.QLabel(self.centralwidget)
        self.label_Phone.setGeometry(QtCore.QRect(40, 560, 67, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Phone.setFont(font)
        self.label_Phone.setObjectName("label_Phone")
        self.label_Perm = QtWidgets.QLabel(self.centralwidget)
        self.label_Perm.setGeometry(QtCore.QRect(40, 600, 91, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Perm.setFont(font)
        self.label_Perm.setObjectName("label_Perm")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 20, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")

        self.radioButton_yes = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_yes.setGeometry(QtCore.QRect(150, 600, 61, 26))
        self.radioButton_yes.setObjectName("radioButton_yes")
        self.radioButton_no = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_no.setGeometry(QtCore.QRect(210, 600, 61, 26))
        self.radioButton_no.setObjectName("radioButton_no")

        self.calendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar.setGeometry(QtCore.QRect(40, 280, 331, 221))
        self.calendar.setMinimumSize(QtCore.QSize(331, 221))
        self.calendar.setMaximumSize(QtCore.QSize(331, 221))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.calendar.setFont(font)
        self.calendar.setObjectName("calendar")
        self.comboBox_target = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_target.setGeometry(QtCore.QRect(200, 30, 171, 36))
        self.comboBox_target.setObjectName("comboBox_target")
        self.comboBox_target.addItems(['Admin', 'User'])
        ########################### comboBox_script Signal ###########################
        self.comboBox_target.activated.connect(lambda: self.Radio_Y_N())

        Create_New_Window.setCentralWidget(self.centralwidget)

        self.RetranslateUi_create_new(Create_New_Window)
        QtCore.QMetaObject.connectSlotsByName(Create_New_Window)

    def RetranslateUi_create_new(self, Create_New_Window):
        _translate = QtCore.QCoreApplication.translate
        Create_New_Window.setWindowTitle(_translate("Create_New_Window", "New"))
        self.pushButton_ok.setText(_translate("Create_New_Window", "OK"))
        self.pushButton_cancel.setText(_translate("Create_New_Window", "Cancel"))
        self.lineEdit_Username.setToolTip(_translate("Create_New_Window", "Enter your username"))
        self.label_Username.setText(_translate("Create_New_Window", "Username:"))
        self.lineEdit_Password.setToolTip(_translate("Create_New_Window", "Enter your password"))
        self.lineEdit_Fname.setToolTip(_translate("Create_New_Window", "Enter your Firstname"))
        self.lineEdit_Lname.setToolTip(_translate("Create_New_Window", "Enter your lastname"))
        self.label_Password.setText(_translate("Create_New_Window", "Password:"))
        self.label_Fname.setText(_translate("Create_New_Window", "Firstname:"))
        self.label_Lname.setText(_translate("Create_New_Window", "Lastname:"))
        self.label_Bdate.setText(_translate("Create_New_Window", "Birthdate:"))
        self.lineEdit_Email.setToolTip(_translate("Create_New_Window", "Enter your Email"))
        self.lineEdit_Phone.setToolTip(_translate("Create_New_Window", "Enter your Phone number"))
        self.label_Email.setText(_translate("Create_New_Window", "Email:"))
        self.label_Phone.setText(_translate("Create_New_Window", "Phone:"))
        self.label_Perm.setText(_translate("Create_New_Window", "Permission:"))
        self.label_9.setText(_translate("Create_New_Window", "Create New"))
        self.radioButton_yes.setText(_translate("Create_New_Window", "Yes"))
        self.radioButton_no.setText(_translate("Create_New_Window", "No"))
        self.calendar.setToolTip(_translate("Create_New_Window", "Select your Birshdate"))
        self.comboBox_target.setToolTip(_translate("Create_New_Window", "Select your target"))

    def Ok_Button(self):
        ui_1.monitoring_tab.setDisabled(False)
        ui_1.script_tab.setDisabled(False)
        U_name = self.lineEdit_Username.text()
        Passwd = self.lineEdit_Password.text()
        F_name = self.lineEdit_Fname.text()
        L_name = self.lineEdit_Lname.text()
        Email = self.lineEdit_Email.text()
        Phone = self.lineEdit_Phone.text()
        D = str(self.calendar.selectedDate().day())
        M = str(self.calendar.selectedDate().month())
        Y = str(self.calendar.selectedDate().year())
        if U_name == '' or Passwd == '' or F_name == '' or L_name == '' \
                or Email == '' or Phone == '' or D == '' or M == '' or Y == '':
            ui_1.Show_notify_bad_input("5")
        else:
            if self.comboBox_target.currentText() == 'Admin':
                ui_1.user.Admin_add(U_name, Passwd, F_name, L_name, Y, M, D, Email, Phone)
                ui_1.statusbar.showMessage(f"New Admin {U_name} Created successfully")
                create_new_window.close()
            else:
                if self.radioButton_yes.isChecked() == True:
                    ui_1.user.User_add(U_name, Passwd, F_name, L_name, Y, M, D, Email, Phone, True)
                    ui_1.statusbar.showMessage(f"New User {U_name} Created successfully")
                    create_new_window.close()
                else:
                    ui_1.user.User_add(U_name, Passwd, F_name, L_name, Y, M, D, Email, Phone, False)
                    ui_1.statusbar.showMessage(f"New User {U_name} Created successfully", False)
                    create_new_window.close()
    def Cancel_Button(self):
        ui_1.monitoring_tab.setDisabled(False)
        ui_1.script_tab.setDisabled(False)
        create_new_window.close()

    def Radio_Y_N(self):
        if self.comboBox_target.currentText() == 'Admin':
            self.radioButton_no.setDisabled(True)
            self.radioButton_yes.setDisabled(True)
        else:
            self.radioButton_no.setDisabled(False)
            self.radioButton_yes.setDisabled(False)

class Ui_New_Server_Window(object):
    def SetupUi_newserver(self, New_Server_Window):
        New_Server_Window.setObjectName("New_Server_Window")
        New_Server_Window.resize(400, 333)
        New_Server_Window.setGeometry(88, 170, 400, 333)
        New_Server_Window.setMinimumSize(QtCore.QSize(400, 333))
        New_Server_Window.setMaximumSize(QtCore.QSize(400, 333))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/2252295991582004497-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        New_Server_Window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(New_Server_Window)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancel.setGeometry(QtCore.QRect(280, 280, 99, 38))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icon/12355707351582004488-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_cancel.setIcon(icon1)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        ############################ Cancel Signal ############################
        self.pushButton_cancel.clicked.connect(lambda: self.Cancel_Button())

        self.pushButton_ok = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ok.setGeometry(QtCore.QRect(170, 280, 99, 38))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icon/7774226221582004489-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_ok.setIcon(icon2)
        self.pushButton_ok.setObjectName("pushButton_ok")
        ############################ Ok Signal ############################
        self.pushButton_ok.clicked.connect(lambda: self.Ok_Button())

        self.lineEdit_Hostname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Hostname.setGeometry(QtCore.QRect(150, 80, 211, 36))
        self.lineEdit_Hostname.setObjectName("lineEdit_Hostname")
        self.lineEdit_Password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Password.setGeometry(QtCore.QRect(150, 120, 211, 36))
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.lineEdit_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_Domain = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Domain.setGeometry(QtCore.QRect(150, 160, 211, 36))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lineEdit_Domain.setFont(font)
        self.lineEdit_Domain.setObjectName("lineEdit_Domain")
        self.lineEdit_IP = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_IP.setGeometry(QtCore.QRect(150, 200, 141, 36))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lineEdit_IP.setFont(font)
        self.lineEdit_IP.setObjectName("lineEdit_IP")
        self.lineEdit_Port = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Port.setGeometry(QtCore.QRect(300, 200, 61, 36))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lineEdit_Port.setFont(font)
        self.lineEdit_Port.setObjectName("lineEdit_Port")
        self.label_Hostname = QtWidgets.QLabel(self.centralwidget)
        self.label_Hostname.setGeometry(QtCore.QRect(40, 90, 81, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Hostname.setFont(font)
        self.label_Hostname.setObjectName("label_Hostname")
        self.label_Password = QtWidgets.QLabel(self.centralwidget)
        self.label_Password.setGeometry(QtCore.QRect(40, 130, 81, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Password.setFont(font)
        self.label_Password.setObjectName("label_Password")
        self.label_Domain = QtWidgets.QLabel(self.centralwidget)
        self.label_Domain.setGeometry(QtCore.QRect(40, 170, 67, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Domain.setFont(font)
        self.label_Domain.setObjectName("label_Domain")
        self.label_IPport = QtWidgets.QLabel(self.centralwidget)
        self.label_IPport.setGeometry(QtCore.QRect(40, 210, 67, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_IPport.setFont(font)
        self.label_IPport.setObjectName("label_IPport")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        New_Server_Window.setCentralWidget(self.centralwidget)

        self.RetranslateUi_newserver(New_Server_Window)
        QtCore.QMetaObject.connectSlotsByName(New_Server_Window)

    def RetranslateUi_newserver(self, New_Server_Window):
        _translate = QtCore.QCoreApplication.translate
        New_Server_Window.setWindowTitle(_translate("New_Server_Window", "New Server"))
        self.pushButton_cancel.setText(_translate("New_Server_Window", "Cancel"))
        self.pushButton_ok.setText(_translate("New_Server_Window", "OK"))
        self.lineEdit_Hostname.setToolTip(_translate("New_Server_Window", "Enter server Hostname"))
        self.lineEdit_Password.setToolTip(_translate("New_Server_Window", "Enter server password"))
        self.lineEdit_Domain.setToolTip(_translate("New_Server_Window", "Enter server Domain name"))
        self.lineEdit_Domain.setPlaceholderText(_translate("New_Server_Window", "www.example.com"))
        self.lineEdit_IP.setToolTip(_translate("New_Server_Window", "IP address"))
        self.lineEdit_IP.setPlaceholderText(_translate("New_Server_Window", "ex: 127.0.0.1"))
        self.lineEdit_Port.setToolTip(_translate("New_Server_Window", "Port number"))
        self.lineEdit_Port.setPlaceholderText(_translate("New_Server_Window", "port"))
        self.label_Hostname.setText(_translate("New_Server_Window", "Hostname:"))
        self.label_Password.setText(_translate("New_Server_Window", "Password:"))
        self.label_Domain.setText(_translate("New_Server_Window", "Domain:"))
        self.label_IPport.setText(_translate("New_Server_Window", "IP / Port:"))
        self.label_5.setText(_translate("New_Server_Window", "Create New Server"))

    def Ok_Button(self):
        ui_1.monitoring_tab.setDisabled(False)
        ui_1.script_tab.setDisabled(False)
        H_name = self.lineEdit_Hostname.text()
        Passwd = self.lineEdit_Password.text()
        D_name = self.lineEdit_Domain.text()
        ip = self.lineEdit_IP.text()
        port = self.lineEdit_Port.text()
        if (H_name == "") or (Passwd == "") or (D_name == ""):
            ui_1.Show_notify_bad_input("5")
        elif (len(ip) < 7) or (len(ip) >= 16) or (ip == ""):
            ui_1.Show_notify_bad_input("2")
        elif port == "":
            ui_1.Show_notify_bad_input("3")
        elif int(port) <= 0 or int(port) > 65536:
            ui_1.Show_notify_bad_input("3")
        else:
            ui_1.user.Server_add(H_name, Passwd, D_name, ip, port)
            ui_1.statusbar.showMessage(f"New server {H_name} Created successfully")
            create_new_server_window.close()
    def Cancel_Button(self):
        ui_1.monitoring_tab.setDisabled(False)
        ui_1.script_tab.setDisabled(False)
        create_new_server_window.close()

class Ui_Update_Window(object):
    def SetupUi_update(self, Update_Window):
        Update_Window.setObjectName("Update_Window")
        Update_Window.resize(400, 333)
        Update_Window.setGeometry(88, 170, 400, 333)
        Update_Window.setMinimumSize(QtCore.QSize(400, 333))
        Update_Window.setMaximumSize(QtCore.QSize(400, 333))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/2252295991582004497-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Update_Window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Update_Window)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancel.setGeometry(QtCore.QRect(290, 280, 99, 38))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icon/12355707351582004488-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_cancel.setIcon(icon2)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        ############################ Cancel Signal ############################
        self.pushButton_cancel.clicked.connect(lambda: self.Cancel_Button())

        self.pushButton_ok = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ok.setGeometry(QtCore.QRect(180, 280, 99, 38))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icon/7774226221582004489-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_ok.setIcon(icon1)
        self.pushButton_ok.setObjectName("pushButton_ok")
        ############################ Ok Signal ############################
        self.pushButton_ok.clicked.connect(lambda: self.Ok_Button())

        self.lineEdit_newvalue = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_newvalue.setGeometry(QtCore.QRect(150, 200, 211, 36))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lineEdit_newvalue.setFont(font)
        self.lineEdit_newvalue.setPlaceholderText("")
        self.lineEdit_newvalue.setObjectName("lineEdit_newvalue")
        self.label_Password = QtWidgets.QLabel(self.centralwidget)
        self.label_Password.setGeometry(QtCore.QRect(40, 130, 81, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Password.setFont(font)
        self.label_Password.setObjectName("label_Password")
        self.label_newvalue = QtWidgets.QLabel(self.centralwidget)
        self.label_newvalue.setGeometry(QtCore.QRect(40, 210, 91, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_newvalue.setFont(font)
        self.label_newvalue.setObjectName("label_newvalue")
        self.lineEdit_UserHostname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_UserHostname.setGeometry(QtCore.QRect(150, 80, 211, 36))
        self.lineEdit_UserHostname.setObjectName("lineEdit_UserHostname")
        self.lineEdit_Password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Password.setGeometry(QtCore.QRect(150, 120, 211, 36))
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.lineEdit_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_Attrib = QtWidgets.QLabel(self.centralwidget)
        self.label_Attrib.setGeometry(QtCore.QRect(40, 170, 81, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Attrib.setFont(font)
        self.label_Attrib.setObjectName("label_Attrib")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_UserHostname = QtWidgets.QLabel(self.centralwidget)
        self.label_UserHostname.setGeometry(QtCore.QRect(40, 90, 101, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_UserHostname.setFont(font)
        self.label_UserHostname.setObjectName("label_UserHostname")
        self.comboBox_target = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_target.setGeometry(QtCore.QRect(170, 30, 191, 36))
        self.comboBox_target.setObjectName("comboBox_target")
        self.comboBox_target.addItems(['Admin', 'User', 'Server'])
        ############################ comboBox_target Signal ############################
        self.comboBox_target.activated.connect(lambda: self.Load_comboBox_attrib())

        self.comboBox_attrib = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_attrib.setGeometry(QtCore.QRect(150, 160, 211, 36))
        self.comboBox_attrib.setObjectName("comboBox_attrib")
        ############################ comboBox_attrib Signal ############################
        self.comboBox_attrib.activated.connect(lambda: self.Change_echomode())

        Update_Window.setCentralWidget(self.centralwidget)

        self.RetranslateUi_update(Update_Window)
        QtCore.QMetaObject.connectSlotsByName(Update_Window)

    def RetranslateUi_update(self, Update_Window):
        _translate = QtCore.QCoreApplication.translate
        Update_Window.setWindowTitle(_translate("Update_Window", "MainWindow"))
        self.pushButton_ok.setText(_translate("Update_Window", "OK"))
        self.lineEdit_newvalue.setToolTip(_translate("Update_Window", "Port number"))
        self.label_Password.setText(_translate("Update_Window", "Password:"))
        self.label_newvalue.setText(_translate("Update_Window", "New value:"))
        self.lineEdit_UserHostname.setToolTip(_translate("Update_Window", "Enter User or Hostname"))
        self.lineEdit_Password.setToolTip(_translate("Update_Window", "Enter password"))
        self.label_Attrib.setText(_translate("Update_Window", "Attribute:"))
        self.label_5.setText(_translate("Update_Window", "Update"))
        self.pushButton_cancel.setText(_translate("Update_Window", "Cancel"))
        self.label_UserHostname.setText(_translate("Update_Window", "User or Host:"))
        self.comboBox_target.setToolTip(_translate("Update_Window", "Select your target"))
        self.comboBox_attrib.setToolTip(_translate("Update_Window", "Select your Attribute"))

    def Ok_Button(self):
        ui_1.monitoring_tab.setDisabled(False)
        ui_1.script_tab.setDisabled(False)
        H_or_U = self.lineEdit_UserHostname.text()
        Passwd = self.lineEdit_Password.text()
        Attrib = self.comboBox_attrib.currentText()
        New_val = self.lineEdit_newvalue.text()
        if self.comboBox_target.currentText() == 'Admin':
            if ui_1.user.Admin_update(H_or_U, Passwd, Attrib, New_val) == False:
                ui_1.statusbar.showMessage("Admin not found !")
            else:
                ui_1.statusbar.showMessage(f"Admin {H_or_U} updated successfully")
                update_window.close()

        elif self.comboBox_target.currentText() == 'User':
            if ui_1.user.User_update(H_or_U, Passwd, Attrib, New_val) == False:
                ui_1.statusbar.showMessage("User not found !")
            else:
                ui_1.statusbar.showMessage(f"User {H_or_U} updated successfully")
                update_window.close()

        elif self.comboBox_target.currentText() == 'Server':
            if ui_1.user.Server_update(H_or_U, Passwd, Attrib, New_val) == False:
                ui_1.statusbar.showMessage("Server not found !")
            else:
                ui_1.statusbar.showMessage(f"Server {H_or_U} updated successfully")
                update_window.close()
    def Cancel_Button(self):
        ui_1.monitoring_tab.setDisabled(False)
        ui_1.script_tab.setDisabled(False)
        update_window.close()
    def Load_comboBox_attrib(self):
        if self.comboBox_target.currentText() == 'Admin':
            self.comboBox_attrib.clear()
            self.comboBox_attrib.addItems(['username', 'password', 'first_name', 'last_name', 'birth_year', 'birth_mouth', 'birth_day', 'email' ,'phone'])
        elif self.comboBox_target.currentText() == 'User':
            self.comboBox_attrib.clear()
            self.comboBox_attrib.addItems(['username', 'password', 'first_name', 'last_name', 'birth_year', 'birth_mouth', 'birth_day', 'email', 'phone'])
        elif self.comboBox_target.currentText() == 'Server':
            self.comboBox_attrib.clear()
            self.comboBox_attrib.addItems(['hostname', 'password', 'domain', 'ip', 'port'])
    def Change_echomode(self):
        if self.comboBox_attrib.currentText() == 'password':
            self.lineEdit_newvalue.setEchoMode(QtWidgets.QLineEdit.Password)
        else:
            self.lineEdit_newvalue.setEchoMode(QtWidgets.QLineEdit.Normal)

class Ui_Delete_Window(object):
    def SetupUi_del(self, Delete_Window):
        Delete_Window.setObjectName("Delete_Window")
        Delete_Window.resize(400, 258)
        Delete_Window.setGeometry(88, 170, 400, 700)
        Delete_Window.setMinimumSize(QtCore.QSize(400, 258))
        Delete_Window.setMaximumSize(QtCore.QSize(400, 258))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/2252295991582004497-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Delete_Window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Delete_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox_target = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_target.setGeometry(QtCore.QRect(200, 30, 171, 36))
        self.comboBox_target.setObjectName("comboBox_target")
        self.comboBox_target.addItems(['Admin', 'User', 'Server'])

        self.pushButton_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancel.setGeometry(QtCore.QRect(280, 200, 99, 38))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icon/12355707351582004488-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_cancel.setIcon(icon1)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        ############################ Cancel Signal ############################
        self.pushButton_cancel.clicked.connect(lambda: self.Cancel_Button())

        self.pushButton_ok = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ok.setGeometry(QtCore.QRect(170, 200, 99, 38))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icon/7774226221582004489-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_ok.setIcon(icon2)
        self.pushButton_ok.setObjectName("pushButton_ok")
        ############################ Ok Signal ############################
        self.pushButton_ok.clicked.connect(lambda: self.Ok_Button())

        self.lineEdit_Username = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Username.setGeometry(QtCore.QRect(160, 80, 211, 36))
        self.lineEdit_Username.setObjectName("lineEdit_Username")
        self.lineEdit_Password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Password.setGeometry(QtCore.QRect(160, 120, 211, 36))
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.lineEdit_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_Username = QtWidgets.QLabel(self.centralwidget)
        self.label_Username.setGeometry(QtCore.QRect(40, 90, 101, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Username.setFont(font)
        self.label_Username.setObjectName("label_Username")
        self.label_Password = QtWidgets.QLabel(self.centralwidget)
        self.label_Password.setGeometry(QtCore.QRect(40, 130, 81, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Password.setFont(font)
        self.label_Password.setObjectName("label_Password")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        Delete_Window.setCentralWidget(self.centralwidget)

        self.RetranslateUi_del(Delete_Window)
        QtCore.QMetaObject.connectSlotsByName(Delete_Window)

    def RetranslateUi_del(self, Delete_Window):
        _translate = QtCore.QCoreApplication.translate
        Delete_Window.setWindowTitle(_translate("Delete_Window", "Delete"))
        self.comboBox_target.setToolTip(_translate("Delete_Window", "Select your target"))
        self.pushButton_cancel.setText(_translate("Delete_Window", "Cancel"))
        self.pushButton_ok.setText(_translate("Delete_Window", "OK"))
        self.lineEdit_Username.setToolTip(_translate("Delete_Window", "Enter Username or Hostname"))
        self.lineEdit_Password.setToolTip(_translate("Delete_Window", "Enter Password"))
        self.label_Username.setText(_translate("Delete_Window", "User or Host:"))
        self.label_Password.setText(_translate("Delete_Window", "Password:"))
        self.label.setText(_translate("Delete_Window", "Delete one"))

    def Ok_Button(self):
        ui_1.monitoring_tab.setDisabled(False)
        ui_1.script_tab.setDisabled(False)
        H_or_U = self.lineEdit_Username.text()
        Passwd = self.lineEdit_Password.text()
        if self.comboBox_target.currentText() == 'Admin':
            if ui_1.user.Admin_del(H_or_U, Passwd) == False:
                ui_1.statusbar.showMessage("Admin not found !")
            else:
                ui_1.statusbar.showMessage(f"Admin {H_or_U} deleted successfully")
                delete_window.close()

        elif self.comboBox_target.currentText() == 'User':
            if ui_1.user.User_del(H_or_U, Passwd) == False:
                ui_1.statusbar.showMessage("User not found !")
            else:
                ui_1.statusbar.showMessage(f"User {H_or_U} deleted successfully")
                delete_window.close()

        elif self.comboBox_target.currentText() == 'Server':
            if ui_1.user.Server_del(H_or_U, Passwd) == False:
                ui_1.statusbar.showMessage("Server not found !")
            else:
                ui_1.statusbar.showMessage(f"Server {H_or_U} deleted successfully")
                delete_window.close()

    def Cancel_Button(self):
        ui_1.monitoring_tab.setDisabled(False)
        ui_1.script_tab.setDisabled(False)
        delete_window.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)  # create a application and get it system argument.
    workspace_window = QMainWindow()  # create a workspace main window
    create_script_window = QMainWindow()
    create_new_window = QMainWindow()
    delete_window = QMainWindow()
    create_new_server_window = QMainWindow()
    update_window = QMainWindow()
    ui_1 = Ui_WorkSpace_window()
    ui_2 = Ui_Create_script_Window()
    ui_3 = Ui_Create_New_Window()
    ui_4 = Ui_Delete_Window()
    ui_5 = Ui_New_Server_Window()
    ui_6 = Ui_Update_Window()
    ui_1.SetupUi_workspace(workspace_window)
    ui_2.SetupUi_create_script(create_script_window)
    ui_3.SetupUi_create_new(create_new_window)
    ui_4.SetupUi_del(delete_window)
    ui_5.SetupUi_newserver(create_new_server_window)
    ui_6.SetupUi_update(update_window)
    workspace_window.show()
    sys.exit(app.exec_())  # OS can know my app.