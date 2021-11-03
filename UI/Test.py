from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import pandas as pd
class Ui_JobSearchPortal(object):
    def setupUi(self, JobSearchPortal):
        JobSearchPortal.setObjectName("JobSearchPortal")
        JobSearchPortal.resize(1201, 612)
        self.frame = QtWidgets.QFrame(JobSearchPortal)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 1221, 621))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("background-color: rgb(230, 231, 232);\n"
"this->statusbar()->setVisible(false);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1221, 21))
        self.frame_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"\n"
"background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(20, 0, 21, 21))
        self.label.setStyleSheet("image: url(:/newPrefix/360_degrees_25px.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(50, 0, 21, 21))
        self.label_2.setStyleSheet("image: url(:/newPrefix/yellow.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(80, 0, 31, 21))
        self.label_3.setStyleSheet("image: url(:/newPrefix/green.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(950, 30, 251, 571))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setStyleSheet("color: rgb(241, 45, 19);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 0px solid white;\n"
"border-radius: 35px;\n"
"\n"
"\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setGeometry(QtCore.QRect(10, 10, 141, 101))
        self.widget_5.setStyleSheet("background-color: rgb(243, 51, 37);\n"
"border: 0px solid white;\n"
"border-radius: 35px;\n"
"")
        self.widget_5.setObjectName("widget_5")
        self.label_9 = QtWidgets.QLabel(self.widget_5)
        self.label_9.setGeometry(QtCore.QRect(10, 0, 121, 101))
        self.label_9.setStyleSheet("image: url(:/newPrefix/alg.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(160, 10, 41, 41))
        self.label_4.setStyleSheet("image: url(:/newPrefix/settings_30px.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(20, 120, 141, 20))
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"color: rgb(121, 121, 121);\n"
"font: 87 8pt \"Arial Black\";")
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setGeometry(QtCore.QRect(20, 140, 171, 21))
        self.comboBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"color: rgb(121, 121, 121);\n"
"font: 7pt \"MS Shell Dlg 2\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setGeometry(QtCore.QRect(160, 50, 41, 21))
        self.label_7.setStyleSheet("image: url(:/newPrefix/share_30px.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_10 = QtWidgets.QLabel(self.widget_2)
        self.label_10.setGeometry(QtCore.QRect(160, 80, 41, 31))
        self.label_10.setStyleSheet("image: url(:/newPrefix/plus_+_30px.png);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 3px solid white;\n"
"border-radius: 35px;\n"
"\n"
"")
        self.widget_3.setObjectName("widget_3")
        self.widget_7 = QtWidgets.QWidget(self.widget_3)
        self.widget_7.setGeometry(QtCore.QRect(10, 10, 141, 101))
        self.widget_7.setStyleSheet("background-color: rgb(249, 233, 1);\n"
"border: 0px solid white;\n"
"border-radius: 35px;\n"
"")
        self.widget_7.setObjectName("widget_7")
        self.label_12 = QtWidgets.QLabel(self.widget_7)
        self.label_12.setGeometry(QtCore.QRect(10, 0, 111, 101))
        self.label_12.setStyleSheet("image: url(:/newPrefix/sort.png);")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.widget_3)
        self.label_13.setGeometry(QtCore.QRect(10, 120, 161, 21))
        self.label_13.setStyleSheet("color: rgb(0, 0, 0);\n"
"color: rgb(121, 121, 121);\n"
"font: 87 8pt \"Arial Black\";")
        self.label_13.setObjectName("label_13")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget_3)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 140, 171, 21))
        self.comboBox_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"color: rgb(121, 121, 121);\n"
"font: 7pt \"MS Shell Dlg 2\";")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_14 = QtWidgets.QLabel(self.widget_3)
        self.label_14.setGeometry(QtCore.QRect(160, 10, 47, 41))
        self.label_14.setStyleSheet("image: url(:/newPrefix/settings_yellow.png);")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.widget_3)
        self.label_15.setGeometry(QtCore.QRect(160, 50, 41, 31))
        self.label_15.setStyleSheet("image: url(:/newPrefix/share_ok.png);")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.widget_3)
        self.label_16.setGeometry(QtCore.QRect(150, 80, 61, 41))
        self.label_16.setStyleSheet("image: url(:/newPrefix/plus_+_y.png);")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 3px solid white;\n"
