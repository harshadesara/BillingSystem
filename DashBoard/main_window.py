# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'main_window.ui'
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1750, 850)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1750, 850))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("color:rgb(255,255,255);\n"
"font: 75 15pt \"MS Shell Dlg 2\";\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(20, 90, 1701, 601))
        self.tableWidget.setStyleSheet("color: rgb(223, 49, 104);")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(18)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, item)

        self._datamodel=QtGui.QStandardItemModel(0,2)
        qindex=self._datamodel.index(1,1,QtCore.QModelIndex())

        button=QtWidgets.QPushButton(ui.tableWidget)
        #ui.tableWidget.setIndexWidget(qindex,button)
        #self.tableWidget.setCellWidget(1,0,combobox)
        #self.tableWidget.setCellWidget(5,0,button)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1750, 46))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("background-color: rgb(33, 103, 120);\n"
"padding:5px 30px;")
        self.menubar.setObjectName("menubar")
        self.menu_New = QtWidgets.QMenu(self.menubar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_New.sizePolicy().hasHeightForWidth())
        self.menu_New.setSizePolicy(sizePolicy)
        self.menu_New.setBaseSize(QtCore.QSize(200, 0))
        self.menu_New.setStyleSheet("font: 22pt \"MS Sans Serif\";")
        self.menu_New.setObjectName("menu_New")
        self.menuCustomers = QtWidgets.QMenu(self.menubar)
        self.menuCustomers.setStyleSheet("margin:100px 40px;")
        self.menuCustomers.setObjectName("menuCustomers")
        self.menuCompany_Details = QtWidgets.QMenu(self.menubar)
        self.menuCompany_Details.setStyleSheet("padding:5px 200px;")
        self.menuCompany_Details.setObjectName("menuCompany_Details")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setStyleSheet("padding:5px 20px;")
        self.menuSettings.setObjectName("menuSettings")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setStyleSheet("padding:5px 20px;")
        self.menuTools.setObjectName("menuTools")
        self.menuHelps = QtWidgets.QMenu(self.menubar)
        self.menuHelps.setStyleSheet("padding:5px 20px;")
        self.menuHelps.setObjectName("menuHelps")
        self.menuProduct_Services = QtWidgets.QMenu(self.menubar)
        self.menuProduct_Services.setObjectName("menuProduct_Services")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_New_Company = QtWidgets.QAction(MainWindow)
        self.actionAdd_New_Company.setObjectName("actionAdd_New_Company")
        self.actionManage_Company = QtWidgets.QAction(MainWindow)
        self.actionManage_Company.setObjectName("actionManage_Company")
        self.actionAdd_New_Customer = QtWidgets.QAction(MainWindow)
        self.actionAdd_New_Customer.setObjectName("actionAdd_New_Customer")
        self.actionAdd_Product_Services = QtWidgets.QAction(MainWindow)
        self.actionAdd_Product_Services.setObjectName("actionAdd_Product_Services")
        self.actionManage_Product_Services = QtWidgets.QAction(MainWindow)
        self.actionManage_Product_Services.setObjectName("actionManage_Product_Services")
        self.menuCustomers.addAction(self.actionAdd_New_Customer)
        self.menuCompany_Details.addSeparator()
        self.menuCompany_Details.addAction(self.actionAdd_New_Company)
        self.menuCompany_Details.addAction(self.actionManage_Company)
        self.menuProduct_Services.addAction(self.actionAdd_Product_Services)
        self.menuProduct_Services.addAction(self.actionManage_Product_Services)
        self.menubar.addAction(self.menu_New.menuAction())
        self.menubar.addAction(self.menuCustomers.menuAction())
        self.menubar.addAction(self.menuCompany_Details.menuAction())
        self.menubar.addAction(self.menuProduct_Services.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelps.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AliveCreate Bill Software"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product_ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product_Type"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Product_Category"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Product_SKU"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Product_Name"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Product_Description"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Product_HSN"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Product_SAC"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Product_Unit_Price"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Product_Tax"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Product_Quantity"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Product_Purchase_Price"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Product_Image_Name"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Product_Created_At"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Product_Updated_At"))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Product_Deleted_At"))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "Product_Status"))
        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "Update"))
        self.menu_New.setTitle(_translate("MainWindow", "New"))
        self.menuCustomers.setTitle(_translate("MainWindow", "Customers"))
        self.menuCompany_Details.setTitle(_translate("MainWindow", "Company Details"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuHelps.setTitle(_translate("MainWindow", "Help"))
        self.menuProduct_Services.setTitle(_translate("MainWindow", "Product/Services"))
        self.actionAdd_New_Company.setText(_translate("MainWindow", "Add New Company"))
        self.actionManage_Company.setText(_translate("MainWindow", "Manage Company"))
        self.actionAdd_New_Customer.setText(_translate("MainWindow", "Add New Customer"))
        self.actionAdd_Product_Services.setText(_translate("MainWindow", "Add Product/Services"))
        self.actionManage_Product_Services.setText(_translate("MainWindow", "Manage Product/Services"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

