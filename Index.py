from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
from PostgresHelper import *
import shutil
from datetime import datetime
import time
import os
import subprocess
from functools import partial
from styles import *
#from PostgresHelper import *
#from dialog import Ui_Dialog
#from dialog_exit import Ui_Dialog
#import subprocess



app=QtWidgets.QApplication([])
dlg=uic.loadUi("DashBoard/main_window.ui")
dlg2=uic.loadUi("Company/add_new_company.ui")
dlg3=uic.loadUi("Customer/add_new_customer.ui")
dlg4=uic.loadUi("Product_Services/add_new_product_services.ui")
dlg5=uic.loadUi("Update_Product_Services/update_product_services.ui")
dlg6=uic.loadUi("Dialogs/delete_dialog.ui")
dlg7=uic.loadUi("Update_Company/update_company.ui")
dlg8=uic.loadUi("Update_Customer/update_customer.ui")
dlg9=uic.loadUi("Add_Invoice/add_invoice.ui")
dlg10=uic.loadUi("Update_Invoice/update_invoice.ui")
pixmap=QPixmap("profile.png")
deleteimage=QPixmap("Images/delete64.png")
#pixmap2=QPixmap("icon.png")

gallery = QPixmap('Images/gallery64.png')
gallerys = QIcon(gallery)

remove=QPixmap('Images/delete264.png')
removes=QIcon(remove)

save=QPixmap('Images/save64.png')
saves=QIcon(save)

edit=QPixmap('Images/edit264.png')
edits=QIcon(edit)
#dlg.tableWidget.setColumnWidth(0,20)
dlg9.table_tw.setColumnWidth(0,130)
dlg9.table_tw.setColumnWidth(1,120)
dlg9.table_tw.setColumnWidth(2,163)
dlg9.table_tw.setColumnWidth(3,120)
dlg9.table_tw.setColumnWidth(4,80)
dlg9.table_tw.setColumnWidth(5,80)
dlg9.table_tw.setColumnWidth(6,80)
dlg9.table_tw.setColumnWidth(7,80)
dlg9.table_tw.setColumnWidth(8,80)
dlg9.table_tw.setColumnWidth(9,80)
dlg9.table_tw.setColumnWidth(10,80)
dlg9.table_tw.setColumnWidth(11,80)
dlg9.table_tw.setColumnWidth(12,80)
dlg9.table_tw.setColumnWidth(13,80)



dlg2.pushButton_2.setProperty('class', 'test')
dlg2.pushButton_3.setProperty('class', 'test')
dlg2.pushButton_2.setStyleSheet(stylesheet)
dlg2.pushButton_3.setStyleSheet(stylesheet)
dlg2.pushButton.setStyleSheet(stylesheet)
dlg2.lineEdit.setStyleSheet(stylesheet)

dlg2.pushButton.setIcon(gallerys)
dlg2.pushButton.setIconSize(QSize(25,25))
dlg2.pushButton_3.setIcon(gallerys)
dlg2.pushButton_3.setIconSize(QSize(25,25))
dlg2.pushButton_2.setIcon(removes)
dlg2.pushButton_2.setIconSize(QSize(25,25))
dlg2.pushButton_4.setIcon(removes)
dlg2.pushButton_4.setIconSize(QSize(25,25))
dlg2.pushButton_5.setIcon(saves)
dlg2.pushButton_5.setIconSize(QSize(25,25))

dlg3.pushButton_6.setIcon(gallerys)
dlg3.pushButton_6.setIconSize(QSize(25,25))
dlg3.pushButton_7.setIcon(removes)
dlg3.pushButton_7.setIconSize(QSize(25,25))
dlg3.pushButton_5.setIcon(saves)
dlg3.pushButton_5.setIconSize(QSize(25,25))

dlg4.pushButton_6.setIcon(gallerys)
dlg4.pushButton_6.setIconSize(QSize(25,25))
dlg4.pushButton_7.setIcon(removes)
dlg4.pushButton_7.setIconSize(QSize(25,25))
dlg4.pushButton_5.setIcon(saves)
dlg4.pushButton_5.setIconSize(QSize(25,25))

dlg5.pushButton_6.setIcon(gallerys)
dlg5.pushButton_6.setIconSize(QSize(25,25))
dlg5.pushButton_7.setIcon(removes)
dlg5.pushButton_7.setIconSize(QSize(25,25))
dlg5.pushButton_5.setIcon(edits)
dlg5.pushButton_5.setIconSize(QSize(25,25))

dlg7.pushButton.setIcon(gallerys)
dlg7.pushButton.setIconSize(QSize(25,25))
dlg7.pushButton_3.setIcon(gallerys)
dlg7.pushButton_3.setIconSize(QSize(25,25))
dlg7.pushButton_2.setIcon(removes)
dlg7.pushButton_2.setIconSize(QSize(25,25))
dlg7.pushButton_4.setIcon(removes)
dlg7.pushButton_4.setIconSize(QSize(25,25))
dlg7.pushButton_5.setIcon(edits)
dlg7.pushButton_5.setIconSize(QSize(25,25))

dlg8.pushButton_6.setIcon(gallerys)
dlg8.pushButton_6.setIconSize(QSize(25,25))
dlg8.pushButton_7.setIcon(removes)
dlg8.pushButton_7.setIconSize(QSize(25,25))
dlg8.pushButton_5.setIcon(edits)
dlg8.pushButton_5.setIconSize(QSize(25,25))

dlg9.add_invoice_pb.setIcon(saves)
dlg9.add_invoice_pb.setIconSize(QSize(25,25))

dlg10.update_invoice_pb.setIcon(edits)
dlg10.update_invoice_pb.setIconSize(QSize(25,25))

dlg3.label_32.setPixmap(pixmap)
dlg2.label_18.setPixmap(pixmap)
dlg2.label_19.setPixmap(pixmap)
dlg4.label_32.setPixmap(pixmap)
dlg6.label_2.setPixmap(deleteimage)

def clearData_invoice():
    dlg9.table_tw.clearSelection()
    while dlg9.table_tw.rowCount()>0:
        dlg9.table_tw.removeRow(0)
        dlg9.table_tw.clearSelection()

def clearData():
    dlg.tableWidget.clearSelection()
    while dlg.tableWidget.rowCount()>0:
        dlg.tableWidget.removeRow(0)
        dlg.tableWidget.clearSelection()

def clearData_Company():
    dlg.tableWidget_2.clearSelection()
    while dlg.tableWidget_2.rowCount()>0:
        dlg.tableWidget_2.removeRow(0)
        dlg.tableWidget_2.clearSelection()

def clearData_Customer():
    dlg.tableWidget_3.clearSelection()
    while dlg.tableWidget_3.rowCount()>0:
        dlg.tableWidget_3.removeRow(0)
        dlg.tableWidget_3.clearSelection()

def loadData_Customer():
    users = helper.select("SELECT * FROM customertest1 ORDER BY cust_id ASC")

    for row_number,user in enumerate(users):
        dlg.tableWidget_3.insertRow(row_number)
        for column_number,data in enumerate(user):
            cell = QtWidgets.QTableWidgetItem(str(data))
            dlg.tableWidget_3.setItem(row_number,column_number,cell)

    edit = QPixmap('Images/edit64.png')
    edit64 = QIcon(edit)

    delete = QPixmap('Images/delete64.png')
    delete64 = QIcon(delete)

    rows=helper.select("SELECT cust_id from customertest1 ORDER BY cust_id ASC")
    count=0
    for row in rows:
        btn1 = QtWidgets.QPushButton()
        btn1.setIcon(edit64)
        btn1.setIconSize(QSize(30, 30))
        btn2 = QtWidgets.QPushButton()
        btn2.setIcon(delete64)
        btn2.setIconSize(QSize(30, 30))
        dlg.tableWidget_3.setCellWidget(count, 19, btn1)
        dlg.tableWidget_3.setCellWidget(count, 20, btn2)
        btn1.clicked.connect(partial(main_window_to_customer, action=row[0]))
        btn2.clicked.connect(partial(delete_customer, action=row[0]))
        count+=1