"border-radius: 35px;\n"
"\n"
"")
        self.widget_4.setObjectName("widget_4")
        self.widget_6 = QtWidgets.QWidget(self.widget_4)
        self.widget_6.setGeometry(QtCore.QRect(10, 10, 151, 101))
        self.widget_6.setStyleSheet("background-color: rgb(51, 181, 11);\n"
"border: 0px solid white;\n"
"border-radius: 35px;\n"
"")
        self.widget_6.setObjectName("widget_6")
        self.label_11 = QtWidgets.QLabel(self.widget_6)
        self.label_11.setGeometry(QtCore.QRect(10, 0, 121, 101))
        self.label_11.setStyleSheet("image: url(:/newPrefix/multicast_75px.png);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_17 = QtWidgets.QLabel(self.widget_4)
        self.label_17.setGeometry(QtCore.QRect(170, 10, 41, 41))
        self.label_17.setStyleSheet("image: url(:/newPrefix/settings_green.png);")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.widget_4)
        self.label_18.setGeometry(QtCore.QRect(170, 50, 41, 31))
        self.label_18.setStyleSheet("image: url(:/newPrefix/share_30pxgreen.png);")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.widget_4)
        self.label_19.setGeometry(QtCore.QRect(170, 80, 41, 41))
        self.label_19.setStyleSheet("image: url(:/newPrefix/plus_+_green.png);")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.widget_4)
        self.label_20.setGeometry(QtCore.QRect(10, 120, 151, 21))
        self.label_20.setStyleSheet("color: rgb(0, 0, 0);\n"
"color: rgb(121, 121, 121);\n"
"font: 87 8pt \"Arial Black\";")
        self.label_20.setObjectName("label_20")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget_4)
        self.comboBox_3.setGeometry(QtCore.QRect(20, 140, 181, 21))
        self.comboBox_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"color: rgb(121, 121, 121);\n"
