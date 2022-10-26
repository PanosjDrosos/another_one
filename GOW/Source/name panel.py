import sys
from typing import Container
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QComboBox, QStackedLayout, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        
        self.username = QLabel()
        self.username.setText("state your name")
        self.color=QLabel()
        self.color.setText("pick a color")
        self.stacklayout = QStackedLayout()
        self.combobox=QComboBox()
        self.combobox.addItems(["red","green","blue","yellow"])
        




        self.input = QLineEdit()
        #self.input.textChanged.connect()
        self.layout= QVBoxLayout()


        button=QPushButton("start game")
        button.setCheckable(True)
        button.clicked.connect(self.welcome_warrior)
        self.layout.addWidget(self.username)
        self.layout.addWidget(self.input)

        
        self.layout.addWidget(self.color)
        self.layout.addWidget(self.combobox) 
        self.layout.addWidget(button)

        container=QWidget()
        container.setLayout(self.layout)
    

        self.setCentralWidget(container)
        self.setFixedSize(QSize(400, 300))

    def welcome_warrior(self):
        player_name=self.input.text()
        print(player_name)
        if player_name=="":
            print("you forgot to put username")
        else:
            print("welcome to the battlefield")
        colour=self.combobox.currentText()

        print(colour)

app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec()