def main_window_to_customer(action):
    try:
        global action_new_customer
        action_new_customer=action
        #print(action)

        data = helper.select("SELECT * FROM customertest1 where cust_id="+str(action))
        data=data[0]
        #print(data)
        dict1={}
        dict2={}
        a=dlg8.comboBox_2.count()
        #print(a)
        for i in range(a):
            #lst.append(dlg4.comboBox_2.itemText(i))
            dict1[dlg8.comboBox_2.itemText(i)]=i
        #print(dict1)
        #print(dict1[data[1]])

        b=dlg8.comboBox_3.count()
        for i in range(b):
            dict2[dlg8.comboBox_3.itemText(i)]=i

        global img_customer
        img_customer=data[7]
        filename='C:\\Users\DELL\.PyCharmCE2018.2\config\scratches\pyqt\Project\Download\\'+data[7]
        pix=QPixmap(filename)
        dlg8.lineEdit_12.setText(data[1])
        dlg8.lineEdit_8.setText(data[2])
        dlg8.lineEdit_9.setText(data[3])
        dlg8.lineEdit_10.setText(data[4])
        dlg8.textEdit_2.setText(data[10])
        dlg8.textEdit_3.setText(data[6])
        dlg8.lineEdit_3.setText(data[5])
        dlg8.lineEdit_2.setText(str(data[11]))
        dlg8.lineEdit_7.setText(data[12])
        dlg8.lineEdit_11.setText(data[13])
        dlg8.lineEdit_6.setText(data[14])
        dlg8.label_32.setPixmap(pix)
        #print(dict1[data[1]])
        #print(type(data[1]))
        dlg8.comboBox_2.setCurrentIndex(dict1[data[8]])
        #dlg4.comboBox_2.setEditText(str(data[1]))
        dlg8.comboBox_3.setCurrentIndex(dict2[data[9]])
        #print(data[9])
        #print(data[10])
        dlg8.show()

    except Exception as e:
        print(e)




def loadData_Company():
    users = helper.select("SELECT * FROM companytest3 ORDER BY comp_id ASC")

    for row_number,user in enumerate(users):
        dlg.tableWidget_2.insertRow(row_number)
        for column_number,data in enumerate(user):
            cell = QtWidgets.QTableWidgetItem(str(data))
            dlg.tableWidget_2.setItem(row_number,column_number,cell)

    edit = QPixmap('Images/edit64.png')
    edit64 = QIcon(edit)

    delete = QPixmap('Images/delete64.png')
    delete64 = QIcon(delete)

    rows=helper.select("SELECT comp_id from companytest3 ORDER BY comp_id ASC")
    count=0
    for row in rows:
        btn1 = QtWidgets.QPushButton()
        btn1.setIcon(edit64)
        btn1.setIconSize(QSize(30, 30))
        btn2 = QtWidgets.QPushButton()
        btn2.setIcon(delete64)
        btn2.setIconSize(QSize(30, 30))
        dlg.tableWidget_2.setCellWidget(count, 21, btn1)
        dlg.tableWidget_2.setCellWidget(count, 22, btn2)
        btn1.clicked.connect(partial(main_window_to_company, action=row[0]))
        btn2.clicked.connect(partial(delete_company, action=row[0]))
        count+=1

def main_window_to_company(action):
    try:


        global action_new_company
        action_new_company=action
        #print(action)

        funcomp(dlg7)
        data = helper.select("SELECT * FROM companytest3 where comp_id="+str(action))
        data=data[0]
        #print(data)
        #print(data)
        dict1={}
        dict2={}
        dict3={}
        dict4={}
        dict5={}
        a=dlg7.comboBox.count()
        #print("Count:"+str(a))
        #print(a)
        for i in range(a):
            #lst.append(dlg4.comboBox_2.itemText(i))
            dict1[dlg7.comboBox.itemText(i)]=i
        #print(dict1)
        #print(dict1[data[1]])

        b=dlg7.city_cmb.count()
        for i in range(b):
            dict2[dlg7.city_cmb.itemText(i)]=i

        c=dlg7.comboBox_3.count()
        for i in range(c):
            dict3[dlg7.comboBox_3.itemText(i)]=i

        d = dlg7.comboBox_4.count()
        for i in range(d):
            dict4[dlg7.comboBox_4.itemText(i)] = i

        e = dlg7.comboBox_5.count()
        for i in range(e):
            dict5[dlg7.comboBox_5.itemText(i)] = i

        dlg7.city_cmb.setCurrentIndex(dict2[data[3]])
        dlg7.comboBox_3.setCurrentIndex(dict3[data[4]])
        dlg7.comboBox_4.setCurrentIndex(dict4[data[10]])
        dlg7.comboBox_5.setCurrentIndex(dict5[data[11]])


        # print(dict1)
        # print("City: "+str(dict2[data[3]]))
        # print(dict3)
        # print(dict4)
        # print(dict5)
        #
        # print(data[2])
        # print(data[3])
        # print(data[4])
        # print(data[10])
        # print(data[11])

        global img_logo
        global img_sign
        img_logo=data[15]
        img_sign=data[16]
        filenamelogo='C:\\Users\DELL\.PyCharmCE2018.2\config\scratches\pyqt\Project\Download\\'+data[15]
        filenamesign='C:\\Users\DELL\.PyCharmCE2018.2\config\scratches\pyqt\Project\Download\\'+data[16]
        pixlogo=QPixmap(filenamelogo)
        pixsign=QPixmap(filenamesign)
        dlg7.lineEdit.setText(data[1])
        dlg7.lineEdit_8.setText(data[9])
        dlg7.lineEdit_3.setText(data[7])
        dlg7.lineEdit_2.setText(str(data[6]))
        dlg7.textEdit.setText(data[5])
        dlg7.lineEdit_4.setText(data[8])
        dlg7.lineEdit_5.setText(data[12])
        dlg7.lineEdit_6.setText(data[14])
        dlg7.lineEdit_7.setText(data[13])
        dlg7.label_18.setPixmap(pixlogo)
        dlg7.comboBox.setCurrentIndex(dict1[data[2]])
        dlg7.label_19.setPixmap(pixsign)
        #print(dict1[data[1]])
        #print(type(data[1]))
        #dlg4.comboBox_2.setEditText(str(data[1]))

        #print(data[9])
        #print(data[10])
        dlg7.show()

    except Exception as e:
        print(e)



def loadData():
    #dlg.tableWidget.hide()
    users = helper.select("SELECT * FROM productservicetest2 ORDER BY prd_id ASC")



    # MainWindow = QtWidgets.QMainWindow()
    # horizontal_new = QtWidgets.QHBoxLayout()
    # horizontal_new.setContentsMargins(-1, -1, -1, 15)
    # horizontal_new.setObjectName("horizontal_new")
    # for i in users:
    #     for j in range(4):
    #         #print(i[0])
    #         print(str(i[2]))
    #         button_new=QtWidgets.QPushButton()
    #         label_new = QtWidgets.QLabel()
    #         label_new.setText(str(i[j])+"\n")
    #         horizontal_new.addWidget(button_new)
    #     dlg2.verticalLayout_5.addLayout(horizontal_new)
    #bts=QtWidgets.QPushButton()
    #dlg.tableWidget.setCellWidget(1,18,bts)


        #dlg2.verticalLayout_5.addLayout(v)



    #buffer=QSqlRecord()
    #a=buffer.value("prd_type")
    #print(type(a))
    #print(str(a))
    #print(users)
    #clearData()
    #pixmap=QPixmap("icon.png")
    #dlg.label_6.setPixmap(pixmap)
    #dlg.label_7.setPixmap(pixmap)


    for row_number,user in enumerate(users):
        dlg.tableWidget.insertRow(row_number)
        for column_number,data in enumerate(user):
            cell = QtWidgets.QTableWidgetItem(str(data))
            dlg.tableWidget.setItem(row_number,column_number,cell)

    edit = QPixmap('Images/edit64.png')
    edit64 = QIcon(edit)

    delete = QPixmap('Images/delete64.png')
    delete64 = QIcon(delete)

    rows=helper.select("SELECT prd_id from productservicetest2 ORDER BY prd_id ASC")
    count=0
    for row in rows:
        btn1 = QtWidgets.QPushButton()
        # btn1.setText("Click"+str(i+1))
        btn1.setIcon(edit64)
        btn1.setIconSize(QSize(30, 30))
        btn2 = QtWidgets.QPushButton()
        # btn2.setText("Click" + str(i + 1))
        btn2.setIcon(delete64)
        btn2.setIconSize(QSize(30, 30))
        dlg.tableWidget.setCellWidget(count, 17, btn1)
        dlg.tableWidget.setCellWidget(count, 18, btn2)
        btn1.clicked.connect(partial(main_window_to_product, action=row[0]))
        btn2.clicked.connect(partial(delete_product_service, action=row[0]))
        count+=1

    # length=len(users)
    #
    # for i in range(length):
    #     btn1= QtWidgets.QPushButton()
    #     #btn1.setText("Click"+str(i+1))
    #     btn1.setIcon(edit64)
    #     btn1.setIconSize(QSize(30,30))
    #     btn2 = QtWidgets.QPushButton()
    #     #btn2.setText("Click" + str(i + 1))
    #     btn2.setIcon(delete64)
    #     btn2.setIconSize(QSize(30,30))
    #     dlg.tableWidget.setCellWidget(i, 17, btn1)
    #     dlg.tableWidget.setCellWidget(i, 18, btn2)
    #     btn1.clicked.connect(partial(main_window_to_product, action=i+1))
    #     btn2.clicked.connect(partial(delete_product_service, action=i+1))