"font: 7pt \"MS Shell Dlg 2\";")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.verticalLayout.addWidget(self.widget_4)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(370, 50, 391, 21))
        self.label_6.setStyleSheet("font: 75 19pt \"Arial\";\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(360, 70, 401, 20))
        self.label_8.setObjectName("label_8")
        self.widget_8 = QtWidgets.QWidget(self.frame)
        self.widget_8.setGeometry(QtCore.QRect(30, 110, 771, 101))
        self.widget_8.setStyleSheet("color: rgb(241, 45, 19);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 0px solid white;\n"
"border-radius: 35px;")
        self.widget_8.setObjectName("widget_8")
        self.progressBar = QtWidgets.QProgressBar(self.widget_8)
        self.progressBar.setGeometry(QtCore.QRect(100, 20, 651, 61))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    color: rgb(245, 0, 0);\n"
"    \n"
"background-color: rgb(220, 220, 220);\n"
"\n"
"border-style:solid;\n"
"border-radius: 30px;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}")
        self.progressBar.setProperty("value", 60)
        self.progressBar.setObjectName("progressBar")
        self.widget_9 = QtWidgets.QWidget(self.frame)
        self.widget_9.setGeometry(QtCore.QRect(30, 240, 901, 351))
        self.widget_9.setStyleSheet("color: rgb(241, 45, 19);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 0px solid white;\n"
"border-radius: 35px;")
        self.widget_9.setObjectName("widget_9")
        self.widget_12 = QtWidgets.QWidget(self.widget_9)
        self.widget_12.setGeometry(QtCore.QRect(0, 0, 901, 71))
        self.widget_12.setStyleSheet("color: rgb(241, 45, 19);\n"
"background-color: rgb(248, 39, 24);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 35px;")
        self.widget_12.setObjectName("widget_12")
        self.label_25 = QtWidgets.QLabel(self.widget_12)
        self.label_25.setGeometry(QtCore.QRect(26, 2, 31, 31))
        self.label_25.setStyleSheet("image: url(:/newPrefix/search.png);")
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_12)
        self.lineEdit.setGeometry(QtCore.QRect(60, 10, 211, 16))
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0.8px solid rgb(255, 255, 255);\n"
"border-radius: 6px")
        self.lineEdit.setObjectName("lineEdit")
        self.label_27 = QtWidgets.QLabel(self.widget_12)
        self.label_27.setGeometry(QtCore.QRect(821, 0, 20, 31))
        self.label_27.setStyleSheet("image: url(:/newPrefix/white.png);")
        self.label_27.setText("")
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.widget_12)
        self.label_28.setGeometry(QtCore.QRect(850, 0, 21, 31))
        self.label_28.setStyleSheet("image: url(:/newPrefix/white.png);")
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.widget_12)
        self.label_29.setGeometry(QtCore.QRect(791, 0, 21, 31))
        self.label_29.setStyleSheet("image: url(:/newPrefix/white.png);")
        self.label_29.setText("")
        self.label_29.setObjectName("label_29")
        self.widget_13 = QtWidgets.QWidget(self.widget_9)
        self.widget_13.setGeometry(QtCore.QRect(-31, 30, 961, 291))
        self.widget_13.setObjectName("widget_13")
        self.tableWidget = QtWidgets.QTableWidget(self.widget_13)
        self.tableWidget.setGeometry(QtCore.QRect(30, 50, 731, 231))
        self.tableWidget.setStyleSheet("color: rgb(71, 71, 71);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
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
        
        
        
        
        self.label_26 = QtWidgets.QLabel(self.widget_13)
        self.label_26.setGeometry(QtCore.QRect(67, 10, 20, 31))
        self.label_26.setStyleSheet("image: url(:/newPrefix/up_20px.png);")
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.label_30 = QtWidgets.QLabel(self.widget_13)
        self.label_30.setGeometry(QtCore.QRect(90, 10, 21, 31))
        self.label_30.setStyleSheet("image: url(:/newPrefix/dn.png);")
        self.label_30.setText("")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.widget_13)
        self.label_31.setGeometry(QtCore.QRect(160, 10, 20, 31))
        self.label_31.setStyleSheet("image: url(:/newPrefix/up_20px.png);")
        self.label_31.setText("")
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.widget_13)
        self.label_32.setGeometry(QtCore.QRect(180, 10, 21, 31))
        self.label_32.setStyleSheet("image: url(:/newPrefix/dn.png);")
        self.label_32.setText("")
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.widget_13)
        self.label_33.setGeometry(QtCore.QRect(270, 10, 20, 31))
        self.label_33.setStyleSheet("image: url(:/newPrefix/up_20px.png);")
        self.label_33.setText("")
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.widget_13)
        self.label_34.setGeometry(QtCore.QRect(290, 10, 21, 31))
        self.label_34.setStyleSheet("image: url(:/newPrefix/dn.png);")
        self.label_34.setText("")
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.widget_13)
        self.label_35.setGeometry(QtCore.QRect(370, 10, 20, 31))
        self.label_35.setStyleSheet("image: url(:/newPrefix/up_20px.png);")
        self.label_35.setText("")
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.widget_13)
        self.label_36.setGeometry(QtCore.QRect(470, 10, 20, 31))
        self.label_36.setStyleSheet("image: url(:/newPrefix/up_20px.png);")
        self.label_36.setText("")
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.widget_13)
        self.label_37.setGeometry(QtCore.QRect(560, 10, 20, 31))
        self.label_37.setStyleSheet("image: url(:/newPrefix/up_20px.png);")
        self.label_37.setText("")
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.widget_13)
        self.label_38.setGeometry(QtCore.QRect(660, 10, 20, 31))
        self.label_38.setStyleSheet("image: url(:/newPrefix/up_20px.png);")
        self.label_38.setText("")
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.widget_13)
        self.label_39.setGeometry(QtCore.QRect(390, 10, 21, 31))
        self.label_39.setStyleSheet("image: url(:/newPrefix/dn.png);")
        self.label_39.setText("")
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.widget_13)
        self.label_40.setGeometry(QtCore.QRect(490, 10, 21, 31))
        self.label_40.setStyleSheet("image: url(:/newPrefix/dn.png);")
        self.label_40.setText("")
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.widget_13)
        self.label_41.setGeometry(QtCore.QRect(580, 10, 21, 31))
        self.label_41.setStyleSheet("image: url(:/newPrefix/dn.png);")
        self.label_41.setText("")
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.widget_13)
        self.label_42.setGeometry(QtCore.QRect(680, 10, 21, 31))
        self.label_42.setStyleSheet("image: url(:/newPrefix/dn.png);")
        self.label_42.setText("")
        self.label_42.setObjectName("label_42")
        self.widget_14 = QtWidgets.QWidget(self.widget_13)
        self.widget_14.setGeometry(QtCore.QRect(779, 40, 131, 241))
        self.widget_14.setStyleSheet("color: rgb(241, 45, 19);\n"
"background-color: rgb(230, 231, 232);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 15px;\n"
"")
        self.widget_14.setObjectName("widget_14")
        self.widget_15 = QtWidgets.QWidget(self.widget_14)
        self.widget_15.setGeometry(QtCore.QRect(0, 0, 131, 31))
        self.widget_15.setStyleSheet("background-color: rgb(71, 71, 71);")
        self.widget_15.setObjectName("widget_15")
        self.widget_16 = QtWidgets.QWidget(self.widget_14)
        self.widget_16.setGeometry(QtCore.QRect(0, 210, 131, 31))
        self.widget_16.setStyleSheet("background-color: rgb(71, 71, 71);")
        self.widget_16.setObjectName("widget_16")
        self.widget_17 = QtWidgets.QWidget(self.widget_14)
        self.widget_17.setGeometry(QtCore.QRect(100, 10, 41, 221))
        self.widget_17.setStyleSheet("background-color: rgb(71, 71, 71);")
        self.widget_17.setObjectName("widget_17")
        self.widget_18 = QtWidgets.QWidget(self.widget_14)
        self.widget_18.setGeometry(QtCore.QRect(0, 0, 31, 231))
        self.widget_18.setStyleSheet("background-color: rgb(71, 71, 71);")
        self.widget_18.setObjectName("widget_18")
        self.label_43 = QtWidgets.QLabel(self.widget_14)
        self.label_43.setGeometry(QtCore.QRect(40, 90, 51, 20))
        self.label_43.setStyleSheet("color: rgb(71, 71, 71);")
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.widget_14)
        self.label_44.setGeometry(QtCore.QRect(40, 40, 47, 51))
        self.label_44.setStyleSheet("image: url(:/newPrefix/electronics_32px.png);")
        self.label_44.setText("")
        self.label_44.setObjectName("label_44")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_14)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 120, 51, 61))
        self.lineEdit_2.setStyleSheet("color: rgb(71, 71, 71);\n"
"border: 0.8px solid rgb(71, 71, 71);\n"
"border-radius: 17px")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.widget_10 = QtWidgets.QWidget(self.frame)
        self.widget_10.setGeometry(QtCore.QRect(810, 110, 121, 101))
        self.widget_10.setStyleSheet("color: rgb(241, 45, 19);\n"
"background-color: rgb(249, 105, 1);\n"
"\n"
"border: 0px solid white;\n"
"border-radius: 35px;")
        self.widget_10.setObjectName("widget_10")
        self.label_22 = QtWidgets.QLabel(self.widget_10)
        self.label_22.setGeometry(QtCore.QRect(10, 10, 31, 81))
        self.label_22.setStyleSheet("image: url(:/newPrefix/play.png);")
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.widget_10)
        self.label_23.setGeometry(QtCore.QRect(36, 0, 51, 101))
        self.label_23.setStyleSheet("image: url(:/newPrefix/pause.png);")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.widget_10)
        self.label_24.setGeometry(QtCore.QRect(80, 10, 31, 81))
        self.label_24.setStyleSheet("image: url(:/newPrefix/stop_30px.png);")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.widget_11 = QtWidgets.QWidget(self.frame)
        self.widget_11.setGeometry(QtCore.QRect(50, 130, 71, 61))
        self.widget_11.setStyleSheet("border-radius: 12px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.widget_11.setObjectName("widget_11")
        self.label_21 = QtWidgets.QLabel(self.widget_11)
        self.label_21.setGeometry(QtCore.QRect(0, 2, 71, 61))
        self.label_21.setStyleSheet("image: url(:/newPrefix/timer.png);")
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")

        self.retranslateUi(JobSearchPortal)
        QtCore.QMetaObject.connectSlotsByName(JobSearchPortal)
        
        self.label_22.mousePressEvent=self.play
        self.label_9.mousePressEvent = self.sort
        
#         JobTitle Sort
        self.label_26.mousePressEvent = self.SortJobTitle
        self.label_30.mousePressEvent = self.sortJobTitleInvert

#         Company Name Sort
        self.label_31.mousePressEvent = self.sortCompanyName
        self.label_32.mousePressEvent = self.sortCompanyNameInvert

#         KeySkills Sort
        self.label_33.mousePressEvent = self.sortKeySkills
        self.label_34.mousePressEvent = self.sortKeySkillsInvert

#       Job Experience Sort
        self.label_35.mousePressEvent = self.sortJobExp
        self.label_39.mousePressEvent = self.sortJobExpInvert
        
#       Job Location Sort
        self.label_36.mousePressEvent = self.sortJobLoc
        self.label_40.mousePressEvent = self.sortJobLocInvert

#       Job Salery Sort
        self.label_37.mousePressEvent = self.sortJobSalery
        self.label_41.mousePressEvent = self.sortJobSaleryInvert

#       Job Description Sort
        self.label_38.mousePressEvent = self.sortJobDesc
        self.label_42.mousePressEvent = self.sortJobDescInvert




        
    

    def sort(self,eve):
        print("Sorted Data")
    def play(self,eve):
        print("Play")
        self.loaddata()

    def retranslateUi(self, JobSearchPortal):
        _translate = QtCore.QCoreApplication.translate
        JobSearchPortal.setWindowTitle(_translate("JobSearchPortal", "Form"))
        self.label_5.setText(_translate("JobSearchPortal", "Select Algorithm"))
        self.comboBox.setItemText(0, _translate("JobSearchPortal", "Bubble Sort"))
        self.comboBox.setItemText(1, _translate("JobSearchPortal", "Insertion Sort"))
        self.comboBox.setItemText(2, _translate("JobSearchPortal", "Merge Sort"))
        self.comboBox.setItemText(3, _translate("JobSearchPortal", "Selection Sort"))
        self.comboBox.setItemText(4, _translate("JobSearchPortal", "Quick Sort"))
        self.comboBox.setItemText(5, _translate("JobSearchPortal", "Counting Sort"))
        self.comboBox.setItemText(6, _translate("JobSearchPortal", "Comb Sort"))
        self.comboBox.setItemText(7, _translate("JobSearchPortal", "Bucket Sort"))
        self.comboBox.setItemText(8, _translate("JobSearchPortal", "Recursive Bubble Sort"))
        self.comboBox.setItemText(9, _translate("JobSearchPortal", "Radix Sort"))
        self.comboBox.setItemText(10, _translate("JobSearchPortal", "Shell Sort"))
        self.comboBox.setItemText(11, _translate("JobSearchPortal", "Tree Sort"))
        self.comboBox.setItemText(12, _translate("JobSearchPortal", "Brick Sort"))
        self.label_13.setText(_translate("JobSearchPortal", "Sort Entities By"))
        self.comboBox_2.setItemText(0, _translate("JobSearchPortal", "Descending Salary"))
        self.comboBox_2.setItemText(1, _translate("JobSearchPortal", "Ascending Salary"))
        self.comboBox_2.setItemText(2, _translate("JobSearchPortal", "Job Location Alphabetically Descending"))
        self.comboBox_2.setItemText(3, _translate("JobSearchPortal", "Job Location Alphabetically Ascending"))
        self.comboBox_2.setItemText(4, _translate("JobSearchPortal", "Job Title Alphabetically Descending"))
        self.comboBox_2.setItemText(5, _translate("JobSearchPortal", "Job Title Alphabetically Descending"))
        self.label_20.setText(_translate("JobSearchPortal", "Add Code"))
        self.comboBox_3.setItemText(0, _translate("JobSearchPortal", "Add .txt"))
        self.label_6.setText(_translate("JobSearchPortal", "J O B   S E A R C H   P O R T A L"))
        self.label_8.setText(_translate("JobSearchPortal", "___________________________________________________________________"))
        self.lineEdit.setPlaceholderText(_translate("JobSearchPortal", "  Search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("JobSearchPortal", "Job Title"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("JobSearchPortal", "Company Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("JobSearchPortal", "Key Skills"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("JobSearchPortal", "Job Experience"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("JobSearchPortal", "Job Location"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("JobSearchPortal", "Job Salary"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("JobSearchPortal", "Job Description"))
        self.label_43.setText(_translate("JobSearchPortal", "  T I M E"))
        self.lineEdit_2.setText(_translate("JobSearchPortal", "   10 ms"))
        
    def loaddata(self):
        f = open('Salery.csv', 'r')
        reader = csv.reader(f)
        JobTitle=[]
        Company=[]
        JobLocation=[]
        JobSalary=[]
        Description=[]
        KeySkills=[]
        Experience=[]
        
        for row in reader:
            JobTitle.append(row[0])
            Company.append(row[1])
            JobLocation.append(row[2])
            JobSalary.append(row[3])
            KeySkills.append(row[5])
            Experience.append(row[6])
            Description.append(row[4])
        row=0
        self.tableWidget.setRowCount(len(JobTitle))
        for title,com,loc,sal, key, exp, des in zip(JobTitle, Company, JobLocation, JobSalary, KeySkills, Experience, Description):
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(com))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(loc))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(sal))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(key))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(exp))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(des))
            #self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(person["address"]))
            row=row+1
            
