# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_new_company.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import converter
import qframe

class MyQtApp(converter.Ui_MainWindow,QtWidgets.QMainWindow):
        def __init__(self):
                super(MyQtApp, self).__init__()
                self.setupUi(self)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 965)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 780))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 1200))
        MainWindow.setStyleSheet("background-color: rgb(231, 231, 231);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(390, 720, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(33, 103, 120);\n"
"color:white;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/sample/Images/save64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(30, 17, 492, 691))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.formLayoutWidget_2.setFont(font)
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.frame = QtWidgets.QFrame(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.frame.setFont(font)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(389, 34))
        self.label.setMaximumSize(QtCore.QSize(389, 34))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 15, -1, 15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setMinimumSize(QtCore.QSize(11, 30))
        self.label_22.setMaximumSize(QtCore.QSize(11, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color:red;")
        self.label_22.setObjectName("label_22")
        self.horizontalLayout.addWidget(self.label_22)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMinimumSize(QtCore.QSize(180, 22))
        self.label_2.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.lineEdit.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius:3px;\n"
"border:1px solid gray;\n"
"background-color:white;\n"
"color:gray;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setMinimumSize(QtCore.QSize(11, 30))
        self.label_23.setMaximumSize(QtCore.QSize(11, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color:red;")
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_2.addWidget(self.label_23)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setMinimumSize(QtCore.QSize(180, 22))
        self.label_3.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("border-radius:3px;\n"
"border:1px solid gray;\n"
"background-color:white;\n"
"color:gray;\n"
"")
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_24 = QtWidgets.QLabel(self.frame)
        self.label_24.setMinimumSize(QtCore.QSize(11, 30))
        self.label_24.setMaximumSize(QtCore.QSize(11, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color:red;")
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_16.addWidget(self.label_24)
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setMinimumSize(QtCore.QSize(180, 22))
        self.label_21.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_16.addWidget(self.label_21)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit_8.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("border-radius:3px;\n"
"border:1px solid gray;\n"
"background-color:white;\n"
"color:gray;\n"
"")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_16.addWidget(self.lineEdit_8)
        self.verticalLayout.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_25 = QtWidgets.QLabel(self.frame)
        self.label_25.setMinimumSize(QtCore.QSize(11, 30))
        self.label_25.setMaximumSize(QtCore.QSize(11, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color:red;")
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_3.addWidget(self.label_25)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setMinimumSize(QtCore.QSize(180, 22))
        self.label_4.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("border-radius:3px;\n"
"border:1px solid gray;\n"
"background-color:white;\n"
"color:gray;\n"
"")
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setMinimumContentsLength(11)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_26 = QtWidgets.QLabel(self.frame)
        self.label_26.setMinimumSize(QtCore.QSize(11, 30))
        self.label_26.setMaximumSize(QtCore.QSize(11, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color:red;")
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_4.addWidget(self.label_26)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setMinimumSize(QtCore.QSize(180, 22))
        self.label_5.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setStyleSheet("border-radius:3px;\n"
"border:1px solid gray;\n"
"background-color:white;\n"
"color:gray;\n"
"")
        self.comboBox_3.setEditable(True)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setMinimumSize(QtCore.QSize(11, 30))
        self.label_27.setMaximumSize(QtCore.QSize(11, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color:red;")
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_6.addWidget(self.label_27)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setMinimumSize(QtCore.QSize(180, 22))
        self.label_8.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border-radius:3px;\n"
"border:1px solid gray;\n"
"background-color:white;\n"
"color:gray;\n"
"")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_6.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_29 = QtWidgets.QLabel(self.frame)
        self.label_29.setEnabled(True)
        self.label_29.setMinimumSize(QtCore.QSize(11, 30))
        self.label_29.setMaximumSize(QtCore.QSize(11, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color:red;")
        self.label_29.setText("")
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_8.addWidget(self.label_29)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setMinimumSize(QtCore.QSize(180, 88))
        self.label_6.setMaximumSize(QtCore.QSize(180, 88))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setMinimumSize(QtCore.QSize(200, 88))
        self.textEdit.setMaximumSize(QtCore.QSize(250, 88))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("border-radius:3px;\n"
"border:1px solid gray;\n"
"background-color:white;\n"
"color:gray;")
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_8.addWidget(self.textEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setEnabled(True)
        self.label_30.setMinimumSize(QtCore.QSize(11, 30))
        self.label_30.setMaximumSize(QtCore.QSize(11, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color:red;")
        self.label_30.setText("")
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_5.addWidget(self.label_30)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setMinimumSize(QtCore.QSize(180, 22))
        self.label_7.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-radius:3px;\n"
"border:1px solid gray;\n"
"background-color:white;\n"
"color:gray;\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_5.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_28 = QtWidgets.QLabel(self.frame)
        self.label_28.setEnabled(True)
        self.label_28.setMinimumSize(QtCore.QSize(11, 30))
        self.label_28.setMaximumSize(QtCore.QSize(11, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color:red;")
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_7.addWidget(self.label_28)
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setMinimumSize(QtCore.QSize(180, 22))
        self.label_9.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border-radius:3px;\n"
"border:1px solid gray;\n"
"background-color:white;\n"
"color:gray;\n"
"")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_7.addWidget(self.lineEdit_4)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frame)
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(530, 20, 411, 681))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_4.setContentsMargins(0, 0, 0, 10)
        self.formLayout_4.setVerticalSpacing(10)
        self.formLayout_4.setObjectName("formLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.formLayoutWidget_3)
        self.frame_2.setStyleSheet("background-color: whitesmoke;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setMinimumSize(QtCore.QSize(359, 34))
        self.label_10.setMaximumSize(QtCore.QSize(359, 34))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, 15, -1, 15)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setMinimumSize(QtCore.QSize(150, 33))
        self.label_11.setMaximumSize(QtCore.QSize(150, 33))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.comboBox_4 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_4.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox_4.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setStyleSheet("border-radius:3px;\n"
"border:1px solid gray;\n"
"background-color:white;\n"
"color:gray;")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout_9.addWidget(self.comboBox_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setMinimumSize(QtCore.QSize(150, 33))
        self.label_12.setMaximumSize(QtCore.QSize(150, 33))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_10.addWidget(self.label_12)
        self.comboBox_5 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_5.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox_5.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setStyleSheet("border-radius:3px;\n"
"border:1px solid gray;\n"
"background-color:white;\n"
"color:gray;")
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.horizontalLayout_10.addWidget(self.comboBox_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setMinimumSize(QtCore.QSize(150, 33))
        self.label_13.setMaximumSize(QtCore.QSize(150, 33))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_11.addWidget(self.label_13)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(200, 30))
        self.lineEdit_5.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("border-radius:3px;\n"
"border:1px solid gray;\n"
"background-color:white;\n"
"color:gray;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_11.addWidget(self.lineEdit_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setMinimumSize(QtCore.QSize(150, 33))
        self.label_14.setMaximumSize(QtCore.QSize(150, 33))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_12.addWidget(self.label_14)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(200, 30))
        self.lineEdit_6.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("border-radius:3px;\n"
"border:1px solid gray;\n"
"background-color:white;\n"
"color:gray;")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_12.addWidget(self.lineEdit_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_20 = QtWidgets.QLabel(self.frame_2)
        self.label_20.setMinimumSize(QtCore.QSize(150, 33))
        self.label_20.setMaximumSize(QtCore.QSize(150, 33))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_15.addWidget(self.label_20)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(200, 30))
        self.lineEdit_7.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("border-radius:3px;\n"
"border:1px solid gray;\n"
"background-color:white;\n"
"color:gray;")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_15.addWidget(self.lineEdit_7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        self.label_15 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_4.addWidget(self.label_15)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setContentsMargins(-1, 15, -1, 15)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_16 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMinimumSize(QtCore.QSize(130, 25))
        self.label_16.setMaximumSize(QtCore.QSize(130, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_2.addWidget(self.label_16)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setMinimumSize(QtCore.QSize(130, 28))
        self.pushButton.setMaximumSize(QtCore.QSize(130, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(33, 103, 120);\n"
"color:white;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/sample/Images/gallery64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(130, 28))
        self.pushButton_2.setMaximumSize(QtCore.QSize(130, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(33, 103, 120);\n"
"color:white;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/sample/Images/delete264.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.horizontalLayout_13.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(85, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem)
        self.label_18 = QtWidgets.QLabel(self.frame_2)
        self.label_18.setMinimumSize(QtCore.QSize(100, 100))
        self.label_18.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("border:1px solid black;")
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap(":/sample/icon.png"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_13.addWidget(self.label_18)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_17 = QtWidgets.QLabel(self.frame_2)
        self.label_17.setMinimumSize(QtCore.QSize(130, 28))
        self.label_17.setMaximumSize(QtCore.QSize(130, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_3.addWidget(self.label_17)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setMinimumSize(QtCore.QSize(130, 28))
        self.pushButton_3.setMaximumSize(QtCore.QSize(130, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(33, 103, 120);\n"
"color:white;")
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setMinimumSize(QtCore.QSize(130, 28))
        self.pushButton_4.setMaximumSize(QtCore.QSize(130, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(33, 103, 120);\n"
"color:white;")
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.horizontalLayout_14.addLayout(self.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(85, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem2)
        self.label_19 = QtWidgets.QLabel(self.frame_2)
        self.label_19.setMinimumSize(QtCore.QSize(100, 100))
        self.label_19.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("border:1px solid black;")
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap(":/sample/hba.jpg"))
        self.label_19.setScaledContents(True)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_14.addWidget(self.label_19)
        self.verticalLayout_4.addLayout(self.horizontalLayout_14)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.frame_2)
        self.label_new = QtWidgets.QLabel(self.centralwidget)
        self.label_new.setGeometry(QtCore.QRect(700, 800, 151, 71))
        self.label_new.setText("")
        self.label_new.setObjectName("label_new")
        self.show = QtWidgets.QFrame(self.centralwidget)
        self.show.setGeometry(QtCore.QRect(10, 770, 351, 141))
        self.show.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.show.setFrameShadow(QtWidgets.QFrame.Raised)
        self.show.setObjectName("show")
        #
        self.test = QtWidgets.QFrame(self.show)
        self.test.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.test.setGeometry(QtCore.QRect(160, 50, 120, 80))
        self.test.setFrameShadow(QtWidgets.QFrame.Raised)
        self.test.setObjectName("test")


        self.inner = QtWidgets.QFrame(self.show)
        self.inner.setGeometry(QtCore.QRect(160, 50, 120, 80))
        self.inner.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inner.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inner.setObjectName("inner")

        qframe.setupUi = QtWidgets.QFrame(self.inner)
        qframe.Ui_Frame.setupUi(self,self.inner)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add New Company"))
        self.pushButton_5.setText(_translate("MainWindow", "Save Company"))
        self.label.setText(_translate("MainWindow", "Company Details"))
        self.label_22.setText(_translate("MainWindow", "*"))
        self.label_2.setText(_translate("MainWindow", "Company Name :"))
        self.label_23.setText(_translate("MainWindow", "*"))
        self.label_3.setText(_translate("MainWindow", "Service Category :"))
        self.label_24.setText(_translate("MainWindow", "*"))
        self.label_21.setText(_translate("MainWindow", "Contact No :"))
        self.label_25.setText(_translate("MainWindow", "*"))
        self.label_4.setText(_translate("MainWindow", "City :"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Vadodara"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Ahmedabad"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Surat"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Rajkot"))
        self.label_26.setText(_translate("MainWindow", "*"))
        self.label_5.setText(_translate("MainWindow", "State :"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Gujarat"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Maharashtra"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Rajasthan"))
        self.label_27.setText(_translate("MainWindow", "*"))
        self.label_8.setText(_translate("MainWindow", "Email :"))
        self.label_6.setText(_translate("MainWindow", "Address :"))
        self.label_7.setText(_translate("MainWindow", "Pincode :"))
        self.label_9.setText(_translate("MainWindow", "Website :"))
        self.label_10.setText(_translate("MainWindow", "Tax Details"))
        self.label_11.setText(_translate("MainWindow", "Tax Type : "))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "2"))
        self.label_12.setText(_translate("MainWindow", "Tax Inclusive :"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Yes"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "No"))
        self.label_13.setText(_translate("MainWindow", "Tin No :"))
        self.label_14.setText(_translate("MainWindow", "Pan No :"))
        self.label_20.setText(_translate("MainWindow", "GST No :"))
        self.label_15.setText(_translate("MainWindow", "Company Identity"))
        self.label_16.setText(_translate("MainWindow", "Logo"))
        self.pushButton.setText(_translate("MainWindow", "Select"))
        self.pushButton_2.setText(_translate("MainWindow", "Remove"))
        self.label_17.setText(_translate("MainWindow", "Signature"))
        self.pushButton_3.setText(_translate("MainWindow", "Select"))
        self.pushButton_4.setText(_translate("MainWindow", "Remove"))

#import add_new_comp_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    qt_app = MyQtApp()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