def delete_product_service(action):
    try:
        #print(action)
        #print(type(action))
        dlg6.show()
        rsp=dlg6.exec_()
        if rsp == QtWidgets.QDialog.Accepted:
            helper.delete("Delete from productservicetest2 where prd_id="+str(action))
            clearData()
            loadData()
        else:
            dlg6.close()
    except Exception as e:
        print("Delete:"+str(e))

def delete_company(action):
    try:
        dlg6.show()
        rsp=dlg6.exec_()
        if rsp == QtWidgets.QDialog.Accepted:
            helper.delete("Delete from companytest3 where comp_id="+str(action))
            clearData_Company()
            loadData_Company()
        else:
            dlg6.close()
    except Exception as e:
        print("Delete:"+str(e))

def delete_customer(action):
    try:
        dlg6.show()
        rsp=dlg6.exec_()
        if rsp == QtWidgets.QDialog.Accepted:
            helper.delete("Delete from customertest1 where cust_id="+str(action))
            clearData_Customer()
            loadData_Customer()
        else:
            dlg6.close()
    except Exception as e:
        print("Delete:"+str(e))




def main_window_to_product(action):
    try:
        global action_new
        action_new=action
        #print(action)

        funpro(dlg5)
        data = helper.select("SELECT * FROM productservicetest2 where prd_id="+str(action))
        data=data[0]
        #print(data)
        dict1={}
        dict2={}
        dict3={}
        a=dlg5.comboBox_2.count()
        #print(a)
        for i in range(a):
            #lst.append(dlg4.comboBox_2.itemText(i))
            dict1[dlg5.comboBox_2.itemText(i)]=i
        #print(dict1)
        #print(dict1[data[1]])

        b=dlg5.comboBox_3.count()
        for i in range(b):
            dict2[dlg5.comboBox_3.itemText(i)]=i

        c=dlg5.comboBox_4.count()
        for i in range(c):
            tax = dlg5.comboBox_4.itemText(i).split("%")
            prd_tax = float(tax[0])
            dict3[prd_tax]=i

        global image_nam
        image_nam=data[12]
        filename='C:\\Users\DELL\.PyCharmCE2018.2\config\scratches\pyqt\Project\Download\\'+data[12]
        pix=QPixmap(filename)
        dlg5.lineEdit_13.setText(data[3])
        dlg5.lineEdit_12.setText(data[4])
        dlg5.lineEdit_8.setText(data[6])
        dlg5.lineEdit_9.setText(str(data[8]))
        dlg5.textEdit.setText(data[5])
        dlg5.lineEdit_11.setText(str(data[11]))
        dlg5.label_32.setPixmap(pix)
        #print(dict1[data[1]])
        #print(type(data[1]))
        dlg5.comboBox_2.setCurrentIndex(dict1[data[1]])
        #dlg4.comboBox_2.setEditText(str(data[1]))
        dlg5.comboBox_3.setCurrentIndex(dict2[data[2]])
        dlg5.comboBox_4.setCurrentIndex(dict3[data[9]])
        #print(data[9])
        #print(data[10])
        dlg5.spinBox.setValue(data[10])
        dlg5.show()

    except Exception as e:
        print(e)


def show_msg(title,message):
    QMessageBox.information(None,title,message)

def dateandtime():
    date = datetime.now()
    dte = str(date.day) + "/" + str(date.month) + "/" + str(date.year)
    time = str(date.hour) + ":" + str(date.minute) + ":" + str(date.second)
    dandt = dte + " " + time
    return dandt


def image_logo():
    filtr="Images (*.png *.jpg *.jpeg)"
    filename=QFileDialog.getOpenFileName(None,"Browse","",filtr)[0]
    if filename!="":
        global lst
        lst=filename.split('/')
        pix=QPixmap(filename)
        global comp_logo
        date = datetime.now()
        new_date_time=str(date.year)+str(date.month)+str(date.day)+str(date.hour)+str(date.minute)+str(date.second)
        comp_logo = new_date_time + "_" + lst[-1]
        dlg2.label_18.setPixmap(pix)
        shutil.copy(filename,'C:\\Users\DELL\.PyCharmCE2018.2\config\scratches\pyqt\Project\Download\\'+comp_logo)

def image_update_logo():
    filtr="Images (*.png *.jpg *.jpeg)"
    #global filename1
    filename1=QFileDialog.getOpenFileName(None,"Browse","",filtr)[0]
    if filename1!="":
        global lst6
        lst6=filename1.split('/')
        pix=QPixmap(filename1)
        date = datetime.now()
        new_date_time=str(date.year)+str(date.month)+str(date.day)+str(date.hour)+str(date.minute)+str(date.second)
        #global update_company_logo
        #global img1
        update_company_logo = new_date_time + "_" + lst6[-1]
        dlg7.label_18.setPixmap(pix)
        img1 = update_company_logo
        print(img1)
        shutil.copy(filename1, 'C:\\Users\DELL\.PyCharmCE2018.2\config\scratches\pyqt\Project\Download\\' + img1)
        par = (img1, action_new_company)
        helper.update("UPDATE companytest3 SET comp_logo=%s WHERE comp_id=%s", par)
    else:
        im=img_logo
        print(im)
        pa=(im,action_new_company)
        helper.update("UPDATE companytest3 SET comp_logo=%s WHERE comp_id=%s", pa)


        # else:
        #     img1=img_logo
        #print("Value from browse:"+str(update_company_logo))

        #shutil.copy(filename,'C:\\Users\DELL\.PyCharmCE2018.2\config\scratches\pyqt\Project\Download\\'+update_company_logo)



def image_signature():
    filtr="Images (*.png *.jpg *.jpeg,*.PNG)"
    filename=QFileDialog.getOpenFileName(None,"Browse","",filtr)[0]
    if filename!="":
        global lst2
        lst2=filename.split('/')
        pix=QPixmap(filename)
        date = datetime.now()
        new_date_time = str(date.year) + str(date.month) + str(date.day) + str(date.hour) + str(date.minute) + str(date.second)
        global comp_sign
        comp_sign = new_date_time + "_" + lst2[-1]
        dlg2.label_19.setPixmap(pix)
        shutil.copy(filename,'C:\\Users\DELL\.PyCharmCE2018.2\config\scratches\pyqt\Project\Download\\'+comp_sign)

