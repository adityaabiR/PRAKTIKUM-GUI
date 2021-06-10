from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(827, 479)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(330, 80, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.namaEdit = QtWidgets.QLineEdit(Form)
        self.namaEdit.setGeometry(QtCore.QRect(260, 120, 301, 20))
        self.namaEdit.setObjectName("namaEdit")
        self.clear = QtWidgets.QPushButton(Form)
        self.clear.setGeometry(QtCore.QRect(440, 200, 156, 23))
        self.clear.setObjectName("clear")
        self.clear.clicked.connect(self.namaEdit.clear)
        self.keluar = QtWidgets.QPushButton(Form)
        self.keluar.setGeometry(QtCore.QRect(330, 270, 156, 23))
        self.keluar.setObjectName("keluar")
        self.keluar.clicked.connect(Form.close)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(210, 200, 158, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.hallo = QtWidgets.QPushButton(self.widget)
        self.hallo.setObjectName("hallo")
        self.horizontalLayout.addWidget(self.hallo)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Masukan Nama Anda"))
        self.clear.setText(_translate("Form", "Clear"))
        self.keluar.setText(_translate("Form", "Keluar"))
        self.hallo.setText(_translate("Form", "Hallo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())