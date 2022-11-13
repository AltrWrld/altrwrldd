import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import math as ntp


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(299, 489)
        MainWindow.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AC = QtWidgets.QPushButton(self.centralwidget)
        self.AC.setGeometry(QtCore.QRect(10, 120, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.AC.setFont(font)
        self.AC.setStyleSheet("border-radius: 30px; \n"
"background-color: rgb(0, 0, 0);\n"
"color: white;  ")
        self.AC.setObjectName("AC")
        self.delete = QtWidgets.QPushButton(self.centralwidget)
        self.delete.setGeometry(QtCore.QRect(150, 120, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.delete.setFont(font)
        self.delete.setStyleSheet("border-radius: 30px; \n"
"background-color: rgb(0, 0, 0);\n"
"color: white;  ")
        self.delete.setObjectName("delete")
        self.plus_minus = QtWidgets.QPushButton(self.centralwidget)
        self.plus_minus.setGeometry(QtCore.QRect(80, 120, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.plus_minus.setFont(font)
        self.plus_minus.setStyleSheet("border-radius: 30px; \n"
"background-color: rgb(0, 0, 0);\n"
"color: white;  ")
        self.plus_minus.setObjectName("plus_minus")
        self.divide = QtWidgets.QPushButton(self.centralwidget)
        self.divide.setGeometry(QtCore.QRect(220, 120, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.divide.setFont(font)
        self.divide.setStyleSheet("border-radius: 30px; \n"
"background-color: rgb(0, 0, 0);\n"
"color: white;  ")
        self.divide.setObjectName("divide")
        self.multiply = QtWidgets.QPushButton(self.centralwidget)
        self.multiply.setGeometry(QtCore.QRect(220, 190, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.multiply.setFont(font)
        self.multiply.setStyleSheet("border-radius: 30px; \n"
"background-color: rgb(0, 0, 0);\n"
"color: white;  ")
        self.multiply.setObjectName("multiply")
        self.minus = QtWidgets.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(220, 260, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.minus.setFont(font)
        self.minus.setStyleSheet("border-radius: 30px; \n"
"background-color: rgb(0, 0, 0);\n"
"color: white;  ")
        self.minus.setObjectName("minus")
        self.plus = QtWidgets.QPushButton(self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(220, 330, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.plus.setFont(font)
        self.plus.setStyleSheet("border-radius: 30px; \n"
"background-color: rgb(0, 0, 0);\n"
"color: white;  ")
        self.plus.setObjectName("plus")
        self.rovno = QtWidgets.QPushButton(self.centralwidget)
        self.rovno.setGeometry(QtCore.QRect(220, 400, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.rovno.setFont(font)
        self.rovno.setStyleSheet("border-radius: 30px; \n"
"background-color: rgb(0, 0, 0);\n"
"color: white;  ")
        self.rovno.setObjectName("rovno")
        self.seven = QtWidgets.QPushButton(self.centralwidget)
        self.seven.setGeometry(QtCore.QRect(10, 190, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.seven.setFont(font)
        self.seven.setStyleSheet("border-radius: 30px; \n"
"background-color: rgb(0, 0, 0);\n"
"color: white;  ")
        self.seven.setObjectName("seven")
        self.eight = QtWidgets.QPushButton(self.centralwidget)
        self.eight.setGeometry(QtCore.QRect(80, 190, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.eight.setFont(font)
        self.eight.setStyleSheet("border-radius: 30px; \n"
"background-color: rgb(0, 0, 0);\n"
"color: white;  ")
        self.eight.setObjectName("eight")
        self.nine = QtWidgets.QPushButton(self.centralwidget)
        self.nine.setGeometry(QtCore.QRect(150, 190, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.nine.setFont(font)
        self.nine.setStyleSheet("border-radius: 30px; \n"
"background-color: rgb(0, 0, 0);\n"
"color: white;  ")
        self.nine.setObjectName("nine")
        self.five = QtWidgets.QPushButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(80, 260, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.five.setFont(font)
        self.five.setStyleSheet("border-radius: 30px; \n"
"background-color: rgb(0, 0, 0);\n"
"color: white;  ")
        self.five.setObjectName("five")
        self.four = QtWidgets.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(10, 260, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.four.setFont(font)
        self.four.setStyleSheet("border-radius: 30px; \n"
"background-color: rgb(0, 0, 0);\n"
"color: white;  ")
        self.four.setObjectName("four")
        self.six = QtWidgets.QPushButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(150, 260, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.six.setFont(font)
        self.six.setStyleSheet("border-radius: 30px; \n"
"background-color: rgb(0, 0, 0);\n"
"color: white;  ")
        self.six.setObjectName("six")
        self.three = QtWidgets.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(150, 330, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.three.setFont(font)
        self.three.setStyleSheet("border-radius: 30px; \n"
"background-color: rgb(0, 0, 0);\n"
"color: white;  ")
        self.three.setObjectName("three")
        self.two = QtWidgets.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(80, 330, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.two.setFont(font)
        self.two.setStyleSheet("border-radius: 30px; \n"
"background-color: rgb(0, 0, 0);\n"
"color: white;  ")
        self.two.setObjectName("two")
        self.one = QtWidgets.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(10, 330, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.one.setFont(font)
        self.one.setStyleSheet("border-radius: 30px; \n"
"background-color: rgb(0, 0, 0);\n"
"color: white;  ")
        self.one.setObjectName("one")
        self.comma = QtWidgets.QPushButton(self.centralwidget)
        self.comma.setGeometry(QtCore.QRect(150, 400, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.comma.setFont(font)
        self.comma.setStyleSheet("border-radius: 30px; \n"
"background-color: rgb(0, 0, 0);\n"
"color: white;  ")
        self.comma.setObjectName("comma")
        self.zero = QtWidgets.QPushButton(self.centralwidget)
        self.zero.setGeometry(QtCore.QRect(10, 400, 131, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.zero.setFont(font)
        self.zero.setStyleSheet("border-radius: 30px; \n"
"background-color: rgb(0, 0, 0);\n"
"color: white;  ")
        self.zero.setObjectName("zero")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 281, 101))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.AC.setText(_translate("MainWindow", "AC"))
        self.plus_minus.setText(_translate("MainWindow", "+/-"))
        self.delete.setText(_translate("MainWindow", "<"))
        self.divide.setText(_translate("MainWindow", "/"))
        self.multiply.setText(_translate("MainWindow", "*"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.rovno.setText(_translate("MainWindow", "="))
        self.seven.setText(_translate("MainWindow", "7"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.five.setText(_translate("MainWindow", "5"))
        self.four.setText(_translate("MainWindow", "4"))
        self.six.setText(_translate("MainWindow", "6"))
        self.three.setText(_translate("MainWindow", "3"))
        self.two.setText(_translate("MainWindow", "2"))
        self.one.setText(_translate("MainWindow", "1"))
        self.comma.setText(_translate("MainWindow", "."))
        self.zero.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", ""))
class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.rovno.clicked.connect(self.Equere)
        self.ui.zero.clicked.connect(lambda: self.NumBut(0))
        self.ui.one.clicked.connect(lambda: self.NumBut(1))
        self.ui.two.clicked.connect(lambda: self.NumBut(2))
        self.ui.three.clicked.connect(lambda: self.NumBut(3))
        self.ui.four.clicked.connect(lambda: self.NumBut(4))
        self.ui.five.clicked.connect(lambda: self.NumBut(5))
        self.ui.six.clicked.connect(lambda: self.NumBut(6))
        self.ui.seven.clicked.connect(lambda: self.NumBut(7))
        self.ui.eight.clicked.connect(lambda: self.NumBut(8))
        self.ui.nine.clicked.connect(lambda: self.NumBut(9))
        self.ui.AC.clicked.connect(self.Clear)
        self.ui.delete.clicked.connect(self.Delete)
        self.ui.minus.clicked.connect(lambda: self.NumBut("-"))
        self.ui.plus.clicked.connect(lambda: self.NumBut("+"))
        self.ui.divide.clicked.connect(lambda: self.NumBut("/"))
        self.ui.multiply.clicked.connect(lambda: self.NumBut("*"))
        self.ui.comma.clicked.connect(lambda: self.NumBut("."))

    def Equere(self):
        min="-"
        plus = "+"
        splitt = "/"
        mn = "*"
        Compare = self.ui.label.text()
        if "-" in Compare:
            s = Compare.split("-")
            n = float(s[0])
            nl = float(s[1])
            f = float(n - nl)
            self.ui.label.setText(str(f))
        if plus in Compare:
            s = Compare.split("+")
            n = float(s[0])
            nl = float(s[1])
            f = float(n + nl)
            self.ui.label.setText(str(f))
        if splitt in Compare:
            s = Compare.split("/")
            n = float(s[0])
            nl = float(s[1])
            f = float(n / nl)
            self.ui.label.setText(str(f))

        if mn in Compare:
            s = Compare.split("*")
            n = float(s[0])
            nl = float(s[1])
            f = float(n * nl)
            self.ui.label.setText(str(f))
        #self.ui.label.clear()
        self.ui.label.setText(self.ui.label.text())





    def Clear(self):
            self.ui.label.clear()

    def NumBut(self,num):
        v = str(num)
        self.ui.label.setText(self.ui.label.text()+v)

    def Delete(self):
        a = self.ui.label.text()
        a = a[:-1]
        self.ui.label.setText(a)


app = QtWidgets.QApplication([])
applicatin = Window()
applicatin.show()
sys.exit(app.exec())