def image_update_signature():
    filtr="Images (*.png *.jpg *.jpeg,*.PNG)"
    #global filename2
    filename2=QFileDialog.getOpenFileName(None,"Browse","",filtr)[0]
    if filename2!="":
        global lst7
        lst7=filename2.split('/')
        pix=QPixmap(filename2)
        date = datetime.now()
        new_date_time = str(date.year) + str(date.month) + str(date.day) + str(date.hour) + str(date.minute) + str(date.second)
        #global update_company_signature
        #global img2
        update_company_signature = new_date_time + "_" + lst7[-1]
        img2=update_company_signature
        shutil.copy(filename2, 'C:\\Users\DELL\.PyCharmCE2018.2\config\scratches\pyqt\Project\Download\\' + img2)
        dlg7.label_19.setPixmap(pix)
        print(img2)
        par = (img2, action_new_company)
        helper.update("UPDATE companytest3 SET comp_sign=%s WHERE comp_id=%s", par)
    else:
        im = img_sign
        print(im)
        pa = (im, action_new_company)
        helper.update("UPDATE companytest3 SET comp_sign=%s WHERE comp_id=%s", pa)
        #shutil.copy(filename,'C:\\Users\DELL\.PyCharmCE2018.2\config\scratches\pyqt\Project\Download\\'+update_company_signature)


def image_product_service():
    filtr="Images (*.png *.jpg *.jpeg)"
    filename=QFileDialog.getOpenFileName(None,"Browse","",filtr)[0]
    print(filename)
    if filename!="":
        global lst3
        lst3=filename.split('/')
        pix=QPixmap(filename)
        global product_service_logo
        date = datetime.now()
        new_date_time=str(date.year)+str(date.month)+str(date.day)+str(date.hour)+str(date.minute)+str(date.second)
        product_service_logo = new_date_time + "_" + lst3[-1]
        dlg4.label_32.setPixmap(pix)
        shutil.copy(filename,'C:\\Users\DELL\.PyCharmCE2018.2\config\scratches\pyqt\Project\Download\\'+product_service_logo)


def image_update_product_service():
    filtr="Images (*.png *.jpg *.jpeg)"
    filename=QFileDialog.getOpenFileName(None,"Browse","",filtr)[0]
    print(filename)
    if filename!="":
        global lst5
        lst5=filename.split('/')
        pix=QPixmap(filename)
        date = datetime.now()
        new_date_time=str(date.year)+str(date.month)+str(date.day)+str(date.hour)+str(date.minute)+str(date.second)
        update_product_service_logo = new_date_time + "_" + lst5[-1]
        print(update_product_service_logo)
        print(type(update_product_service_logo))
        dlg5.label_32.setPixmap(pix)
        img4=update_product_service_logo
        shutil.copy(filename,'C:\\Users\DELL\.PyCharmCE2018.2\config\scratches\pyqt\Project\Download\\'+img4)
        par = (img4, action_new)
        helper.update("UPDATE productservicetest2 SET prd_image=%s WHERE prd_id=%s", par)
    else:
        i = image_nam
        print(i)
        pa = (i, action_new)
        helper.update("UPDATE productservicetest2 SET prd_image=%s WHERE prd_id=%s", pa)
def image_customer():
    filtr="Images (*.png *.jpg *.jpeg)"
    filename=QFileDialog.getOpenFileName(None,"Browse","",filtr)[0]
    if filename!="":
        global lst4
        lst4=filename.split('/')
        pix=QPixmap(filename)
        global customer_logo
        date = datetime.now()
        new_date_time=str(date.year)+str(date.month)+str(date.day)+str(date.hour)+str(date.minute)+str(date.second)
        customer_logo = new_date_time + "_" + lst4[-1]
        dlg3.label_32.setPixmap(pix)
        shutil.copy(filename,'C:\\Users\DELL\.PyCharmCE2018.2\config\scratches\pyqt\Project\Download\\'+customer_logo)

def image_update_customer():
    filtr="Images (*.png *.jpg *.jpeg)"
    filename=QFileDialog.getOpenFileName(None,"Browse","",filtr)[0]
    if filename!="":
        global lst8
        lst8=filename.split('/')
        pix=QPixmap(filename)
        date = datetime.now()
        new_date_time=str(date.year)+str(date.month)+str(date.day)+str(date.hour)+str(date.minute)+str(date.second)
        customer_update_logo = new_date_time + "_" + lst8[-1]
        dlg8.label_32.setPixmap(pix)
        img3=customer_update_logo
        shutil.copy(filename,'C:\\Users\DELL\.PyCharmCE2018.2\config\scratches\pyqt\Project\Download\\'+img3)
        par = (img3, action_new_customer)
        helper.update("UPDATE customertest1 SET cust_img=%s WHERE cust_id=%s", par)
    else:
        i = img_customer
        print(i)
        pa = (i, action_new_customer)
        helper.update("UPDATE customertest1 SET cust_img=%s WHERE cust_id=%s", pa)

def remove_logo():
    dlg2.label_18.clear()
    os.remove('C:\\Users\DELL\.PyCharmCE2018.2\config\scratches\pyqt\Project\Download\\'+comp_logo)
    dlg2.label_18.setPixmap(pixmap)

def remove_signature():
    dlg2.label_19.clear()
    os.remove('C:\\Users\DELL\.PyCharmCE2018.2\config\scratches\pyqt\Project\Download\\'+comp_sign)
    dlg2.label_19.setPixmap(pixmap)

def remove_update_logo():
    try:
        dlg7.label_18.clear()
        # img=""
        # flag = 0
        # if update_company_logo=="":
        #     img = img_logo
        #     flag = 1
        # if flag == 0:
        #     img = update_company_logo

        # print("update company logo::"+str(update_company_logo))
        # tmp_img=update_company_logo
        # if tmp_img!="":
        #     img1 = tmp_img
        #     print("First:"+str(img1))
        # else:
        #     img1 = img_logo
        #     print("DB:"+str(img1))
        # print(img1)
        #os.remove('C:\\Users\DELL\.PyCharmCE2018.2\config\scratches\pyqt\Project\Download\\'+img)
        dlg7.label_18.setPixmap(pixmap)
    except Exception as e:
        print("Logo:"+str(e))

def remove_update_signature():
    try:
        dlg7.label_19.clear()
        # img=""
        # flag=0
        # if update_company_signature=="":
        #     img=img_sign
        #     flag=1
        # if flag==0:
        #     img = update_company_signature

        # print("update company logo"+str(update_company_logo))
        # tmp_img = update_company_signature
        # if tmp_img != "":
        #     img1 = tmp_img
        #     # print("First:"+str(img1))
        # elif update_company_signature == "":
        #     img1 = img_sign
        #     # print("DB:"+str(img1))
        #os.remove('C:\\Users\DELL\.PyCharmCE2018.2\config\scratches\pyqt\Project\Download\\'+img)
        dlg7.label_19.setPixmap(pixmap)
    except Exception as e:
        print("Signature:"+str(e))


def remove_product_service():
    dlg4.label_32.clear()
    os.remove('C:\\Users\DELL\.PyCharmCE2018.2\config\scratches\pyqt\Project\Download\\'+product_service_logo)
    dlg4.label_32.setPixmap(pixmap)

#global flag
#flag=0

def remove_update_product_service():
    try:
        dlg5.label_32.clear()
        img=""
        flag=0
        if flag==0:
            update_product_service_logo=""
            img=image_nam
            flag=1
        # print("update company logo"+str(update_company_logo))
        # tmp_img = update_product_service_logo
        # if tmp_img != "":
        #     img1 = tmp_img
        #     # print("First:"+str(img1))
        # elif update_product_service_logo == "":
        #     img1 = image_nam
        #     # print("DB:"+str(img1))
        if flag==1:
            if update_product_service_logo != "":
                img = update_product_service_logo
            else:
                img = image_nam
        os.remove('C:\\Users\DELL\.PyCharmCE2018.2\config\scratches\pyqt\Project\Download\\'+img)
        dlg5.label_32.setPixmap(pixmap)
    except Exception as e:
        print("REMOVE UPDATE PRODUCT:"+str(e))

def remove_customer():
    dlg3.label_32.clear()
    os.remove('C:\\Users\DELL\.PyCharmCE2018.2\config\scratches\pyqt\Project\Download\\'+customer_logo)
    dlg3.label_32.setPixmap(pixmap)

