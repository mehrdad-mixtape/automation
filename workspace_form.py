# PyQt5 have 620 class and 6000 method
# QtCore use for working with files, directories, URL protocols, ...
# QtGui use for working with graphical content like font-size, sentence-size, ...
# QtWidgets for working with widgets_UI like buttons, labels, combobox, ...
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
import sys
import admin, normal_user

class Ui_WorkSpace_window(object):
    def __init__(self):
        self.user = object

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
        # self.admin_radioButton.setChecked(True or False)
        # self.admin_radioButton.setIconSize(QtCore.QSize(40,40))
        self.admin_radioButton.toggled.connect(lambda: self.Admin_radiobutton())

        self.user_radioButton = QtWidgets.QRadioButton(self.login_tab)
        self.user_radioButton.setGeometry(QtCore.QRect(400, 330, 160, 28))
        self.user_radioButton.setObjectName("user_radioButton")
        self.user_radioButton.setIcon(icon3)
        self.user_radioButton.setFont(font)
        self.user_radioButton.setChecked(True)
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

        self.comboBox_log_filter = QtWidgets.QComboBox(self.groupBox_logging)
        self.comboBox_log_filter.setGeometry(QtCore.QRect(230, 90, 221, 36))
        self.comboBox_log_filter.setObjectName("comboBox_log_filter")
        self.comboBox_log_filter.addItems(['year','mouth','day','hour','owner', 'username','workspace'])

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
        self.pushButton_create_script.setObjectName("pushButton_create_script")

        self.pushButton_edit_script = QtWidgets.QPushButton(self.script_tab)
        self.pushButton_edit_script.setGeometry(QtCore.QRect(750, 540, 99, 38))
        self.pushButton_edit_script.setFont(font)
        self.pushButton_edit_script.setObjectName("pushButton_edit_script")

        self.pushButton_delete_script = QtWidgets.QPushButton(self.script_tab)
        self.pushButton_delete_script.setGeometry(QtCore.QRect(640, 540, 99, 38))
        self.pushButton_delete_script.setFont(font)
        self.pushButton_delete_script.setObjectName("pushButton_delete_script")

        self.pushButton_update_script = QtWidgets.QPushButton(self.script_tab)
        self.pushButton_update_script.setGeometry(QtCore.QRect(530, 540, 99, 38))
        self.pushButton_update_script.setFont(font)
        self.pushButton_update_script.setObjectName("pushButton_update_script")

        self.pushButton_launch_script = QtWidgets.QPushButton(self.script_tab)
        self.pushButton_launch_script.setGeometry(QtCore.QRect(10, 540, 99, 38))
        self.pushButton_launch_script.setFont(font)
        self.pushButton_launch_script.setObjectName("pushButton_launch_script")

        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        self.progressBar_process = QtWidgets.QProgressBar(self.script_tab)
        self.progressBar_process.setGeometry(QtCore.QRect(120, 543, 401, 31))
        self.progressBar_process.setFont(font)
        self.progressBar_process.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.progressBar_process.setProperty("value", 24)
        self.progressBar_process.setObjectName("progressBar_process")

        self.tabWidget.addTab(self.script_tab, "")
        #-------------------------------------------------------------------------------#

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        WorkSpace_window.setCentralWidget(self.centralwidget)
        # ------------------------------- Menu bar -------------------------------------#
        self.menubar = QtWidgets.QMenuBar(WorkSpace_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 34))
        self.menubar.setObjectName("menubar")

        self.menuAdmin = QtWidgets.QMenu(self.menubar)
        self.menuAdmin.setObjectName("menuAdmin")

        self.menuUser = QtWidgets.QMenu(self.menubar)
        self.menuUser.setObjectName("menuUser")

        self.menuServer = QtWidgets.QMenu(self.menubar)
        self.menuServer.setObjectName("menuServer")

        self.menuRemote = QtWidgets.QMenu(self.menubar)
        self.menuRemote.setObjectName("menuRemote")

        self.menuConnection = QtWidgets.QMenu(self.menubar)
        self.menuConnection.setObjectName("menuConnection")

        WorkSpace_window.setMenuBar(self.menubar)

        self.actionNew_admin = QtWidgets.QAction(WorkSpace_window)
        self.actionNew_admin.setIcon(icon2)
        self.actionNew_admin.setObjectName("actionNew_admin")

        self.actionNew_user = QtWidgets.QAction(WorkSpace_window)
        self.actionNew_user.setIcon(icon3)
        self.actionNew_user.setObjectName("actionNew_user")

        self.actionNew_server = QtWidgets.QAction(WorkSpace_window)
        self.actionNew_server.setIcon(icon4)
        self.actionNew_server.setObjectName("actionNew_server")

        self.actionEdit_admin = QtWidgets.QAction(WorkSpace_window)
        self.actionEdit_admin.setIcon(icon2)
        self.actionEdit_admin.setObjectName("actionEdit_admin")

        self.actionEdit_user = QtWidgets.QAction(WorkSpace_window)
        self.actionEdit_user.setIcon(icon3)
        self.actionEdit_user.setObjectName("actionEdit_user")

        self.actionEdit_server = QtWidgets.QAction(WorkSpace_window)
        self.actionEdit_server.setIcon(icon4)
        self.actionEdit_server.setObjectName("actionEdit_server")

        self.actionDelete_admin = QtWidgets.QAction(WorkSpace_window)
        self.actionDelete_admin.setIcon(icon2)
        self.actionDelete_admin.setObjectName("actionDelete_admin")

        self.actionDelete_user = QtWidgets.QAction(WorkSpace_window)
        self.actionDelete_user.setIcon(icon3)
        self.actionDelete_user.setObjectName("actionDelete_user")

        self.actionDelete_server = QtWidgets.QAction(WorkSpace_window)
        self.actionDelete_server.setIcon(icon4)
        self.actionDelete_server.setObjectName("actionDelete_server")

        self.actionSSH = QtWidgets.QAction(WorkSpace_window)
        self.actionSSH.setIcon(icon5)
        self.actionSSH.setObjectName("actionSSH")

        self.actionConnection = QtWidgets.QAction(WorkSpace_window)
        self.actionConnection.setIcon(icon6)
        self.actionConnection.setObjectName("actionConnection")
        ######################## actionConnection trigger ##########################
        self.actionConnection.triggered.connect(lambda: self.AcConnection())

        self.menuAdmin.addAction(self.actionNew_admin)
        self.menuAdmin.addAction(self.actionNew_user)
        self.menuAdmin.addAction(self.actionNew_server)

        self.menuUser.addAction(self.actionEdit_admin)
        self.menuUser.addAction(self.actionEdit_user)
        self.menuUser.addAction(self.actionEdit_server)

        self.menuServer.addAction(self.actionDelete_admin)
        self.menuServer.addAction(self.actionDelete_user)
        self.menuServer.addAction(self.actionDelete_server)

        self.menuRemote.addAction(self.actionSSH)

        self.menuConnection.addAction(self.actionConnection)

        self.menubar.addAction(self.menuAdmin.menuAction())
        self.menubar.addAction(self.menuUser.menuAction())
        self.menubar.addAction(self.menuServer.menuAction())
        self.menubar.addAction(self.menuRemote.menuAction())
        self.menubar.addAction(self.menuConnection.menuAction())

        self.menubar.setDisabled(True)
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

        self.progressBar_process.setToolTip(_translate("WorkSpace_window", "Process"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.script_tab), _translate("WorkSpace_window", "Script"))

        self.menuAdmin.setTitle(_translate("WorkSpace_window", "New"))
        self.menuUser.setTitle(_translate("WorkSpace_window", "Edit"))
        self.menuServer.setTitle(_translate("WorkSpace_window", "Delete"))
        self.menuRemote.setTitle(_translate("WorkSpace_window", "Remote"))
        self.menuConnection.setTitle((_translate("WorkSpace_window", "Connection")))

        self.statusbar.setToolTip(_translate("WorkSpace_window", "Status bar section"))

        self.actionNew_admin.setText(_translate("WorkSpace_window", "Admin"))
        self.actionNew_user.setText(_translate("WorkSpace_window", "User"))
        self.actionNew_server.setText(_translate("WorkSpace_window", "Server"))

        self.actionEdit_admin.setText(_translate("WorkSpace_window", "Admin"))
        self.actionEdit_user.setText(_translate("WorkSpace_window", "User"))
        self.actionEdit_server.setText(_translate("WorkSpace_window", "Server"))

        self.actionDelete_admin.setText(_translate("WorkSpace_window", "Admin"))
        self.actionDelete_user.setText(_translate("WorkSpace_window", "User"))
        self.actionDelete_server.setText(_translate("WorkSpace_window", "Server"))

        self.actionSSH.setText(_translate("WorkSpace_window", "SSH"))

        self.actionConnection.setText(_translate("WorkSpace_window", "Close Connection"))

    def Login_Button(self):
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
                    self.menubar.setDisabled(False)
                    self.statusbar.showMessage(f'status: {username}, you login to the server successfully')

            elif self.password2_lineEdit.isReadOnly() == True:
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
                    self.menubar.setDisabled(False)
                    self.statusbar.showMessage(f'status: {username}, you login to the server successfully')

    def Close_Button(self):
        workspace_window.close()
    def Show_log_Button(self):
        if self.comboBox_log_category.currentText() == 'Login':
            log_list = self.user.Login_log(self.comboBox_log_filter.currentText(), self.lineEdit_filter.text())
            self.listView_logs.clear()
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


        elif self.comboBox_log_category.currentText() == 'Action':
            log_list = self.user.Action_log(self.comboBox_log_filter.currentText(), self.lineEdit_filter.text())
            self.listView_logs.clear()
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

    def Admin_radiobutton(self):
        if self.password2_lineEdit.isReadOnly() == True:
            self.password2_lineEdit.setReadOnly(False)
        self.statusbar.showMessage('status: please fill the Administration password')
    def User_radiobutton(self):
        if self.password2_lineEdit.isReadOnly() == False:
            self.password2_lineEdit.setReadOnly(True)
        self.statusbar.showMessage('status: ok')

    def AcConnection(self):
        self.user.Send_msg('exit')
        self.Show_notify_fail_login("3")
        workspace_window.close()
    def AcNew_Admin(self):
        pass
    def AcEdit_Admin(self):
        pass
    def AcDel_Admin(self):
        pass
    def AcNew_User(self):
        pass
    def AcEdit_User(self):
        pass
    def AcDel_User(self):
        pass
    def AcNew_Server(self):
        pass
    def AcEdit_Server(self):
        pass
    def AcDel_Server(self):
        pass
    def AcRemote(self):
        pass

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
        if flag == "4": # administration password
            msg = QMessageBox()
            msg.setWindowTitle("Notify")
            msg.setText("Please fill Administration password field!")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)  # create a application and get it system argument.
    workspace_window = QMainWindow()  # create a main window.
    ui = Ui_WorkSpace_window()
    ui.SetupUi_workspace(workspace_window)
    workspace_window.show()
    sys.exit(app.exec_())  # OS can know my app.