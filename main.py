from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys
import PyQt5.QtWidgets as QtWidgets
from multiprocessing import Process
import os
import subprocess
import platform
import uvicorn
import contextlib
import time
import threading

from fastapi import *

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

      self.actinp = QPushButton()
      self.actinp.setText("activate fastapi")
      self.actinp.setFont(QFont('Times', 16))
      self.actinp.clicked.connect(lambda: self.create_server())
      self.layout.addWidget(self.actinp)

      self.endbtn = QPushButton()
      self.endbtn.setText("deactivate fastapi")
      self.endbtn.setFont(QFont('Times', 16))
      self.endbtn.clicked.connect(lambda: self.close_server())
      self.endbtn.setEnabled(False)
      self.layout.addWidget(self.endbtn)

      self.setLayout(self.layout)
      self.process = 0

   def create_server(self):
      print("create server")
      self.actinp.setEnabled(False)
      self.endbtn.setEnabled(True)
      self.process = Process(target=server_test) 
      self.process.start() 
   
   def close_server(self):
      print("close server")
      self.actinp.setEnabled(True)
      self.endbtn.setEnabled(False)
      self.process.terminate() 
      self.process = 0


def server_test():
   app = FastAPI()
   @app.get("/helloworld")
   async def hello_world():
      return {"result":"hello world"}
   @app.post("/uploadfile/")
   async def create_upload_file(file: UploadFile):
      fpath = os.path.join(os.getcwd(), file.filename)
      try:
         contents = file.file.read()
         with open(fpath, 'wb') as f:
            f.write(contents)
      except Exception:
         return {"message": "There was an error uploading the file"}
      finally:
         file.file.close()
      return {"message": f"Successfully uploaded {file.filename}"}
   
   kwargs={"app": app, "port": 8000}
   uvicorn.run(**kwargs)


#uvicorn.run("main:app", port = 8080, reload = True)
#config = uvicorn.Config("main:app", host="192.168.1.10", port=8008, log_level="info")

class MainWindow(QMainWindow):
   def __init__(self):
      super().__init__()
      self.setWindowTitle("PyQt5")
      self.setGeometry(100,100,1500,900)
      self.table_widget = MyTabs(self)
      self.setCentralWidget(self.table_widget)
      
   def closeEvent(self, Event):
      print("close")
      if self.table_widget.process != 0:
         self.table_widget.process.terminate()
         print("close and terminated \n")
      return


def window():
   print("Current Platform: ", platform.system())
   app = QApplication(sys.argv)
   w = MainWindow()
   w.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   print("Start")
   window()