def add_company():
    try:
        dict1={}
        flag=0
        company_name=dlg2.lineEdit.text()
        contact_no=dlg2.lineEdit_8.text()
        email=dlg2.lineEdit_3.text()
        service_category=dlg2.comboBox.currentText()

        b = dlg2.comboBox.count()
        for i in range(b):
            dict1[dlg2.comboBox.itemText(i)] = i
        # print(dict1)
        # print(prd_type)
        # print(dict1.keys())
        for i in dict1.keys():
            print("KEYS:" + str(i.lower()))
            print("Input:" + str(service_category.lower()))
            if service_category.lower() == i.lower():
                flag = 1
                print("Matched")
                break
        if flag == 0:
            par = (service_category, "Nothing", dateandtime(), dateandtime(), dateandtime(), "Enable")
            helper.insert("INSERT INTO servicecategorytest1 (ser_name,ser_description,ser_created_at,ser_updated_at,ser_deleted_at,ser_status) VALUES (%s,%s,%s,%s,%s,%s)",par)

        city=dlg2.comboBox_2.currentText()
        state=dlg2.comboBox_3.currentText()
        address=dlg2.textEdit.toPlainText()
        pincode=dlg2.lineEdit_2.text()
        website=dlg2.lineEdit_4.text()
        tax_type=dlg2.comboBox_4.currentText()
        tax_inclusive=dlg2.comboBox_5.currentText()
        tin_no=dlg2.lineEdit_5.text()
        pan_no=dlg2.lineEdit_6.text()
        gst_no=dlg2.lineEdit_7.text()
        status="Enable"
        #date = datetime.now()
        #dte = str(date.day) + "/" + str(date.month) + "/" + str(date.year)
        #time = str(date.hour) + ":" + str(date.minute) + ":" + str(date.second)
        #dandt = dte + " " + time

        if company_name.strip(" ")!="" and contact_no.strip(" ")!="" and email.strip(" ")!="" and service_category.strip(" ")!="" and city.strip(" ")!="" and state.strip(" ")!="":
            parameters=(company_name,service_category,city,state,address,pincode,email,website,contact_no,tax_type,tax_inclusive,tin_no,gst_no,pan_no,comp_logo,comp_sign,dateandtime(),dateandtime(),dateandtime(),status)
            helper.insert("INSERT INTO companytest3 (comp_name , cat_id , comp_city , comp_state , comp_address , comp_pincode , comp_email , comp_website , comp_contact_no , comp_tax_type , comp_tax_inclusive , comp_tinno , comp_gstno , comp_panno , comp_logo , comp_sign , comp_created_at  , comp_updated_at , comp_deleted_at ,comp_status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",parameters)
            show_msg("Success","Company created successfully")
            clear_add_company()
        else:
            show_msg("Empty Field(s)","Please fill all the mandatory fields")
        funcomp(dlg2)

    except Exception as e:
        print("Error:"+str(e))

def update_company():
    try:
        dict1={}
        flag=0
        company_name=dlg7.lineEdit.text()
        contact_no=dlg7.lineEdit_8.text()
        email=dlg7.lineEdit_3.text()
        service_category=dlg7.comboBox.currentText()

        b = dlg7.comboBox.count()
        for i in range(b):
            dict1[dlg7.comboBox.itemText(i)] = i
        # print(dict1)
        # print(prd_type)
        # print(dict1.keys())
        for i in dict1.keys():
            print("KEYS:" + str(i.lower()))
            print("Input:" + str(service_category.lower()))
            if service_category.lower() == i.lower():
                flag = 1
                print("Matched")
                break
        if flag == 0:
            par = (service_category, "Nothing", dateandtime(), dateandtime(), dateandtime(), "Enable")
            helper.insert("INSERT INTO servicecategorytest1 (ser_name,ser_description,ser_created_at,ser_updated_at,ser_deleted_at,ser_status) VALUES (%s,%s,%s,%s,%s,%s)",par)

        city=dlg7.city_cmb.currentText()
        state=dlg7.comboBox_3.currentText()
        address=dlg7.textEdit.toPlainText()
        pincode=dlg7.lineEdit_2.text()
        website=dlg7.lineEdit_4.text()
        tax_type=dlg7.comboBox_4.currentText()
        tax_inclusive=dlg7.comboBox_5.currentText()
        tin_no=dlg7.lineEdit_5.text()
        pan_no=dlg7.lineEdit_6.text()
        gst_no=dlg7.lineEdit_7.text()
        status="Enable"
        # if filename1=="":
        #     print("Printing1")
        #     img1=img_logo
        #
        # if filename2=="":
        #     print("Printing2")
        #     img2=img_sign
        #date = datetime.now()
        #dte = str(date.day) + "/" + str(date.month) + "/" + str(date.year)
        #time = str(date.hour) + ":" + str(date.minute) + ":" + str(date.second)
        #dandt = dte + " " + time

        #else:
            #os.remove('C:\\Users\DELL\.PyCharmCE2018.2\config\scratches\pyqt\Project\Download\\' + img_logo)

        #print("LOGOIMAGE:"+str(img1))



        # if update_company_signature!="":
        #     img2=update_company_signature
        #     shutil.copy(filename2, 'C:\\Users\DELL\.PyCharmCE2018.2\config\scratches\pyqt\Project\Download\\' + img2)
        # else:
        #     img2=img_sign
        #else:
            #os.remove('C:\\Users\DELL\.PyCharmCE2018.2\config\scratches\pyqt\Project\Download\\' + img_sign)
        #print("SIGNATURE:"+str(img2))



        if company_name.strip(" ")!="" and contact_no.strip(" ")!="" and email.strip(" ")!="" and service_category.strip(" ")!="" and city.strip(" ")!="" and state.strip(" ")!="":
            parameters=(company_name,service_category,city,state,address,pincode,email,website,contact_no,tax_type,tax_inclusive,tin_no,gst_no,pan_no,dateandtime(),dateandtime(),status,action_new_company)
            #helper.insert("INSERT INTO companytest3 (comp_name , cat_id , comp_city , comp_state , comp_address , comp_pincode , comp_email , comp_website , comp_contact_no , comp_tax_type , comp_tax_inclusive , comp_tinno , comp_gstno , comp_panno , comp_logo , comp_sign , comp_created_at  , comp_updated_at , comp_deleted_at ,comp_status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",parameters)
            helper.update("UPDATE companytest3 SET comp_name=%s , cat_id=%s , comp_city=%s , comp_state=%s , comp_address=%s , comp_pincode=%s , comp_email=%s , comp_website=%s , comp_contact_no=%s , comp_tax_type=%s , comp_tax_inclusive=%s , comp_tinno=%s , comp_gstno=%s , comp_panno=%s  , comp_updated_at=%s , comp_deleted_at=%s ,comp_status=%s WHERE comp_id=%s",parameters)
            show_msg("Success","Company updated successfully")
            dlg7.close()
            clearData_Company()
            loadData_Company()

        else:
            show_msg("Empty Field(s)","Please fill all the mandatory fields")

    except Exception as e:
        print("Error:"+str(e))




def add_customer():
    try:
        cust_name=dlg3.lineEdit_12.text()
        cust_contact_person=dlg3.lineEdit_8.text()
        cust_contact_no=dlg3.lineEdit_9.text()
        cust_email=dlg3.lineEdit_10.text()
        cust_website=dlg3.lineEdit_3.text()
        cust_imp_note=dlg3.textEdit_3.toPlainText()
        cust_city=dlg3.comboBox_2.currentText()
        cust_state=dlg3.comboBox_3.currentText()
        cust_address=dlg3.textEdit_2.toPlainText()
        cust_pincode=dlg3.lineEdit_2.text()
        cust_gst_no=dlg3.lineEdit_7.text()
        cust_tin_no=dlg3.lineEdit_11.text()
        cust_pan_no=dlg3.lineEdit_6.text()
        cust_status="Enable"

        if cust_name.strip(" ")!="" and cust_contact_person.strip(" ")!="" and cust_contact_no.strip(" ")!="" and cust_email.strip(" ")!="" and cust_city.strip(" ")!="" and cust_state.strip(" ")!="":
            parameters=(cust_name,cust_contact_person,cust_contact_no,cust_email,cust_website,cust_imp_note,customer_logo,cust_city,cust_state,cust_address,cust_pincode,cust_gst_no,cust_tin_no,cust_pan_no,dateandtime(),dateandtime(),dateandtime(),cust_status)
            helper.insert("INSERT INTO customertest1 (cust_name,cust_contact_person,cust_contact_no,cust_email,cust_website,cust_imp_note,cust_img,cust_city,cust_state,cust_address,cust_pincode,cust_gst_no,cust_tin_no,cust_pan_no,cust_created_at,cust_updated_at,cust_deleted_at,cust_status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",parameters)
            show_msg("Success","Customer created successfully")
            clear_add_customer()
        else:
            show_msg("Empty Field(s)","Please fill all the mandatory fields")


    except Exception as e:
        print("Error:"+str(e))


