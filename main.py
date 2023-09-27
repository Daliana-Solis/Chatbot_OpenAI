import sys
from PyQt6.QtWidgets import QMainWindow, QTextEdit,\
    QLineEdit, QPushButton, QApplication
from backend import Chatbot
import threading


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(700,500)
        self.chatbot = Chatbot()


        #Add chat area
        self.chat_window = QTextEdit(self)
        self.chat_window.setGeometry(10,10,480,320) #area from side, top, width, height
        self.chat_window.setReadOnly(True) #View only

        #Add input field
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10,340,480,40) #area from side, top, width, height
        self.input_field.returnPressed.connect(self.send_message)

        #Button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500,340,100,40) #area from side, top, width, height
        self.button.clicked.connect(self.send_message) #When user presses enter



        self.show()


    def send_message(self):
        user_input = self.input_field.text().strip() #Get what user typed
        self.chat_window.append(f"<p style='color:#333333'>Me: {user_input}</p>") #Show on chat window
        self.input_field.clear() #Clear input area from text

        #Create thread
        thread = threading.Thread(target=self.get_bot_response, args=(user_input, ))
        thread.start()

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input) #Ask Chatbot user_input
        self.chat_window.append(f"<p style='color:#333333; background-color:#E9E9E9'>Bot: {response}")



app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
