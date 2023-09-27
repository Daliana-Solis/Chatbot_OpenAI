import sys
from PyQt6.QtWidgets import QMainWindow, QTextEdit,\
    QLineEdit, QPushButton, QApplication


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(700,500)

        #Add chat area
        self.chat_window = QTextEdit(self)
        self.chat_window.setGeometry(10,10,480,320) #area from side, top, width, height
        self.chat_window.setReadOnly(True) #View only

        #Add input field
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10,340,480,40) #area from side, top, width, height


        #Button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500,340,100,40) #area from side, top, width, height



        self.show()

class Chatbot:
    pass


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
