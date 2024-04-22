from PIL import Image
import os
import subprocess
import matplotlib.pyplot as plt
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QDialog
from ui import ui_app, ui_adminDiag

from faceutil import FaceUtil

database_path = 'database/'
faceutil = None
threshold = 1.10
pwd = '123456'

class AdminDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = ui_adminDiag.Ui_Dialog()  # 初始化界面
        self.ui.setupUi(self)
        self.setGeometry(950,450,400,200)
        self.ui.pwdEdit 
        # 连接信号和槽
        self.ui.buttonBox.accepted.disconnect()
        self.ui.buttonBox.rejected.disconnect()
        self.ui.buttonBox.accepted.connect(self.check_password)
        self.ui.buttonBox.rejected.connect(self.reject)
        

    def check_password(self):
        password = self.ui.pwdEdit.text()
        if password == pwd:
            print("密码正确！")
            self.accept()
        else:
            QMessageBox.warning(self, '错误', '密码错误，请重试！')
            self.ui.pwdEdit.clear()


class MainWindow(QMainWindow):
    admin_state = False

    def __init__(self):
        super().__init__()
        self.ui = ui_app.Ui_MainWindow()  # 初始化界面
        self.ui.setupUi(self)
        self.setGeometry(900,300,700,800)
        self.admin_state = False
        # 连接信号和槽
        self.ui.camRecoBtn.clicked.connect(self.camReco)
        self.ui.fileRecoBtn.clicked.connect(self.fileReco)
        self.ui.switchUserBtn.clicked.connect(self.switchUser)

    def writeLog(self, log):
        self.ui.debugOutputTextEdit.append(f"{log}")

    def switchUser(self):
        if not self.admin_state:
            dialog = AdminDialog()
            if dialog.exec_():
                self.admin_state = True
                self.writeLog('-> Admin mode')
                self.ui.userLb.setText('Admin（管理员）')
                self.ui.switchUserBtn.setText('退出登录')
                self.ui.openFaceMgrBtn.setEnabled(True)
        else:
            self.admin_state = False
            self.writeLog('-> User mode')
            self.ui.userLb.setText('User')
            self.ui.switchUserBtn.setText('管理员登录')
            self.ui.openFaceMgrBtn.setEnabled(False)

    def camReco(self):
        # 摄像头人脸比对
        QMessageBox.information(self, "提示",
                                 "即将打开相机，取景框左上角倒计时结束后会自动拍照",
                                 QMessageBox.Ok)
        self.writeLog('Opening Camera...')
        camface = faceutil.get_cam_faces()
        if len(camface) > 0:
            camface = camface[0]
        else:
            print("未检测到人脸!")
            self.writeLog('No face detected!')
            QMessageBox.warning(self, "警告",
                                "未检测到人脸",
                                QMessageBox.Ok)
            return
        # plt.imshow(camface)
        # plt.show()
        name, dist = faceutil.recognize_face(camface)
        if dist>threshold:
            print("未找到匹配的人脸！", name, dist)
            self.writeLog(f"Possible Face: {name}@{dist}")
            QMessageBox.warning(self, "警告",
                                "未找到匹配的人脸",
                                QMessageBox.Ok)
        else:
            print(f"你好，{name}", dist)
            self.writeLog(f"Possible Face: {name}@{dist}")
            QMessageBox.information(self, "检测完毕",
                                f"人脸姓名：{name}",
                                QMessageBox.Ok)
        pass

    def fileReco(self):
        options = QFileDialog.Options()
        path, _ = QFileDialog.getOpenFileName(self, "选择图片", "",
                                                  "JPEG Files (*.jpg);;All Files (*)", options=options)
        if path:
            self.writeLog(f"Image Path: {path}")
            img = Image.open(path)
            img = faceutil.get_img_faces(img)
            if len(img) > 0:
                img = img[0]
            else:
                print("未检测到人脸！")
                self.writeLog('No face detected!')
                QMessageBox.warning(self, "警告",
                                "未检测到人脸",
                                QMessageBox.Ok)
                return
            # plt.imshow(img)
            # plt.show()
            name, dist = faceutil.recognize_face(img)
            if dist>threshold:
                print("未找到匹配的人脸！", name, dist)
                self.writeLog(f"Possible Face: {name}@{dist}")
                QMessageBox.warning(self, "警告",
                                "未找到匹配的人脸",
                                QMessageBox.Ok)
            else:
                print(f"你好，{name}", dist)
                self.writeLog(f"Possible Face: {name}@{dist}")
                QMessageBox.information(self, "检测完毕",
                                f"人脸姓名：{name}",
                                QMessageBox.Ok)
            

if __name__ == '__main__':
    faceutil = FaceUtil(database_path=database_path)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
