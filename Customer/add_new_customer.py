# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_new_customer.ui',
# licensing of 'add_new_customer.ui' applies.
#
# Created: Fri Jul 26 16:06:18 2019
#      by: pyside2-uic  running on PySide2 5.12.4
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 780)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 780))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 780))
        MainWindow.setStyleSheet("background-color: rgb(231, 231, 231);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(400, 690, 250, 40))
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
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(538, 40, 483, 611))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.formLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 10)
        self.gridLayout_3.setVerticalSpacing(10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.formLayoutWidget_3)
        self.frame_2.setStyleSheet("background-color: whitesmoke;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_25 = QtWidgets.QLabel(self.frame_2)
        self.label_25.setMinimumSize(QtCore.QSize(11, 30))
        self.label_25.setMaximumSize(QtCore.QSize(11, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color:red;")
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_3.addWidget(self.label_25)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setMinimumSize(QtCore.QSize(150, 33))
        self.label_4.setMaximumSize(QtCore.QSize(150, 33))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_2.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox_2.setMaximumSize(QtCore.QSize(200, 30))
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
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_26 = QtWidgets.QLabel(self.frame_2)
        self.label_26.setMinimumSize(QtCore.QSize(11, 30))
        self.label_26.setMaximumSize(QtCore.QSize(11, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color:red;")
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_4.addWidget(self.label_26)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setMinimumSize(QtCore.QSize(150, 33))
        self.label_5.setMaximumSize(QtCore.QSize(150, 33))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_3.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox_3.setMaximumSize(QtCore.QSize(200, 30))
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
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_30 = QtWidgets.QLabel(self.frame_2)
        self.label_30.setEnabled(True)
        self.label_30.setMinimumSize(QtCore.QSize(11, 30))
        self.label_30.setMaximumSize(QtCore.QSize(11, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color:red;")
        self.label_30.setText("")
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_21.addWidget(self.label_30)
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setMinimumSize(QtCore.QSize(150, 33))
        self.label_7.setMaximumSize(QtCore.QSize(150, 33))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_21.addWidget(self.label_7)
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_2.setMinimumSize(QtCore.QSize(200, 30))
        self.textEdit_2.setMaximumSize(QtCore.QSize(200, 88))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("border-radius:3px;\n"
"border:1px solid gray;\n"
"background-color:white;\n"
"color:gray;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_21.addWidget(self.textEdit_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_36 = QtWidgets.QLabel(self.frame_2)
        self.label_36.setEnabled(True)
        self.label_36.setMinimumSize(QtCore.QSize(11, 30))
        self.label_36.setMaximumSize(QtCore.QSize(11, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("color:red;")
        self.label_36.setText("")
        self.label_36.setObjectName("label_36")
        self.horizontalLayout_5.addWidget(self.label_36)
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setMinimumSize(QtCore.QSize(150, 33))
        self.label_9.setMaximumSize(QtCore.QSize(150, 33))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(200, 30))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(200, 30))
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
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_37 = QtWidgets.QLabel(self.frame_2)
        self.label_37.setEnabled(True)
        self.label_37.setMinimumSize(QtCore.QSize(11, 30))
        self.label_37.setMaximumSize(QtCore.QSize(11, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("color:red;")
        self.label_37.setText("")
        self.label_37.setObjectName("label_37")
        self.horizontalLayout_15.addWidget(self.label_37)
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
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_38 = QtWidgets.QLabel(self.frame_2)
        self.label_38.setEnabled(True)
        self.label_38.setMinimumSize(QtCore.QSize(11, 30))
        self.label_38.setMaximumSize(QtCore.QSize(11, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("color:red;")
        self.label_38.setText("")
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_22.addWidget(self.label_38)
        self.label_28 = QtWidgets.QLabel(self.frame_2)
        self.label_28.setMinimumSize(QtCore.QSize(150, 33))
        self.label_28.setMaximumSize(QtCore.QSize(150, 33))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_22.addWidget(self.label_28)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_11.setMinimumSize(QtCore.QSize(200, 30))
        self.lineEdit_11.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setStyleSheet("border-radius:3px;\n"
"border:1px solid gray;\n"
"background-color:white;\n"
"color:gray;")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_22.addWidget(self.lineEdit_11)
        self.verticalLayout_4.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_39 = QtWidgets.QLabel(self.frame_2)
        self.label_39.setEnabled(True)
        self.label_39.setMinimumSize(QtCore.QSize(11, 30))
        self.label_39.setMaximumSize(QtCore.QSize(11, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("color:red;")
        self.label_39.setText("")
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_12.addWidget(self.label_39)
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
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_41 = QtWidgets.QLabel(self.frame_2)
        self.label_41.setEnabled(True)
        self.label_41.setMinimumSize(QtCore.QSize(11, 30))
        self.label_41.setMaximumSize(QtCore.QSize(11, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("color:red;")
        self.label_41.setText("")
        self.label_41.setObjectName("label_41")
        self.horizontalLayout_9.addWidget(self.label_41)
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setMinimumSize(QtCore.QSize(150, 33))
        self.label_10.setMaximumSize(QtCore.QSize(150, 33))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.textEdit_3 = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_3.setMinimumSize(QtCore.QSize(200, 88))
        self.textEdit_3.setMaximumSize(QtCore.QSize(200, 88))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setStyleSheet("border-radius:3px;\n"
"border:1px solid gray;\n"
"background-color:white;\n"
"color:gray;")
        self.textEdit_3.setObjectName("textEdit_3")
        self.horizontalLayout_9.addWidget(self.textEdit_3)
        self.gridLayout_2.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(31, -9, 483, 677))
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
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setContentsMargins(-1, 15, -1, 15)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.verticalLayout.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_32 = QtWidgets.QLabel(self.frame)
        self.label_32.setMinimumSize(QtCore.QSize(140, 140))
        self.label_32.setMaximumSize(QtCore.QSize(140, 140))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("border:1px solid black;")
        self.label_32.setText("")
        self.label_32.setPixmap(QtGui.QPixmap(":/sample/hba.jpg"))
        self.label_32.setScaledContents(True)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_18.addWidget(self.label_32)
        spacerItem = QtWidgets.QSpacerItem(63, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem1)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setMinimumSize(QtCore.QSize(130, 28))
        self.pushButton_6.setMaximumSize(QtCore.QSize(130, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(33, 103, 120);\n"
"color:white;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/sample/Images/gallery64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_5.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setMinimumSize(QtCore.QSize(130, 28))
        self.pushButton_7.setMaximumSize(QtCore.QSize(130, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(33, 103, 120);\n"
"color:white;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/sample/Images/delete264.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon2)
        self.pushButton_7.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_5.addWidget(self.pushButton_7)
        self.horizontalLayout_18.addLayout(self.verticalLayout_5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_35 = QtWidgets.QLabel(self.frame)
        self.label_35.setMinimumSize(QtCore.QSize(11, 30))
        self.label_35.setMaximumSize(QtCore.QSize(11, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("color:red;")
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_23.addWidget(self.label_35)
        self.label_40 = QtWidgets.QLabel(self.frame)
        self.label_40.setMinimumSize(QtCore.QSize(180, 22))
        self.label_40.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.horizontalLayout_23.addWidget(self.label_40)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy)
        self.lineEdit_12.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit_12.setMaximumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setStyleSheet("border-radius:3px;\n"
"border:1px solid gray;\n"
"background-color:white;\n"
"color:gray;\n"
"")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.horizontalLayout_23.addWidget(self.lineEdit_12)
        self.verticalLayout.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_24 = QtWidgets.QLabel(self.frame)
        self.label_24.setMinimumSize(QtCore.QSize(11, 30))
        self.label_24.setMaximumSize(QtCore.QSize(11, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit_8.setMaximumSize(QtCore.QSize(250, 30))
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
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_31 = QtWidgets.QLabel(self.frame)
        self.label_31.setMinimumSize(QtCore.QSize(11, 30))
        self.label_31.setMaximumSize(QtCore.QSize(11, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color:red;")
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_19.addWidget(self.label_31)
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setMinimumSize(QtCore.QSize(180, 22))
        self.label_23.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_19.addWidget(self.label_23)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit_9.setMaximumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setStyleSheet("border-radius:3px;\n"
"border:1px solid gray;\n"
"background-color:white;\n"
"color:gray;\n"
"")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_19.addWidget(self.lineEdit_9)
        self.verticalLayout.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_33 = QtWidgets.QLabel(self.frame)
        self.label_33.setMinimumSize(QtCore.QSize(11, 30))
        self.label_33.setMaximumSize(QtCore.QSize(11, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color:red;")
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_20.addWidget(self.label_33)
        self.label_34 = QtWidgets.QLabel(self.frame)
        self.label_34.setMinimumSize(QtCore.QSize(180, 22))
        self.label_34.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_20.addWidget(self.label_34)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy)
        self.lineEdit_10.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit_10.setMaximumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setStyleSheet("border-radius:3px;\n"
"border:1px solid gray;\n"
"background-color:white;\n"
"color:gray;\n"
"")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_20.addWidget(self.lineEdit_10)
        self.verticalLayout.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setMinimumSize(QtCore.QSize(11, 30))
        self.label_27.setMaximumSize(QtCore.QSize(11, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color:red;")
        self.label_27.setText("")
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(250, 30))
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
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
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
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Add New Customer", None, -1))
        self.pushButton_5.setText(QtWidgets.QApplication.translate("MainWindow", "Save Customer", None, -1))
        self.label_25.setText(QtWidgets.QApplication.translate("MainWindow", "*", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "City :", None, -1))
        self.comboBox_2.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Vadodara", None, -1))
        self.comboBox_2.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Ahmedabad", None, -1))
        self.comboBox_2.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "Surat", None, -1))
        self.comboBox_2.setItemText(3, QtWidgets.QApplication.translate("MainWindow", "Rajkot", None, -1))
        self.label_26.setText(QtWidgets.QApplication.translate("MainWindow", "*", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "State :", None, -1))
        self.comboBox_3.setItemText(4, QtWidgets.QApplication.translate("MainWindow", "Gujarat", None, -1))
        self.comboBox_3.setItemText(5, QtWidgets.QApplication.translate("MainWindow", "Maharashtra", None, -1))
        self.comboBox_3.setItemText(6, QtWidgets.QApplication.translate("MainWindow", "Rajasthan", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("MainWindow", "Address :", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("MainWindow", "Pincode :", None, -1))
        self.label_20.setText(QtWidgets.QApplication.translate("MainWindow", "GST No :", None, -1))
        self.label_28.setText(QtWidgets.QApplication.translate("MainWindow", "Tin No :", None, -1))
        self.label_14.setText(QtWidgets.QApplication.translate("MainWindow", "Pan No :", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("MainWindow", "IMP Note :", None, -1))
        self.pushButton_6.setText(QtWidgets.QApplication.translate("MainWindow", "Select", None, -1))
        self.pushButton_7.setText(QtWidgets.QApplication.translate("MainWindow", "Remove", None, -1))
        self.label_35.setText(QtWidgets.QApplication.translate("MainWindow", "*", None, -1))
        self.label_40.setText(QtWidgets.QApplication.translate("MainWindow", "Contact Name :", None, -1))
        self.label_24.setText(QtWidgets.QApplication.translate("MainWindow", "*", None, -1))
        self.label_21.setText(QtWidgets.QApplication.translate("MainWindow", "Contact Person :", None, -1))
        self.label_31.setText(QtWidgets.QApplication.translate("MainWindow", "*", None, -1))
        self.label_23.setText(QtWidgets.QApplication.translate("MainWindow", "Contact No :", None, -1))
        self.label_33.setText(QtWidgets.QApplication.translate("MainWindow", "*", None, -1))
        self.label_34.setText(QtWidgets.QApplication.translate("MainWindow", "Email :", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("MainWindow", "Website :", None, -1))

#import add_new_comp_rc
