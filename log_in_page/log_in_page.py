# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Log_in_modern1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from ast import If, Str
from distutils import command
from distutils.command.build_scripts import first_line_re
from email.policy import default
from faulthandler import disable
from tabnanny import check
from tkinter import DISABLED
from PyQt5 import QtCore, QtGui, QtWidgets
from numpy import empty
import pymysql as db
from PyQt5.QtWidgets import *


try:
#     mydb = db.connect(host="127.0.0.1", user="root", password="35955501100",database= 'arvin')
    mydb = db.connect(host="127.0.0.1", user="root", password="35955501100",database= 'arvin')
    print('Connected')
except:
    print('Not connected')
    
try:
        mycursor = mydb.cursor()
        query = "CREATE TABLE IF NOT EXISTS `arvin`.`info_list` (`id` INT NOT NULL AUTO_INCREMENT,`user_name` VARCHAR(45) NOT NULL,`password` VARCHAR(45) NOT NULL, PRIMARY KEY (`id`),UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,UNIQUE INDEX `user_name_UNIQUE` (`user_name` ASC) VISIBLE);"
        #query= "CREATE TABLE IF NOT EXISTS `arvin`.`info_list` (`id` INT NOT NULL AUTO_INCREMENT,`user_name` VARCHAR(12) NOT NULL,`password` VARCHAR(18) NOT NULL,PRIMARY KEY (`id`),UNIQUE INDEX `user_name_UNIQUE` (`user_name` ASC) VISIBLE);"
        mycursor.execute(query)
        print("Done!")
except:
        print ("Not Done!")
 




        




class Ui_Form(object):
                
     
    
#     def show_info_messagebox(self):
#         msg = QMessageBox()
#         msg.setIcon(QMessageBox.Information)
  
    
#         msg.setText("Your Account Created Successfully")
     
#         msg.setWindowTitle("Success")
      