def update_customer():
    try:
        cust_name=dlg8.lineEdit_12.text()
        cust_contact_person=dlg8.lineEdit_8.text()
        cust_contact_no=dlg8.lineEdit_9.text()
        cust_email=dlg8.lineEdit_10.text()
        cust_website=dlg8.lineEdit_3.text()
        cust_imp_note=dlg8.textEdit_3.toPlainText()
        cust_city=dlg8.comboBox_2.currentText()
        cust_state=dlg8.comboBox_3.currentText()
        cust_address=dlg8.textEdit_2.toPlainText()
        cust_pincode=dlg8.lineEdit_2.text()
        cust_gst_no=dlg8.lineEdit_7.text()
        cust_tin_no=dlg8.lineEdit_11.text()
        cust_pan_no=dlg8.lineEdit_6.text()
        cust_status="Enable"

        if cust_name.strip(" ")!="" and cust_contact_person.strip(" ")!="" and cust_contact_no.strip(" ")!="" and cust_email.strip(" ")!="" and cust_city.strip(" ")!="" and cust_state.strip(" ")!="":
            parameters=(cust_name,cust_contact_person,cust_contact_no,cust_email,cust_website,cust_imp_note,cust_city,cust_state,cust_address,cust_pincode,cust_gst_no,cust_tin_no,cust_pan_no,dateandtime(),dateandtime(),cust_status,action_new_customer)
            #helper.insert("INSERT INTO customertest1 (cust_name,cust_contact_person,cust_contact_no,cust_email,cust_website,cust_imp_note,cust_img,cust_city,cust_state,cust_address,cust_pincode,cust_gst_no,cust_tin_no,cust_pan_no,cust_created_at,cust_updated_at,cust_deleted_at,cust_status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",parameters)
            helper.update("UPDATE customertest1 SET cust_name=%s,cust_contact_person=%s,cust_contact_no=%s,cust_email=%s,cust_website=%s,cust_imp_note=%s,cust_city=%s,cust_state=%s,cust_address=%s,cust_pincode=%s,cust_gst_no=%s,cust_tin_no=%s,cust_pan_no=%s,cust_updated_at=%s,cust_deleted_at=%s,cust_status=%s WHERE cust_id=%s",parameters)
            show_msg("Success","Customer updated successfully")
            dlg8.close()
            clearData_Customer()
            loadData_Customer()
        else:
            show_msg("Empty Field(s)","Please fill all the mandatory fields")


    except Exception as e:
        print("Error:"+str(e))


def add_product_service():
    try:
        flag=0
        dict1={}

        prd_type=dlg4.comboBox_2.currentText()
        prd_category=dlg4.comboBox_3.currentText()
        b = dlg4.comboBox_3.count()
        for i in range(b):
            dict1[dlg4.comboBox_3.itemText(i)] = i
        #print(dict1)
        #print(prd_type)
        #print(dict1.keys())
        for i in dict1.keys():
            print("KEYS:"+str(i.lower()))
            print("Input:"+str(prd_category.lower()))
            if prd_category.lower()==i.lower():
                flag=1
                print("Matched")
                break
        if flag==0:
            par=(prd_category,"Nothing",dateandtime(),dateandtime(),dateandtime(),"Enable")
            helper.insert("INSERT INTO categorytest1 (cat_name,cat_description,cat_created_at,cat_updated_at,cat_deleted_at,cat_status) VALUES (%s,%s,%s,%s,%s,%s)",par)
            #dlg4.comboBox_3.addItem(prd_category)
        else:
            print("NOT Matched")

        prd_sku=dlg4.lineEdit_13.text()
        prd_name=dlg4.lineEdit_12.text()
        prd_description=dlg4.textEdit.toPlainText()
        prd_hsn=dlg4.lineEdit_8.text()
        prd_sac="Demo"
        prd_unit_price=dlg4.lineEdit_9.text()
        prd_unit_price2=round(float(prd_unit_price),2)
        prd_tax=dlg4.comboBox_4.currentText()
        tax=prd_tax.split("%")
        prd_tax=float(tax[0])
        prd_qty=dlg4.spinBox.value()
        prd_qty=float(prd_qty)
        prd_purchase_price=dlg4.lineEdit_11.text()
        prd_purchase_price=round(float(prd_purchase_price),2)
        prd_status="Enable"

        if prd_type.strip(" ")!="" and prd_category.strip(" ")!="" and prd_name.strip(" ")!="" and prd_unit_price.strip(" ")!="":
            parameters=(prd_type,prd_category,prd_sku,prd_name,prd_description,prd_hsn,prd_sac,prd_unit_price2,prd_tax,prd_qty,prd_purchase_price,product_service_logo,dateandtime(),dateandtime(),dateandtime(),prd_status)
            helper.insert("INSERT INTO productservicetest2 (prd_type,prd_category,prd_sku,prd_name,prd_description,prd_hsn,prd_sac,prd_unit_price,prd_tax,prd_qty,prd_purchase_price,prd_image,prd_created_at,prd_updated_at,prd_deleted_at,prd_status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",parameters)
            show_msg("Success", "Product/Service created successfully")
            clear_add_product_service(dlg4)
        else:
            show_msg("Empty Field(s)","Please fill all the mandatory fields")
        clearData()
        loadData()
        funpro(dlg4)

    except Exception as e:
        print("Error:"+str(e))


def update_product_service():
    try:
        #print(action_new)
        dict1={}
        flag=0
        prd_type = dlg5.comboBox_2.currentText()
        prd_category = dlg5.comboBox_3.currentText()

        b = dlg5.comboBox_3.count()
        for i in range(b):
            dict1[dlg5.comboBox_3.itemText(i)] = i
        # print(dict1)
        # print(prd_type)
        # print(dict1.keys())
        for i in dict1.keys():
            print("KEYS:" + str(i.lower()))
            print("Input:" + str(prd_category.lower()))
            if prd_category.lower() == i.lower():
                flag = 1
                print("Matched")
                break
        if flag == 0:
            par = (prd_category, "Nothing", dateandtime(), dateandtime(), dateandtime(), "Enable")
            helper.insert(
                "INSERT INTO categorytest1 (cat_name,cat_description,cat_created_at,cat_updated_at,cat_deleted_at,cat_status) VALUES (%s,%s,%s,%s,%s,%s)",
                par)
            # dlg4.comboBox_3.addItem(prd_category)
        else:
            print("NOT Matched")


        prd_sku = dlg5.lineEdit_13.text()
        print("sku"+prd_sku)
        prd_name = dlg5.lineEdit_12.text()
        print("name"+prd_name)
        prd_description = dlg5.textEdit.toPlainText()
        print("Desc"+prd_description)
        prd_hsn = dlg5.lineEdit_8.text()
        print("HSN"+prd_hsn)
        prd_sac = "Demo"
        prd_unit_price = dlg5.lineEdit_9.text()
        prd_unit_price2 = round(float(prd_unit_price), 2)
        print('prd'+str(prd_unit_price2))
        print(type(prd_unit_price2))
        prd_tax = dlg5.comboBox_4.currentText()
        tax = prd_tax.split("%")
        prd_tax = float(tax[0])
        print("tax"+str(prd_tax))
        print(type(prd_tax))
        prd_qty = dlg5.spinBox.value()
        prd_qty = float(prd_qty)
        print("qty"+str(prd_qty))
        print(type(prd_qty))
        prd_purchase_price = dlg5.lineEdit_11.text()
        prd_purchase_price = round(float(prd_purchase_price), 2)
        print("purchase"+str(prd_purchase_price))
        print(type(prd_purchase_price))
        prd_status = "Enable"

        if prd_type.strip(" ") != "" and prd_category.strip(" ") != "" and prd_name.strip(" ") != "" and prd_unit_price.strip(" ") != "":
            parameters = (prd_type, prd_category, prd_sku, prd_name, prd_description, prd_hsn, prd_sac, prd_unit_price2, prd_tax, prd_qty,
                      prd_purchase_price, dateandtime(), dateandtime(), prd_status,action_new)
            helper.update(
                "UPDATE productservicetest2 SET prd_type=%s, prd_category=%s, prd_sku=%s, prd_name=%s, prd_description=%s, prd_hsn=%s,"
                " prd_sac=%s, prd_unit_price=%s, prd_tax=%s, prd_qty=%s, prd_purchase_price=%s, prd_updated_at=%s,"
                " prd_deleted_at=%s, prd_status=%s WHERE prd_id=%s",
                parameters)
            #parameters = ("hh", "hh", "hh", "hh", "hh", "hh", "hh", 77.77, 77.77, 7, 77.77, "hh", "hh", "hh", 17)
        #parameters = ("trialss",17)
        #helper.update("UPDATE productservicetest2 SET prd_sku=%s WHERE prd_id=%s",parameters)
            show_msg("Success", "Product/Service updated successfully")

            #clear_add_product_service(dlg5)
            dlg5.close()
            clearData()
            loadData()
            #funpro(dlg5)
        else:
                show_msg("Empty Field(s)", "Please fill all the mandatory fields")

    except Exception as e:
        print("Error:"+str(e))

