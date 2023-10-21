# testFastapi

bosch_auth=('FCBBF021-0CE4-45E9-9E6E-579B5F3FFC08\\697c5136-e719-40a1-a52a-11cd330bb5db', '13513f28-934d-4374-9f23-98e1e6aa6968')
bosch_software_url = 'https://api.eu1.bosch-iot-rollouts.com/rest/v1/softwaremodules/'
curl "https://api.eu1.bosch-iot-rollouts.com/rest/v1/softwaremodules" -u "FCBBF021-0CE4-45E9-9E6E-579B5F3FFC08\697c5136-e719-40a1-a52a-11cd330bb5db:13513f28-934d-4374-9f23-98e1e6aa6968" -i -X POST -H "Content-Type: application/json;charset=UTF-8" -d "[ { \"vendor\" : \"Example Ltd.\",\"name\" : \"myOs\",\"description\" : \"First version of MyOS.\",\"type\" : \"os\",\"version\" : \"1.0\" } ]"


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
