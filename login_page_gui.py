from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Login_Window(QMainWindow): # I inherit from QMainWindow
    def __init__(self):
        super(Login_Window, self).__init__() # Login_Window can build itself object from Constructor form QMainWindow
        self.Window() # I call Window function to create fields.

    def Window(self): # label and submit button are fields on Login_Window
        self.welcome_label = QtWidgets.QLabel(self)
        self.welcome_label.setText("Welcome dear user")
        self.Update_Label_Size(self.welcome_label)
        self.welcome_label.move(180, 5)

        self.message_label = QtWidgets.QLabel(self)
        self.message_label.setText("")
        self.message_label.move(180,320)

        self.submit_button = QtWidgets.QPushButton(self)
        self.submit_button.setText("Submit")
        self.submit_button.move(202, 350)
        self.submit_button.clicked.connect(lambda: self.Submit_Button())

    def Submit_Button(self):
        self.message_label.setText("Login was Successful")
        self.Update_Label_Size(self.message_label)

    def Update_Label_Size(self, label):
        label.adjustSize()

def Show_Login_Window():
    app = QApplication(sys.argv)
    log_win = Login_Window()
    log_win.setGeometry(730, 300, 500, 400) # x,y,width,height
    log_win.setWindowTitle("Login-page")

    log_win.show()
    sys.exit(app.exec_())

Show_Login_Window()