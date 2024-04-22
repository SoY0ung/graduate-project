from PIL import Image
import os
import subprocess
import matplotlib.pyplot as plt
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import ui_app

from faceutil import FaceUtil

database_path = 'database/'
faceutil = None
threshold = 1.10

class MainWindow(QMainWindow, ui_app.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 初始化界面

        # 连接信号和槽
        self.startButton.clicked.connect(self.start_face_recognition)

    def start_face_recognition(self):
        # 实现人脸比对的逻辑
        print('Starting')
        pass

if __name__ == '__main__':
    faceutil = FaceUtil(database_path=database_path)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
