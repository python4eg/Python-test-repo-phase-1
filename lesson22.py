import sys

from functools import partial

from PyQt5.QtGui import QFont, QColor, QPallete
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, 
                             QWidget,
                             QHBoxLayout,
                             QVBoxLayout,
                             QGridLayout,
                             QMainWindow,
                             QPushButton,
                             QLineEdit,
                             QListWidget,
                             QLabel,
                             QSizePolicy)


class MyWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Моє перше вікно')
        self.setGeometry(0, 0, 500, 200)
        widget = QWidget()
        firstLabel = QLabel('<h1><b><i><s>Давно не бачилися!</s></i></b></h1>')
        self.editArea = QLineEdit('0')

        mainLayout = QHBoxLayout()
        mainSubLayout = QVBoxLayout()
        mainSubLayout.addWidget(self.editArea)

        buttonLayout = QGridLayout()
        buttons = [
            {
                'name': '1',
                'row': 0,
                'col': 0
            },
            {
                'name': '2',
                'row': 0,
                'col': 1
            },
            {
                'name': '3',
                'row': 0,
                'col': 2
            },
            {
                'name': '4',
                'row': 1,
                'col': 0
            },
            {
                'name': '5',
                'row': 1,
                'col': 1
            },
            {
                'name': '6',
                'row': 1,
                'col': 2
            },
            {
                'name': '7',
                'row': 2,
                'col': 0
            },
            {
                'name': '8',
                'row': 2,
                'col': 1
            },
            {
                'name': '9',
                'row': 2,
                'col': 2
            },
            {
                'name': '0',
                'row': 3,
                'col': 0,
                'colSpan': 2
            },
            {
                'name': '=',
                'row': 3,
                'col': 2,
            },
            {
                'name': '+',
                'row': 0,
                'col': 4,
            },
            {
                'name': '-',
                'row': 1,
                'col': 4,
            },
            {
                'name': '*',
                'row': 2,
                'col': 4,
            },
            {
                'name': '/',
                'row': 3,
                'col': 4,
            }
        ]
        self.buttons = {}
        for buttonConfig in buttons:
            name = buttonConfig.get('name', '')
            btn = QPushButton(name)
            font = QFont()
            font.setBold(True)
            btn.setFont(font)
            btn.setSizePolicy(QSizePolicy.Preferred, 
                              QSizePolicy.Expanding)
            btn.setFlat(True)
            self.buttons[name] = btn
            buttonLayout.addWidget(btn, 
                                   buttonConfig['row'],
                                   buttonConfig['col'],
                                   1,
                                   buttonConfig.get('colSpan', 1))
        mainSubLayout.addLayout(buttonLayout)
        mainLayout.addLayout(mainSubLayout)
        self.history = QListWidget()
        mainLayout.addWidget(self.history)
        widget.setLayout(mainLayout)

        self.setCentralWidget(widget)

        for buttonName in self.buttons:
            btn = self.buttons[buttonName]
            if buttonName == '=':
                btn.clicked.connect(self.end)
            else:
                btn.clicked.connect(partial(self.change_text, buttonName))
                

    def change_text(self, text):
        self.editArea.setText(self.editArea.text() + text)

    def end(self):
        self.history.addItem(self.editArea.text() + ' = ' + '0')
        self.editArea.setText('')

def main_window():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    return_code = app.exec()
    sys.exit(return_code)

if __name__ == '__main__':
    main_window()
