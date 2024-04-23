# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\app.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 528)
        MainWindow.setMinimumSize(QtCore.QSize(700, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rootVLayout = QtWidgets.QVBoxLayout()
        self.rootVLayout.setObjectName("rootVLayout")
        self.winTitle = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.winTitle.sizePolicy().hasHeightForWidth())
        self.winTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.winTitle.setFont(font)
        self.winTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.winTitle.setObjectName("winTitle")
        self.rootVLayout.addWidget(self.winTitle)
        self.userFuncHLayout = QtWidgets.QHBoxLayout()
        self.userFuncHLayout.setObjectName("userFuncHLayout")
        self.const_userLb = QtWidgets.QLabel(self.centralwidget)
        self.const_userLb.setObjectName("const_userLb")
        self.userFuncHLayout.addWidget(self.const_userLb)
        self.userLb = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userLb.sizePolicy().hasHeightForWidth())
        self.userLb.setSizePolicy(sizePolicy)
        self.userLb.setObjectName("userLb")
        self.userFuncHLayout.addWidget(self.userLb)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.userFuncHLayout.addItem(spacerItem)
        self.switchUserBtn = QtWidgets.QPushButton(self.centralwidget)
        self.switchUserBtn.setObjectName("switchUserBtn")
        self.userFuncHLayout.addWidget(self.switchUserBtn)
        self.rootVLayout.addLayout(self.userFuncHLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.rootVLayout.addItem(spacerItem1)
        self.faceRecoHLayout = QtWidgets.QHBoxLayout()
        self.faceRecoHLayout.setObjectName("faceRecoHLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.faceRecoHLayout.addWidget(self.label)
        self.line = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.faceRecoHLayout.addWidget(self.line)
        self.rootVLayout.addLayout(self.faceRecoHLayout)
        self.faceRecoFuncHLayout = QtWidgets.QHBoxLayout()
        self.faceRecoFuncHLayout.setObjectName("faceRecoFuncHLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.faceRecoFuncHLayout.addItem(spacerItem2)
        self.camRecoBtn = QtWidgets.QPushButton(self.centralwidget)
        self.camRecoBtn.setObjectName("camRecoBtn")
        self.faceRecoFuncHLayout.addWidget(self.camRecoBtn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.faceRecoFuncHLayout.addItem(spacerItem3)
        self.fileRecoBtn = QtWidgets.QPushButton(self.centralwidget)
        self.fileRecoBtn.setObjectName("fileRecoBtn")
        self.faceRecoFuncHLayout.addWidget(self.fileRecoBtn)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.faceRecoFuncHLayout.addItem(spacerItem4)
        self.rootVLayout.addLayout(self.faceRecoFuncHLayout)
        spacerItem5 = QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.rootVLayout.addItem(spacerItem5)
        self.faceMgrHLayout = QtWidgets.QHBoxLayout()
        self.faceMgrHLayout.setObjectName("faceMgrHLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.faceMgrHLayout.addWidget(self.label_4)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.faceMgrHLayout.addWidget(self.line_4)
        self.rootVLayout.addLayout(self.faceMgrHLayout)
        self.faceMgrFuncHLayout = QtWidgets.QHBoxLayout()
        self.faceMgrFuncHLayout.setObjectName("faceMgrFuncHLayout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.faceMgrFuncHLayout.addItem(spacerItem6)
        self.openFaceMgrBtn = QtWidgets.QPushButton(self.centralwidget)
        self.openFaceMgrBtn.setEnabled(False)
        self.openFaceMgrBtn.setObjectName("openFaceMgrBtn")
        self.faceMgrFuncHLayout.addWidget(self.openFaceMgrBtn)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.faceMgrFuncHLayout.addItem(spacerItem7)
        self.faceIdentityBtn = QtWidgets.QPushButton(self.centralwidget)
        self.faceIdentityBtn.setEnabled(False)
        self.faceIdentityBtn.setObjectName("faceIdentityBtn")
        self.faceMgrFuncHLayout.addWidget(self.faceIdentityBtn)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.faceMgrFuncHLayout.addItem(spacerItem8)
        self.rootVLayout.addLayout(self.faceMgrFuncHLayout)
        spacerItem9 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.rootVLayout.addItem(spacerItem9)
        self.debugHLayout = QtWidgets.QHBoxLayout()
        self.debugHLayout.setObjectName("debugHLayout")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.debugHLayout.addWidget(self.label_5)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_5.sizePolicy().hasHeightForWidth())
        self.line_5.setSizePolicy(sizePolicy)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.debugHLayout.addWidget(self.line_5)
        self.rootVLayout.addLayout(self.debugHLayout)
        self.debugOutputTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.debugOutputTextEdit.setReadOnly(True)
        self.debugOutputTextEdit.setObjectName("debugOutputTextEdit")
        self.rootVLayout.addWidget(self.debugOutputTextEdit)
        self.reservedHLayout = QtWidgets.QHBoxLayout()
        self.reservedHLayout.setObjectName("reservedHLayout")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.reservedHLayout.addItem(spacerItem10)
        self.reservedLBtn = QtWidgets.QPushButton(self.centralwidget)
        self.reservedLBtn.setObjectName("reservedLBtn")
        self.reservedHLayout.addWidget(self.reservedLBtn)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.reservedHLayout.addItem(spacerItem11)
        self.reservedRBtn = QtWidgets.QPushButton(self.centralwidget)
        self.reservedRBtn.setObjectName("reservedRBtn")
        self.reservedHLayout.addWidget(self.reservedRBtn)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.reservedHLayout.addItem(spacerItem12)
        self.rootVLayout.addLayout(self.reservedHLayout)
        self.horizontalLayout_2.addLayout(self.rootVLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "人脸识别系统"))
        self.winTitle.setText(_translate("MainWindow", "人脸识别比对系统"))
        self.const_userLb.setText(_translate("MainWindow", "当前用户："))
        self.userLb.setText(_translate("MainWindow", "User"))
        self.switchUserBtn.setText(_translate("MainWindow", "管理员登录"))
        self.label.setText(_translate("MainWindow", "人脸识别"))
        self.camRecoBtn.setText(_translate("MainWindow", "从相机中识别"))
        self.fileRecoBtn.setText(_translate("MainWindow", "从文件中识别"))
        self.label_4.setText(_translate("MainWindow", "管理员选项"))
        self.openFaceMgrBtn.setText(_translate("MainWindow", "人脸库管理"))
        self.faceIdentityBtn.setText(_translate("MainWindow", "人脸比对"))
        self.label_5.setText(_translate("MainWindow", "DEBUG"))
        self.reservedLBtn.setText(_translate("MainWindow", "调试按钮（左）"))
        self.reservedRBtn.setText(_translate("MainWindow", "调试按钮（右）"))
