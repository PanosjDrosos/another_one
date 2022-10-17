import sys
from typing import Container
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        
        self.username = QLabel()
        self.username.setText("state your name")
        self.color=QLabel()
        self.color.setText("pick a color")




        self.input = QLineEdit()
        #self.input.textChanged.connect()
        layout= QVBoxLayout()


        button=QPushButton("press me!")
        button.setCheckable(True)
        button.clicked.connect(self.welcome_warrior)
        
        layout.addWidget(self.username)
        layout.addWidget(self.input)
        layout.addWidget(self.color)
        layout.addWidget(button)

        container=QWidget()
        container.setLayout(layout)
    

        self.setCentralWidget(container)
        self.setFixedSize(QSize(400, 300))

    def welcome_warrior(self):
        print("Get ready to battle")


app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec()

