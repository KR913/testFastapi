# testFastapi

bosch_auth=('FCBBF021-0CE4-45E9-9E6E-579B5F3FFC08\\697c5136-e719-40a1-a52a-11cd330bb5db', '13513f28-934d-4374-9f23-98e1e6aa6968')
bosch_software_url = 'https://api.eu1.bosch-iot-rollouts.com/rest/v1/softwaremodules/'
curl "https://api.eu1.bosch-iot-rollouts.com/rest/v1/softwaremodules" -u "FCBBF021-0CE4-45E9-9E6E-579B5F3FFC08\697c5136-e719-40a1-a52a-11cd330bb5db:13513f28-934d-4374-9f23-98e1e6aa6968" -i -X POST -H "Content-Type: application/json;charset=UTF-8" -d "[ { \"vendor\" : \"Example Ltd.\",\"name\" : \"myOs\",\"description\" : \"First version of MyOS.\",\"type\" : \"os\",\"version\" : \"1.0\" } ]"



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
      self.process = 0
