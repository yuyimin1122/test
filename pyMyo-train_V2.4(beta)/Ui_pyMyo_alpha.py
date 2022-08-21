# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyMyo_alpha.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1360, 707)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/DYX/.designer/backup/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.GroupEMG = QtWidgets.QGroupBox(Form)
        self.GroupEMG.setGeometry(QtCore.QRect(10, 10, 1321, 521))
        self.GroupEMG.setTitle("")
        self.GroupEMG.setObjectName("GroupEMG")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.GroupEMG)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1301, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.graph_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.graph_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.graph_layout.setContentsMargins(0, 0, 0, 0)
        self.graph_layout.setObjectName("graph_layout")
        self.funcArea = QtWidgets.QGroupBox(Form)
        self.funcArea.setGeometry(QtCore.QRect(10, 540, 260, 71))
        self.funcArea.setTitle("")
        self.funcArea.setObjectName("funcArea")
        self.layoutWidget = QtWidgets.QWidget(self.funcArea)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 221, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.setBATTERY = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.setBATTERY.setFont(font)
        self.setBATTERY.setText("")
        self.setBATTERY.setObjectName("setBATTERY")
        self.gridLayout.addWidget(self.setBATTERY, 0, 1, 1, 1)
        self.Battery = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Battery.setFont(font)
        self.Battery.setObjectName("Battery")
        self.gridLayout.addWidget(self.Battery, 0, 0, 1, 1)
        self.btnGroup = QtWidgets.QGroupBox(Form)
        self.btnGroup.setGeometry(QtCore.QRect(290, 540, 771, 161))
        self.btnGroup.setTitle("")
        self.btnGroup.setObjectName("btnGroup")
        self.connectBtn = QtWidgets.QPushButton(self.btnGroup)
        self.connectBtn.setGeometry(QtCore.QRect(10, 10, 100, 51))
        self.connectBtn.setObjectName("connectBtn")
        self.disConnectBtn = QtWidgets.QPushButton(self.btnGroup)
        self.disConnectBtn.setGeometry(QtCore.QRect(10, 90, 100, 51))
        self.disConnectBtn.setObjectName("disConnectBtn")
        self.startBtn = QtWidgets.QPushButton(self.btnGroup)
        self.startBtn.setGeometry(QtCore.QRect(140, 10, 100, 51))
        self.startBtn.setObjectName("startBtn")
        self.pose1Btn = QtWidgets.QPushButton(self.btnGroup)
        self.pose1Btn.setGeometry(QtCore.QRect(270, 10, 100, 51))
        self.pose1Btn.setObjectName("pose1Btn")
        self.pose2Btn = QtWidgets.QPushButton(self.btnGroup)
        self.pose2Btn.setGeometry(QtCore.QRect(270, 90, 100, 51))
        self.pose2Btn.setObjectName("pose2Btn")
        self.pose3Btn = QtWidgets.QPushButton(self.btnGroup)
        self.pose3Btn.setGeometry(QtCore.QRect(400, 10, 100, 51))
        self.pose3Btn.setObjectName("pose3Btn")
        self.pose4Btn = QtWidgets.QPushButton(self.btnGroup)
        self.pose4Btn.setGeometry(QtCore.QRect(400, 90, 100, 51))
        self.pose4Btn.setObjectName("pose4Btn")
        self.calculateBtn = QtWidgets.QPushButton(self.btnGroup)
        self.calculateBtn.setGeometry(QtCore.QRect(660, 90, 100, 51))
        self.calculateBtn.setObjectName("calculateBtn")
        self.freeBtn = QtWidgets.QPushButton(self.btnGroup)
        self.freeBtn.setGeometry(QtCore.QRect(140, 90, 100, 51))
        self.freeBtn.setObjectName("freeBtn")
        self.maxBtn = QtWidgets.QPushButton(self.btnGroup)
        self.maxBtn.setGeometry(QtCore.QRect(530, 10, 100, 51))
        self.maxBtn.setObjectName("maxBtn")
        self.minBtn = QtWidgets.QPushButton(self.btnGroup)
        self.minBtn.setGeometry(QtCore.QRect(530, 90, 100, 51))
        self.minBtn.setObjectName("minBtn")
        self.msgGroup = QtWidgets.QGroupBox(Form)
        self.msgGroup.setGeometry(QtCore.QRect(1070, 540, 261, 161))
        self.msgGroup.setTitle("")
        self.msgGroup.setObjectName("msgGroup")
        self.msgBrowser = QtWidgets.QTextBrowser(self.msgGroup)
        self.msgBrowser.setGeometry(QtCore.QRect(10, 10, 241, 141))
        self.msgBrowser.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.msgBrowser.setObjectName("msgBrowser")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 620, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 131, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.subjectnum = QtWidgets.QLineEdit(self.groupBox)
        self.subjectnum.setGeometry(QtCore.QRect(160, 20, 91, 31))
        self.subjectnum.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.subjectnum.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.subjectnum.setAlignment(QtCore.Qt.AlignCenter)
        self.subjectnum.setObjectName("subjectnum")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.connectBtn, self.disConnectBtn)
        Form.setTabOrder(self.disConnectBtn, self.startBtn)
        Form.setTabOrder(self.startBtn, self.msgBrowser)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "pyMyo-train"))
        self.Battery.setText(_translate("Form", "BATTERY:"))
        self.connectBtn.setText(_translate("Form", "Connect"))
        self.disConnectBtn.setText(_translate("Form", "Disconnect"))
        self.startBtn.setText(_translate("Form", "Start"))
        self.pose1Btn.setText(_translate("Form", "Pose1"))
        self.pose2Btn.setText(_translate("Form", "Pose2"))
        self.pose3Btn.setText(_translate("Form", "Pose3"))
        self.pose4Btn.setText(_translate("Form", "Pose4"))
        self.calculateBtn.setText(_translate("Form", "Calculate"))
        self.freeBtn.setText(_translate("Form", "Free"))
        self.maxBtn.setText(_translate("Form", "Maximum"))
        self.minBtn.setText(_translate("Form", "Minimum"))
        self.groupBox.setTitle(_translate("Form", "Set subject number"))
        self.label.setText(_translate("Form", "Subject Number :"))