def clear_add_company():
    dlg2.lineEdit.clear()
    dlg2.lineEdit_8.clear()
    dlg2.lineEdit_3.clear()
    dlg2.comboBox.clearEditText()
    dlg2.comboBox_2.clearEditText()
    dlg2.comboBox_3.clearEditText()
    dlg2.textEdit.clear()
    dlg2.lineEdit_2.clear()
    dlg2.lineEdit_4.clear()
    #dlg2.comboBox_4.clear()
    #dlg2.comboBox_5.clear()
    dlg2.lineEdit_5.clear()
    dlg2.lineEdit_6.clear()
    dlg2.lineEdit_7.clear()
    dlg2.label_18.setPixmap(pixmap)
    dlg2.label_19.setPixmap(pixmap)

def clear_add_customer():
    dlg3.lineEdit_12.clear()
    dlg3.lineEdit_8.clear()
    dlg3.lineEdit_9.clear()
    dlg3.lineEdit_10.clear()
    dlg3.lineEdit_3.clear()
    dlg3.textEdit_3.clear()
    dlg3.comboBox_2.clearEditText()
    dlg3.comboBox_3.clearEditText()
    dlg3.textEdit_2.clear()
    dlg3.lineEdit_2.clear()
    dlg3.lineEdit_7.clear()
    dlg3.lineEdit_11.clear()
    dlg3.lineEdit_6.clear()
    dlg3.label_32.setPixmap(pixmap)

def clear_add_product_service(action):
    action.comboBox_2.currentText()
    action.comboBox_3.clearEditText()
    action.lineEdit_13.clear()
    action.lineEdit_12.clear()
    action.textEdit.clear()
    action.lineEdit_8.clear()
    action.lineEdit_9.clear()
    action.comboBox_4.clearEditText()
    action.spinBox.setValue(0)
    action.lineEdit_11.clear()
    action.label_32.setPixmap(pixmap)


def funpro(action):
    action.comboBox_3.clear()
    action.show()
    row = helper.select("SELECT cat_name from categorytest1")
    l=len(row)
    for i in range(l):
        n = row[i]
        action.comboBox_3.addItem(n[0])

def funcomp(action):
    action.comboBox.clear()
    action.show()
    row = helper.select("SELECT ser_name from servicecategorytest1")
    l = len(row)
    for i in range(l):
        n = row[i]
        action.comboBox.addItem(n[0])




dlg.actionAdd_New_Company.triggered.connect(partial(funcomp,action=dlg2))
dlg.actionAdd_New_Customer.triggered.connect(dlg3.show)
try:
    dlg.actionAdd_Product_Services.triggered.connect(partial(funpro,action=dlg4))
except Exception as e:
    print(e)

def menu_product_service():
    dlg.tableWidget_2.close()
    dlg.tableWidget_3.close()
    dlg.tableWidget.show()


def menu_company():
    dlg.tableWidget.close()
    dlg.tableWidget_3.close()
    dlg.tableWidget_2.show()

def menu_customer():
    dlg.tableWidget.close()
    dlg.tableWidget_2.close()
    dlg.tableWidget_3.show()

def add_invoice_cmb():
    #add_invoice_clear()
    dlg9.subtotal_rs_lbl.setText('00.00')
    dlg9.discount_rs_lbl.setText('00.00')
    dlg9.shipping_packaging_cost_lbl.setText('00.00')
    dlg9.total_cost_lbl.setText('00.00')
    dlg9.cust_name_cmb.clear()
    dlg9.product_cmb.clear()
    dlg9.cust_name_cmb.addItem("Select")
    dlg9.product_cmb.addItem("Select")
    add_invoice_clear()

    clearData_invoice()
    customer=helper.select("Select cust_name,cust_id from customertest1")
    product=helper.select("Select prd_name,prd_id from productservicetest2")
    for i in customer:
        dlg9.cust_name_cmb.addItem(str(i[1])+"-"+i[0])
    for j in product:
        dlg9.product_cmb.addItem(str(j[1])+"-"+j[0])
    dlg9.show()


def invoice_cust_name():
    try:
        customer=dlg9.cust_name_cmb.currentText().split("-")
        if customer[0]!="Select":
            id=int(customer[0])
            result=helper.select("Select cust_city,cust_state,cust_address,cust_pincode from customertest1 where cust_id="+str(id))
            for i in result:
                dlg9.place_le.setText(i[0]+"-"+str(i[3])+", "+i[1])
                dlg9.address_te.setText(i[2])
        else:
            dlg9.place_le.clear()
            dlg9.address_te.clear()
    except Exception as e:
        print(e)

def invoice_product():
    try:
        product=dlg9.product_cmb.currentText().split("-")
        if product[0]!="Select":
            id=int(product[0])
            result=helper.select("Select prd_description,prd_unit_price,prd_tax from productservicetest2 where prd_id="+str(id))
            for i in result:
                dlg9.description_le.setText(i[0])
                dlg9.unit_price_le.setText(str(i[1]))
                dlg9.tax_cmb.clear()
                dlg9.tax_cmb.addItem(str(i[2]))
        else:
            dlg9.description_le.clear()
            dlg9.unit_price_le.clear()
            dlg9.tax_cmb.clear()
    except Exception as e:
        print(e)


