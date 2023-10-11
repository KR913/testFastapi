from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys
import PyQt5.QtWidgets as QtWidgets
import os
import subprocess
import platform

from fastapi import FastAPI

class Task1Tab(QScrollArea):
   def __init__(self, parent = None):
      super(Task1Tab, self).__init__(parent)

      self.setGeometry(100,100,1500,900)
      #self.setWindowTitle("PyQt5")

      self.content = QWidget()
      self.layout = QVBoxLayout(self.content)
      self.layout.setAlignment(Qt.AlignTop)

      self.title = QLabel()
      self.title.setText("Task1")
      self.title.setFont(QFont('Times', 24))
      self.title.setAlignment(Qt.AlignCenter)
      self.title.resize(1200,48)
      self.layout.addWidget(self.title)
      self.setLayout(self.layout)

class Task2Tab(QScrollArea):
    def __init__(self, parent = None):
        super(Task2Tab, self).__init__(parent)

        self.setGeometry(100,100,1500,900)
        #self.setWindowTitle("PyQt5")

        self.content = QWidget()
        self.layout = QVBoxLayout(self.content)
        self.layout.setAlignment(Qt.AlignTop)

        self.title = QLabel()
        self.title.setText("Task2")
        self.title.setFont(QFont('Times', 24))
        self.title.setAlignment(Qt.AlignCenter)
        self.title.resize(1200,48)

        self.actinp = QPushButton()
        self.actinp.setText("task2")
        self.actinp.setFont(QFont('Times', 16))

        self.layout.addWidget(self.title)
        self.layout.addWidget(self.actinp)
        self.setLayout(self.layout)

class MyTabs(QWidget):
   def __init__(self, parent):
      super(QWidget, self).__init__(parent)
      self.layout = QVBoxLayout(self)
      self.tabs = QTabWidget()
      self.tab1 = Task1Tab(self)
      self.tabs.addTab(self.tab1,"task1")
      self.tab1 = Task2Tab(self)
      self.tabs.addTab(self.tab1,"task2")
      self.layout.addWidget(self.tabs)
      self.setLayout(self.layout)
   

class MainWindow(QMainWindow):
   def __init__(self):
      super().__init__()
      self.setWindowTitle("PyQt5")
      self.setGeometry(100,100,1500,900)
      self.table_widget = MyTabs(self)
      self.setCentralWidget(self.table_widget)
      
   def closeEvent(self, Event):
      return


def window():
   print("Current Platform: ", platform.system())
   app = QApplication(sys.argv)
   w = MainWindow()
   w.show()
   sys.exit(app.exec_())

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == '__main__':
    print("Start")
    window()