# ---------------------- Sorting Algorithms -------------------


# ------------ Insersion Sort

    def insertionSort(self,arr):
        for i in range(1, len(arr)):
            key = (arr[i])
            j = i-1
            while j >= 0 and key < (arr[j])[0] :
                    (arr[j + 1]) = (arr[j])
                    j -= 1
            (arr[j + 1]) = key
            
    def insertionSortInverse(self,arr):
        for i in range(1, len(arr)):
            key = (arr[i])
            j = i-1
            while j >= 0 and key > (arr[j])[0] :
                    (arr[j + 1]) = (arr[j])
                    j -= 1
            (arr[j + 1]) = key
    
    
    def InsertionInTable(self,arr,col):
        row = 0
        self.tableWidget.setRowCount(len(arr))
        for item in arr:
            self.tableWidget.setItem(row,col, QtWidgets.QTableWidgetItem(item))
            row+=1
            
        
#  Job Title Sort Defination
    def SortJobTitle(self,eve):
        JobTitle = pd.read_csv("Salery.csv")['Job Title']
        self.insertionSort(JobTitle)
        self.InsertionInTable(JobTitle,0)

    def sortJobTitleInvert(self,eve):
        JobTitle = pd.read_csv("Salery.csv")['Job Title']
        self.insertionSortInverse(JobTitle)
        self.InsertionInTable(JobTitle,0)