def add_invoice_table_widget():
    # dlg9.table_tw.insertRow(1)
    # cell = QtWidgets.QTableWidgetItem(str(1))
    # cell2 = QtWidgets.QTableWidgetItem(str("Product"))
    # dlg9.table_tw.setItem(0,0,cell)
    # dlg9.table_tw.setItem(0, 1, cell2)
    try:
        product=dlg9.product_cmb.currentText()
        if product!="Select":

            delete = QPixmap('Images/delete64.png')
            delete64 = QIcon(delete)


            product = product.split('-')
            id = product[0]
            product_name = product[1]
            description=dlg9.description_le.text()
            uom=dlg9.uom_cmb.currentText()
            unit_price=dlg9.unit_price_le.text()
            discount=dlg9.discount_cmb.currentText()
            quantity=dlg9.quantity_le.text()

            value=calculate_value_add_invoice(unit_price,quantity,discount)
            subtotal = float(dlg9.subtotal_rs_lbl.text())
            subtotal+=float(quantity)*float(unit_price)
            subtotal=round(subtotal,2)
            dlg9.subtotal_rs_lbl.setText(str(subtotal))
            disc=float(dlg9.discount_rs_lbl.text())
            disc+=float(quantity)*float(unit_price)*float(discount)/100
            disc=round(disc,2)
            dlg9.discount_rs_lbl.setText(str(disc))
            shipping_cost=float(dlg9.shipping_packaging_cost_lbl.text())
            total=subtotal-disc+shipping_cost
            total=round(total,2)
            dlg9.total_cost_lbl.setText(str(total))
            result=helper.select("Select prd_hsn from productservicetest2 where prd_id="+str(id))

            for row in range(1):
                dlg9.table_tw.insertRow(row)
                cell0 = QtWidgets.QTableWidgetItem(str(countz+1))
                cell1 = QtWidgets.QTableWidgetItem(str(product_name))
                cell2 = QtWidgets.QTableWidgetItem(str(result[0][0]))
                cell3 = QtWidgets.QTableWidgetItem(str(description))
                cell4 = QtWidgets.QTableWidgetItem(str(uom))
                cell5 = QtWidgets.QTableWidgetItem(str(quantity))
                cell6 = QtWidgets.QTableWidgetItem(str(unit_price))
                cell7 = QtWidgets.QTableWidgetItem(str(value))
                cell8 = QtWidgets.QTableWidgetItem(str(discount))
                cell9 = QtWidgets.QTableWidgetItem(str('00.00'))
                cell10 = QtWidgets.QTableWidgetItem(str('00.00'))
                cell11 = QtWidgets.QTableWidgetItem(str('00.00'))
                #lst=[str(product_name),str(result[0][0]),str(description),str(uom),str(quantity),str(unit_price),str(value),str(discount),str('00.00'),str('00.00'),str('00.00')]

                dlg9.table_tw.setItem(row, 0, cell0)
                dlg9.table_tw.setItem(row, 1, cell1)
                dlg9.table_tw.setItem(row, 2, cell2)
                dlg9.table_tw.setItem(row, 3, cell3)
                dlg9.table_tw.setItem(row, 4, cell4)
                dlg9.table_tw.setItem(row, 5, cell5)
                dlg9.table_tw.setItem(row, 6, cell6)
                dlg9.table_tw.setItem(row, 7, cell7)
                dlg9.table_tw.setItem(row, 8, cell8)
                dlg9.table_tw.setItem(row, 9, cell9)
                dlg9.table_tw.setItem(row, 10, cell10)
                dlg9.table_tw.setItem(row, 11, cell11)

                # btn1 = QtWidgets.QPushButton()
                # btn1.setIcon(edit64)
                # btn1.setIconSize(QSize(30, 30))
                btn1 = QtWidgets.QPushButton()
                btn1.setIcon(delete64)
                btn1.setIconSize(QSize(30, 30))
                #dlg9.table_tw.setCellWidget(row, 11, btn1)
                dlg9.table_tw.setCellWidget(row, 12, btn1)
                #btn1.clicked.connect(partial(add_invoice_update, action=lst))
                btn1.clicked.connect(partial(add_invoice_delete, action=row))
            countz+=1
            add_invoice_clear()

    except Exception as e:
        print(e)


def add_invoice_delete(action):
    print("Hello delete: "+str(action))
    try:
        dlg6.show()
        rsp=dlg6.exec_()
        if rsp == QtWidgets.QDialog.Accepted:
            helper.delete("Delete from productservicetest2 where prd_id="+str(action))
            clearData()
            loadData()
        else:
            dlg6.close()
    except Exception as e:
        print("Delete:"+str(e))



# def add_invoice_update(action):
#     print("Hello update: "+str(action))
#     dlg10.product_service_le.setText(action[0])
#     dlg10.hsn_sac_le.setText(action[1])
#     dlg10.description_le.setText(action[2])
#     dlg10.uom_le.setText(action[3])
#     dlg10.quantity_le.setText(action[4])
#     dlg10.unit_price_le.setText(action[5])
#     dlg10.value_le.setText(action[6])
#     dlg10.discount_le.setText(action[7])
#     dlg10.cgst_le.setText(action[8])
#     dlg10.sgst_le.setText(action[9])
#     dlg10.igst_le.setText(action[10])
#     dlg10.show()

# def update_invoice():
#     print("HOLA")

    # for i in range(13):
    #     dlg9.table_tw.setItem(0,i,cell)
    # users = helper.select("SELECT * FROM companytest3 ORDER BY comp_id ASC")
    #
    # for row_number,user in enumerate(users):
    #     dlg9.table_tw.insertRow(row_number)
    #     for column_number,data in enumerate(user):
    #         cell = QtWidgets.QTableWidgetItem(str(data))
    #         dlg.tableWidget_2.setItem(row_number,column_number,cell)

def add_invoice_clear():
    dlg9.cust_name_cmb.setCurrentIndex(0)
    dlg9.product_cmb.setCurrentIndex(0)
    dlg9.quantity_le.clear()
    # dlg9.description_le.clear()
    # dlg9.unit_price_le.clear()
    # dlg9.tax_cmb.clear()
    # dlg9.place_le.clear()
    # dlg9.address_te.clear()

def calculate_value_add_invoice(unit_price,quantity,discount):
    unit_price=float(unit_price)
    quantity=float(quantity)
    discount=float(discount)
    mul1=unit_price*quantity
    mul2=mul1-(mul1*discount/100)
    return mul2


dlg.actionAdd_Invoice.triggered.connect(add_invoice_cmb)
dlg.actionManage_Product_Services.triggered.connect(menu_product_service)
dlg.actionManage_Company.triggered.connect(menu_company)
dlg.actionManage_Customer.triggered.connect(menu_customer)
dlg2.pushButton_5.clicked.connect(add_company)
dlg2.pushButton.clicked.connect(image_logo)
dlg2.pushButton_3.clicked.connect(image_signature)
dlg2.pushButton_2.clicked.connect(remove_logo)
dlg2.pushButton_4.clicked.connect(remove_signature)
dlg4.pushButton_6.clicked.connect(image_product_service)
dlg4.pushButton_7.clicked.connect(remove_product_service)
dlg3.pushButton_6.clicked.connect(image_customer)
dlg3.pushButton_7.clicked.connect(remove_customer)
dlg3.pushButton_5.clicked.connect(add_customer)
dlg4.pushButton_5.clicked.connect(add_product_service)
dlg5.pushButton_5.clicked.connect(update_product_service)
dlg5.pushButton_6.clicked.connect(image_update_product_service)
dlg5.pushButton_7.clicked.connect(remove_update_product_service)
dlg7.pushButton_5.clicked.connect(update_company)
dlg7.pushButton.clicked.connect(image_update_logo)
dlg7.pushButton_3.clicked.connect(image_update_signature)
dlg7.pushButton_2.clicked.connect(remove_update_logo)
dlg7.pushButton_4.clicked.connect(remove_update_signature)
dlg8.pushButton_5.clicked.connect(update_customer)
dlg8.pushButton_6.clicked.connect(image_update_customer)
dlg9.cust_name_cmb.currentTextChanged.connect(invoice_cust_name)
dlg9.product_cmb.currentTextChanged.connect(invoice_product)
dlg9.add_pb.clicked.connect(add_invoice_table_widget)
#dlg10.update_invoice_pb.clicked.connect(update_invoice)




if __name__=="__main__":
    global countz
    countz = 0
    #dlg.setWindowFlags(Qt.FramelessWindowHint)
    subprocess.call([r'..\pgsql\bin\startserver.bat'])
    splash_pix = QPixmap('splash.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
    splash.setEnabled(False)
    progressBar = QProgressBar(splash)
    progressBar.setMaximum(10)
    progressBar.setGeometry(0, splash_pix.height() - 50, splash_pix.width(), 20)
    splash.show()
    #splash.showMessage("<h1><font color='green'>Welcome!</font></h1>", Qt.AlignTop | Qt.AlignCenter, Qt.black)

    for i in range(1, 11):
        progressBar.setValue(i)
        #time.sleep(0.2)
        t = time.time()
        while time.time() < t + 0.1:
            app.processEvents()


desktopRect = QApplication.desktop().availableGeometry(dlg)
center = desktopRect.center()
dlg.move(center.x()-dlg.width()  * 0.5,
                 center.y()-dlg.height() * 0.5)




helper = PostgresHelper("postgres")
loadData()
loadData_Company()
loadData_Customer()
dlg.tableWidget.close()
dlg.tableWidget_2.close()
dlg.tableWidget_3.close()
dlg.show()
#dlg2.show()
splash.finish(dlg)
app.exec()