# PyQt5 have 620 class and 6000 method
# QtCore use for working with files, directories, URL protocols, ...
# QtGui use for working with graphical content like font-size, sentence-size, ...
# QtWidgets for working with widgets_UI like buttons, labels, combobox, ...
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
import sys
import admin, normal_user

class Ui_WorkSpace_window(object):

    def SetupUi(self, WorkSpace_window):
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
        WorkSpace_window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(WorkSpace_window)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 981, 621))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.tabWidget = QtWidgets.QTabWidget(self.gridLayoutWidget)

        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setToolTip("")
        self.tabWidget.setObjectName("tabWidget")
        self.monitoring_tab = QtWidgets.QWidget()
        self.monitoring_tab.setObjectName("monitoring_tab")
        self.groupBox_logging = QtWidgets.QGroupBox(self.monitoring_tab)
        self.groupBox_logging.setGeometry(QtCore.QRect(410, 10, 561, 571))

        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
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
        self.listView_logs = QtWidgets.QListView(self.groupBox_logging)
        self.listView_logs.setGeometry(QtCore.QRect(10, 221, 541, 341))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
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
        self.pushButton_show_log = QtWidgets.QPushButton(self.groupBox_logging)
        self.pushButton_show_log.setGeometry(QtCore.QRect(230, 170, 221, 38))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/7774226221582004489-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_show_log.setFont(font)
        self.pushButton_show_log.setIcon(icon1)
        self.pushButton_show_log.setObjectName("pushButton_show_log")
        self.lineEdit_filter = QtWidgets.QLineEdit(self.groupBox_logging)
        self.lineEdit_filter.setGeometry(QtCore.QRect(230, 130, 221, 36))

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

        self.script_tab = QtWidgets.QWidget()
        self.script_tab.setObjectName("script_tab")

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
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        WorkSpace_window.setCentralWidget(self.centralwidget)

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

        self.statusbar = QtWidgets.QStatusBar(WorkSpace_window)
        self.statusbar.setObjectName("statusbar")
        WorkSpace_window.setStatusBar(self.statusbar)

        self.RetranslateUi(WorkSpace_window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(WorkSpace_window)

    def RetranslateUi(self, WorkSpace_window):
        _translate = QtCore.QCoreApplication.translate
        WorkSpace_window.setWindowTitle(_translate("WorkSpace_window", "Workspace"))

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

# if __name__ == '__main__':
#     app = QApplication(sys.argv)  # create a application and get it system argument.
#     workspace_window = QMainWindow()  # create a main window.
#     ui = Ui_WorkSpace_window()
#     ui.SetupUi(workspace_window)
#     workspace_window.show()
#     sys.exit(app.exec_())  # OS can know my app.