#  Company name Sort Defination
    def sortCompanyName(self,eve):
        companyName = pd.read_csv("Salery.csv")['Company Name']
        self.insertionSort(companyName)
        self.InsertionInTable(companyName,1)

    def sortCompanyNameInvert(self,eve):
        companyName = pd.read_csv("Salery.csv")['Company Name']
        self.insertionSortInverse(companyName)
        self.InsertionInTable(companyName,1)

#  Key Skills Sort Defination
    def sortKeySkills(self,eve):
        keySkils = pd.read_csv("Salery.csv")['Key Skills']
        self.insertionSort(keySkils)
        self.InsertionInTable(keySkils,2)
    
    def sortKeySkillsInvert(self,eve):
        keySkils = pd.read_csv("Salery.csv")['Key Skills']
        self.insertionSortInverse(keySkils)
        self.InsertionInTable(keySkils,2)

#  Job Experience Definition
    def sortJobExp(self,eve):
        jobExp = pd.read_csv("Salery.csv")['Experience']
        self.insertionSort(jobExp)
        self.InsertionInTable(jobExp,3)

    def sortJobExpInvert(self,eve):
        jobExp = pd.read_csv("Salery.csv")['Experience']
        self.insertionSortInverse(jobExp)
        self.InsertionInTable(jobExp,3)

