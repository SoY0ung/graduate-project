from PIL import Image
import os
import subprocess
import matplotlib.pyplot as plt
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QDialog, QInputDialog, QLineEdit, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from ui import ui_app, ui_adminDiag, ui_faceManagerWin, ui_faceIdentityWin

from faceutil import FaceUtil


## 配置区域
database_path = 'database/'
faceutil = None
threshold = 1.10
pwd = '123456'
## 配置区域（结束）

class AdminDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = ui_adminDiag.Ui_Dialog()  # 初始化界面
        self.ui.setupUi(self)
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

class ImageViewer(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.setWindowTitle('人脸预览')
        self.setGeometry(300, 300, 350, 350) 

        self.imageLabel = QLabel(self)
        self.imageLabel.setAlignment(Qt.AlignCenter)

        # 载入图片
        pixmap = QPixmap(image_path)
        self.imageLabel.setPixmap(pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))

        layout = QVBoxLayout()
        layout.addWidget(self.imageLabel)
        self.setLayout(layout)

class FaceManagerWindow(QMainWindow):

    def __init__(self, faceutil, logFunc):
        super().__init__()
        self.imageViewer = None 
        self.faceutil = faceutil
        self.logFunc = logFunc
        self.ui = ui_faceManagerWin.Ui_MainWindow()  # 初始化界面
        self.ui.setupUi(self)
        self.logFunc('Opening face manager window...')
        self.load_face_data()

        # 连接信号和槽
        self.ui.refreshBtn.clicked.connect(self.load_face_data)
        self.ui.cancelBtn.clicked.connect(self.close)
        self.ui.camAddBtn.clicked.connect(self.camAdd)
        self.ui.fileAddBtn.clicked.connect(self.fileAdd)
        self.ui.camUpdBtn.clicked.connect(self.camUpd)
        self.ui.fileUpdBtn.clicked.connect(self.fileUpd)
        self.ui.delBtn.clicked.connect(self.delFace)

        self.ui.faceDataList.itemSelectionChanged.connect(self.on_selection_changed)
        self.ui.faceDataList.doubleClicked.connect(self.previewPic)

    def load_face_data(self):
        face_list = self.faceutil.list_face()
        self.ui.faceDataList.clear()
        for face_info in face_list:
            self.ui.faceDataList.addItem(face_info) 

    def camAdd(self):
        QMessageBox.information(self, "提示",
                                 "即将打开相机，取景框左上角倒计时结束后会自动拍照",
                                 QMessageBox.Ok)
        self.logFunc('Opening Camera...')
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
        if camface is not None:
            text, okPressed = QInputDialog.getText(self, "添加人脸","请输入人脸名称", QLineEdit.Normal, "")
            if okPressed and text != '':
                if faceutil.add_face(camface, text):
                    print('成功添加人脸：'+text)
                    self.logFunc('Added face: '+text)
                    self.load_face_data()
                    QMessageBox.information(self, "人脸管理",
                                 "人脸添加成功",
                                 QMessageBox.Ok)
                else:
                    print('人脸名称已存在！')
                    QMessageBox.warning(self, "人脸管理",
                                 "人脸名称已存在",
                                 QMessageBox.Ok)
                    
    def fileAdd(self):
        options = QFileDialog.Options()
        path, _ = QFileDialog.getOpenFileName(self, "选择图片", "",
                                                  "JPEG Files (*.jpg);;All Files (*)", options=options)
        if path:
            self.logFunc(f"Image Path: {path}")
            img = Image.open(path)
            img = faceutil.get_img_faces(img)
            if len(img) > 0:
                img = img[0]
            else:
                print("未检测到人脸！")
                self.logFunc('No face detected!')
                QMessageBox.warning(self, "警告",
                                "未检测到人脸",
                                QMessageBox.Ok)
                return
        else:
            return
        if img is not None:
            text, okPressed = QInputDialog.getText(self, "添加人脸","请输入人脸名称", QLineEdit.Normal, "")
            if okPressed and text != '':
                if faceutil.add_face(img, text):
                    print('成功添加人脸：'+text)
                    self.logFunc('Added face: '+text)
                    self.load_face_data()
                    QMessageBox.information(self, "人脸管理",
                                 "人脸添加成功",
                                 QMessageBox.Ok)
                else:
                    print('人脸名称已存在！')
                    QMessageBox.warning(self, "人脸管理",
                                 "人脸名称已存在",
                                 QMessageBox.Ok)
            
    def previewPic(self):
        selected_item = self.ui.faceDataList.selectedItems()[0].text()
        image_path = database_path+selected_item+'.jpg'
        self.image_viewer = ImageViewer(image_path=image_path)
        self.image_viewer.show()

    def camUpd(self):
        selName = self.ui.faceDataList.selectedItems()[0].text()
        if QMessageBox.information(self, "提示",
                                 "即将打开相机，取景框左上角倒计时结束后会自动拍照",
                                 QMessageBox.Ok|QMessageBox.Cancel) == QMessageBox.Cancel:
            return
        self.logFunc('Opening Camera...')
        camface = faceutil.get_cam_faces()
        if len(camface) > 0:
            camface = camface[0]
        else:
            print("未检测到人脸!")
            self.logFunc('No face detected!')
            QMessageBox.warning(self, "警告",
                                "未检测到人脸",
                                QMessageBox.Ok)
            return
        if camface is not None:
            if faceutil.update_face(camface, selName):
                    print('成功更新人脸：'+selName)
                    self.logFunc('Updated face: '+selName)
                    QMessageBox.information(self, "人脸管理",
                                 "人脸更新成功",
                                 QMessageBox.Ok)

    def fileUpd(self):
        selName = self.ui.faceDataList.selectedItems()[0].text()
        options = QFileDialog.Options()
        path, _ = QFileDialog.getOpenFileName(self, "选择图片", "",
                                                  "JPEG Files (*.jpg);;All Files (*)", options=options)
        if path:
            self.logFunc(f"Image Path: {path}")
            img = Image.open(path)
            img = faceutil.get_img_faces(img)
            if len(img) > 0:
                img = img[0]
            else:
                print("未检测到人脸！")
                self.logFunc('No face detected!')
                QMessageBox.warning(self, "警告",
                                "未检测到人脸",
                                QMessageBox.Ok)
                return
        else:
            return
        if img is not None:
            if faceutil.update_face(img, selName):
                    print('成功更新人脸：'+selName)
                    self.logFunc('Updated face: '+selName)
                    QMessageBox.information(self, "人脸管理",
                                 "人脸更新成功",
                                 QMessageBox.Ok)
            else:
                print('人脸名称已存在！')
                QMessageBox.warning(self, "人脸管理",
                                "人脸名称已存在",
                                QMessageBox.Ok)
                
    def delFace(self):
        selName = self.ui.faceDataList.selectedItems()[0].text()
        if QMessageBox.question(self, "人脸删除",
                                 f"确定要删除{selName}的人脸数据吗",
                                 QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
            return
        if faceutil.remove_face(selName):
            print('成功删除人脸：'+selName)
            self.logFunc('Deleted face: '+selName)
            self.load_face_data()
            QMessageBox.information(self, "人脸管理",
                                 "人脸删除成功",
                                 QMessageBox.Ok)
        else:
            print('人脸名称不存在！')
            QMessageBox.warning(self, "人脸管理",
                                "人脸名称已存在",
                                QMessageBox.Ok)
        


    def on_selection_changed(self):
        selected_items = self.ui.faceDataList.selectedItems()
        if selected_items:  # 检查列表是否不为空
            # print("Selected Item:", selected_items[0].text())  # 输出选中的第一个项目
            self.ui.camUpdBtn.setEnabled(True)
            self.ui.fileUpdBtn.setEnabled(True)
            self.ui.delBtn.setEnabled(True)
        else:
            self.ui.camUpdBtn.setEnabled(False)
            self.ui.fileUpdBtn.setEnabled(False)
            self.ui.delBtn.setEnabled(False)

class FaceIdentityWindow(QMainWindow):

    def __init__(self, faceutil, logFunc):
        super().__init__()
        self.faceutil = faceutil
        self.logFunc = logFunc
        self.ui = ui_faceIdentityWin.Ui_MainWindow()  # 初始化界面
        self.ui.setupUi(self)
        self.logFunc('Opening face identity window...')


class MainWindow(QMainWindow):
    admin_state = False

    def __init__(self):
        super().__init__()
        self.ui = ui_app.Ui_MainWindow()  # 初始化界面
        self.ui.setupUi(self)
        self.admin_state = False
        # 连接信号和槽
        self.ui.camRecoBtn.clicked.connect(self.camReco)
        self.ui.fileRecoBtn.clicked.connect(self.fileReco)
        self.ui.switchUserBtn.clicked.connect(self.switchUser)
        self.ui.openFaceMgrBtn.clicked.connect(self.open_face_manager)
        self.ui.faceIdentityBtn.clicked.connect(self.open_face_identity)

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
                self.ui.faceIdentityBtn.setEnabled(True)
        else:
            self.admin_state = False
            self.writeLog('-> User mode')
            self.ui.userLb.setText('User')
            self.ui.switchUserBtn.setText('管理员登录')
            self.ui.openFaceMgrBtn.setEnabled(False)
            self.ui.faceIdentityBtn.setEnabled(False)

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

    def open_face_manager(self):
        self.faceManager = FaceManagerWindow(faceutil=faceutil, logFunc=self.writeLog) 
        self.faceManager.show()

    def open_face_identity(self):
        self.faceIdentity = FaceIdentityWindow(faceutil=faceutil, logFunc=self.writeLog)
        self.faceIdentity.show()
        

if __name__ == '__main__':
    faceutil = FaceUtil(database_path=database_path)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
