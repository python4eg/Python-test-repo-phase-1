import asyncio
import sys

from random import random

from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QHBoxLayout,
                             QVBoxLayout,
                             QMainWindow,
                             QPushButton,
                             QLineEdit,
                             QTextEdit,
                             QLabel)
from PyQt5.QtGui import QTextCursor
from quamash import QEventLoop

from client import Client


class MyWindow(QMainWindow):
    def __init__(self, loop, client):
        super().__init__()
        self.loop = loop
        self.client = client
        self.client.set_output_callback(self.output)
        self.__init_widgets()

    def send(self):
        self.client.send(self.inputWidget.text())
        self.inputWidget.setText('')

    def output(self, message):
        self.chatArea.insertPlainText(message)
        self.chatArea.insertPlainText('\n')
        self.chatArea.moveCursor(QTextCursor.End)

    def __init_widgets(self):
        self.setWindowTitle('Чат')
        self.setGeometry(0, 0, 500, 500)

        self.widget = QWidget()

        self.firstLabel = QLabel(f'Username: {self.client.user}')
        self.chatArea = QTextEdit('', self)
        self.chatArea.setReadOnly(True)
        self.chatArea.setMouseTracking(True)
        self.chatArea.textSelected = False

        self.mainLayout = QVBoxLayout()
        self.mainEditLayout = QHBoxLayout()
        self.mainLayout.addWidget(self.firstLabel)
        self.mainLayout.addWidget(self.chatArea)
        self.mainLayout.addLayout(self.mainEditLayout)

        self.inputWidget = QLineEdit()
        self.sendButton = QPushButton('Send')

        self.mainEditLayout.addWidget(self.inputWidget)
        self.mainEditLayout.addWidget(self.sendButton)

        self.setCentralWidget(self.widget)
        self.widget.setLayout(self.mainLayout)

        self.sendButton.clicked.connect(self.send)


class App(QApplication):
    def __init__(self):
        QApplication.__init__(self, sys.argv)
        self.loop = QEventLoop(self)
        asyncio.set_event_loop(self.loop)

        self.client = Client(self.loop, f'user-{int(random()*10000)}')
        self.loop.create_task(self.start())

        self.gui = MyWindow(self.loop, self.client)
        self.gui.show()
        self.loop.run_forever()

    async def start(self):
        clientConnection = self.loop.create_connection(lambda: self.client, '127.0.0.1', 8888)
        await asyncio.wait_for(clientConnection, 10000)


def main_window():
    App()


if __name__ == '__main__':
    main_window()