#  Job Loction Defination
    def sortJobLoc(self,eve):
        jobLoc = pd.read_csv("Salery.csv")['Job Location']
        self.insertionSort(jobLoc)
        self.InsertionInTable(jobLoc,4)

    def sortJobLocInvert(self,eve):
        jobLoc = pd.read_csv("Salery.csv")['Job Location']
        self.insertionSortInverse(jobLoc)
        self.InsertionInTable(jobLoc,4)

#  Job Salery Defination

    def sortJobSalery(self,eve):
        jobSalery = pd.read_csv("Salery.csv")['Job Salery']
        self.insertionSort(jobSalery)
        self.InsertionInTable(jobSalery,5)

    def sortJobSaleryInvert(self,eve):
        jobSalery = pd.read_csv("Salery.csv")['Job Salery']
        self.insertionSortInverse(jobSalery)
        self.InsertionInTable(jobSalery,5)

#  Job Description Defination
    def sortJobDesc(self,eve):
        jobDesc = pd.read_csv("Salery.csv")['Job Description']
        self.insertionSort(jobDesc)
        self.InsertionInTable(jobDesc,6)

    def sortJobDescInvert(self,eve):
        jobDesc = pd.read_csv("Salery.csv")['Job Description']
        self.insertionSortInverse(jobDesc)
        self.InsertionInTable(jobDesc,6)


        

import Ok

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JobSearchPortal = QtWidgets.QWidget()
    ui = Ui_JobSearchPortal()
    ui.setupUi(JobSearchPortal)
    JobSearchPortal.show()
    sys.exit(app.exec_())