#     # declaring buttons on Message Box
#         msg.setStandardButtons(QMessageBox.Ok )
#         retval = msg.exec_()
            
        
        
    def confirm(self,mycurser):
            
        #     if len (self.user_name_et_rigester_pg) == 0:
        #             msg=QMessageBox
        #             msg.setIcon(QMessageBox.Information)
        #             msg.setText("User name not set!")
        #             msg.setWindowTitle("Failed")
        #             msg.setStandardButtons(QMessageBox.Ok )
        #             retval = msg.exec_()
        #             disable(self.query)
            
                    temp_text1 = self.user_name_et_rigester_pg.text()
                    temp_text2 = self.password_et_rigister_pg.text()
                    self.mydb  = db.connect (host="127.0.0.1", user="root", password="35955501100",database= 'arvin')                    
                    self.query = "INSERT INTO `arvin`.`info_list` (`user_name`,`password`) VALUES (%s, %s); "
                    mycurser.execute(self.query, (temp_text1, temp_text2))
                    mydb.commit()
                    
            
            
        
            
        
    def method1(self):
            if self.rigister_btn.clicked:
                    self.rigister_label.show()
                    self.user_name_et_rigester_pg.show()
                    self.password_et_rigister_pg.show()
                    self.rigister_btn_rigister_pg.show()
                    self.back_to_login_btn.show()
                    self.welcome_label.hide()
                    self.user_name_et.hide()
                    self.password_et.hide()
                    
    def method2(self):
            if self.back_to_login_btn.clicked:
                    self.welcome_label.show()
                    self.user_name_et.show()
                    self.password_et.show()
                    self.log_in_btn.show()
                    self.rigister_btn.show()
                    self.rigister_label.hide()
                    self.user_name_et_rigester_pg.hide()
                    self.password_et_rigister_pg.hide()
                    self.rigister_btn_rigister_pg.hide()
                    self.back_to_login_btn.hide()
                    
        
     
                    
        
                    
                    
               
        

                
                
                        
                        
                  
                        
            
                   
            
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(716, 540)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-10, 0, 731, 551))
        self.widget.setStyleSheet("background-color: rgb(0, 170, 127);\n"

        
"")
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(70, 40, 291, 431))
        self.label_2.setStyleSheet("image: url(:/images/6.jpg);\n"
"")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("6.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(350, 40, 291, 431))
        self.label.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius: 50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.welcome_label = QtWidgets.QLabel(self.widget)
        self.welcome_label.setGeometry(QtCore.QRect(410, 80, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.welcome_label.setFont(font)
        self.welcome_label.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.welcome_label.setObjectName("welcome_label")
        self.user_name_et = QtWidgets.QLineEdit(self.widget)
        self.user_name_et.setGeometry(QtCore.QRect(390, 200, 221, 41))
        self.user_name_et.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.user_name_et.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.user_name_et.setObjectName("user_name_et")
        self.password_et = QtWidgets.QLineEdit(self.widget)
        self.password_et.setGeometry(QtCore.QRect(390, 280, 221, 41))
        self.password_et.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.password_et.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.password_et.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_et.setObjectName("password_et")
        self.log_in_btn = QtWidgets.QPushButton(self.widget)
        self.log_in_btn.setGeometry(QtCore.QRect(400, 340, 190, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.log_in_btn.setFont(font)
        self.log_in_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.log_in_btn.setStyleSheet("\n"
"border-radius:10px;\n"
"\n"
"background-color: rgb(0, 255, 127);")
        self.log_in_btn.setObjectName("log_in_btn")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(70, 70, 271, 91))
        self.label_5.setStyleSheet("background-color:rgba(0, 0, 0, 75);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(80, 120, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:rgba(0, 0, 0, 75);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(80, 70, 131, 40))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgba(255, 255, 255, 200);\n"
"background-color:rgba(0, 0, 0, 75);")
        self.label_8.setObjectName("label_8")
        self.forgot_pass_btn = QtWidgets.QPushButton(self.widget)
        self.forgot_pass_btn.setGeometry(QtCore.QRect(410, 440, 171, 23))
        self.forgot_pass_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.forgot_pass_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.forgot_pass_btn.setCheckable(False)
        self.forgot_pass_btn.setFlat(True)
        self.forgot_pass_btn.setObjectName("forgot_pass_btn")
        self.rigister_btn = QtWidgets.QPushButton(self.widget)
        self.rigister_btn.setGeometry(QtCore.QRect(400, 390, 190, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rigister_btn.setFont(font)
        self.rigister_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rigister_btn.setStyleSheet("\n"
"border-radius:10px;\n"
"\n"
"background-color: rgb(0, 255, 127);")
        self.rigister_btn.setObjectName("rigister_btn")
        self.user_name_et_rigester_pg = QtWidgets.QLineEdit(self.widget)
        self.user_name_et_rigester_pg.setGeometry(QtCore.QRect(390, 200, 221, 41))
        self.user_name_et_rigester_pg.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.user_name_et_rigester_pg.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.user_name_et_rigester_pg.setObjectName("user_name_et_rigester_pg")
        self.password_et_rigister_pg = QtWidgets.QLineEdit(self.widget)
        self.password_et_rigister_pg.setGeometry(QtCore.QRect(390, 280, 221, 41))
        self.password_et_rigister_pg.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.password_et_rigister_pg.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.password_et_rigister_pg.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_et_rigister_pg.setObjectName("password_et_rigister_pg")
        self.rigister_btn_rigister_pg = QtWidgets.QPushButton(self.widget)
        self.rigister_btn_rigister_pg.setGeometry(QtCore.QRect(400, 340, 190, 40))
        
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rigister_btn_rigister_pg.setFont(font)
        self.rigister_btn_rigister_pg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rigister_btn.clicked.connect(self.method1)
        self.rigister_btn_rigister_pg.setStyleSheet("\n"
"border-radius:10px;\n"
"\n"
"background-color: rgb(0, 255, 127);")
        self.rigister_btn_rigister_pg.setObjectName("rigister_btn_rigister_pg")
        
        self.back_to_login_btn = QtWidgets.QPushButton(self.widget)
        self.back_to_login_btn.clicked.connect(self.method2)
        self.back_to_login_btn.setGeometry(QtCore.QRect(400, 390, 190, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.back_to_login_btn.setFont(font)
        self.back_to_login_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_to_login_btn.setStyleSheet("\n"
"border-radius:10px;\n"
"\n"
"background-color: rgb(0, 255, 127);")
        self.back_to_login_btn.setObjectName("back_to_login_btn")
        self.rigister_label = QtWidgets.QLabel(self.widget)
        self.rigister_label.setGeometry(QtCore.QRect(410, 80, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.rigister_label.setFont(font)
        self.rigister_label.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.rigister_label.setObjectName("rigister_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.rigister_label.hide()
        self.user_name_et_rigester_pg.hide()      
        self.password_et_rigister_pg.hide()
        self.rigister_btn_rigister_pg.hide()
        self.back_to_login_btn.hide()
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.welcome_label.setText(_translate("Form", "Welcome"))
        self.user_name_et.setPlaceholderText(_translate("Form", "User name"))
        self.password_et.setPlaceholderText(_translate("Form", "Password"))
        self.log_in_btn.setText(_translate("Form", "Log in "))
        self.label_7.setText(_translate("Form", " This is my Log in page and i hope you enjoy "))
        self.label_8.setText(_translate("Form", "arvin.afz"))
        self.forgot_pass_btn.setText(_translate("Form", "Forgot your password ?"))
        self.rigister_btn.setText(_translate("Form", "Rigister"))
        self.user_name_et_rigester_pg.setPlaceholderText(_translate("Form", "User name"))
        self.password_et_rigister_pg.setPlaceholderText(_translate("Form", "Password"))
        self.rigister_btn_rigister_pg.setText(_translate("Form", "Rigister"))
        self.back_to_login_btn.setText(_translate("Form", "Back to Log in "))
        self.rigister_label.setText(_translate("Form", " Rigister"))
        self.rigister_btn.clicked.connect(self.method1)
        self.rigister_btn_rigister_pg.clicked.connect(lambda:self.confirm(mycursor))
        
        # if len(self.user_name_et_rigester_pg.text()) == 0:
        #                 msg=QMessageBox
        #                 msg.setIcon(QMessageBox.Critical)
        #                 msg.setText("User name not set!")
        #                 msg.setWindowTitle("Failed")
        #                 msg.setStandardButtons(QMessageBox.Ok )
        #                 retval = msg.exec_()
        #                 disable(self.query)
        
        
        
        
       #self.rigister_btn_rigister_pg.clicked.connect(self.show_info_messagebox)
        
#         if self.user_name_et_rigester_pg is empty:
#                 msg1=QMessageBox() 
#                 msg1.setIcon(QMessageBox.Information)
  
    
#         msg1.setText("Username box is empty")
     
#         msg1.setWindowTitle("Failed")
      
#     # declaring buttons on Message Box
#         msg1.setStandardButtons(QMessageBox.Ok )
#         retval = msg1.exec_()
                
                
        
      




      
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
