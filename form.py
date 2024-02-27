from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 800)
        MainWindow.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.token = QtWidgets.QTextEdit(MainWindow)
        self.token.setGeometry(QtCore.QRect(10, 90, 581, 31))
        self.token.setStyleSheet("background: #C4C4C4;border-radius: 10px;font-family: Sitara;font-style: normal;font-weight: normal;font-size: 18px;line-height: 29px;color: #000000;")
        self.token.setObjectName("token")
        self.token_text = QtWidgets.QLabel(MainWindow)
        self.token_text.setGeometry(QtCore.QRect(10, 60, 110, 30))
        self.token_text.setStyleSheet("font-family: Sitara;font-style: normal;font-weight: normal;font-size: 18px;line-height: 29px;color: #FFFFFF;")
        self.token_text.setObjectName("token_text")
        self.channel_id_text = QtWidgets.QLabel(MainWindow)
        self.channel_id_text.setGeometry(QtCore.QRect(10, 130, 110, 30))
        self.channel_id_text.setStyleSheet("font-family: Sitara;font-style: normal;font-weight: normal;font-size: 18px;line-height: 29px;color: #FFFFFF;")
        self.channel_id_text.setObjectName("channel_id_text")
        self.message = QtWidgets.QLabel(MainWindow)
        self.message.setGeometry(QtCore.QRect(10, 200, 110, 30))
        self.message.setStyleSheet("font-family: Sitara;font-style: normal;font-weight: normal;font-size: 18px;line-height: 29px;color: #FFFFFF;")
        self.message.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.message.setObjectName("message")
        self.delay_text = QtWidgets.QLabel(MainWindow)
        self.delay_text.setGeometry(QtCore.QRect(10, 390, 331, 30))
        self.delay_text.setStyleSheet("font-family: Sitara;font-style: normal;font-weight: normal;font-size: 18px;line-height: 29px;color: #FFFFFF;")
        self.delay_text.setObjectName("delay_text")
        self.image_text = QtWidgets.QLabel(MainWindow)
        self.image_text.setGeometry(QtCore.QRect(10, 430, 131, 30))
        self.image_text.setStyleSheet("font-family: Sitara;font-style: normal;font-weight: normal;font-size: 18px;line-height: 29px;color: #FFFFFF;")
        self.image_text.setObjectName("image_text")
        self.message_text = QtWidgets.QTextEdit(MainWindow)
        self.message_text.setGeometry(QtCore.QRect(10, 230, 581, 141))
        self.message_text.setStyleSheet("background: #C4C4C4;border-radius: 10px;font-family: Sitara;font-style: normal;font-weight: normal;font-size: 18px;line-height: 29px;color: #000000;")
        self.message_text.setObjectName("message_text")
        self.channel_id = QtWidgets.QLineEdit(MainWindow)
        self.channel_id.setGeometry(QtCore.QRect(10, 160, 581, 31))
        self.channel_id.setStyleSheet("background: #C4C4C4;border-radius: 10px;font-family: Sitara;font-style: normal;font-weight: normal;font-size: 18px;line-height: 29px;color: #000000;")
        self.channel_id.setObjectName("channel_id")
        self.lineEdit_2 = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 390, 51, 31))
        self.lineEdit_2.setStyleSheet("background: #C4C4C4;border-radius: 10px;font-family: Sitara;font-style: normal;font-weight: normal;font-size: 18px;line-height: 29px;color: #000000;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.channel_id_2 = QtWidgets.QLineEdit(MainWindow)
        self.channel_id_2.setGeometry(QtCore.QRect(10, 460, 581, 31))
        self.channel_id_2.setStyleSheet("background: #C4C4C4;border-radius: 10px;font-family: Sitara;font-style: normal;font-weight: normal;font-size: 18px;line-height: 29px;color: #000000;")
        self.channel_id_2.setObjectName("channel_id_2")
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(180, 500, 221, 61))
        self.pushButton.setStyleSheet("background: #9fff7c;border-radius: 15px;font-family: Sitara;font-style: normal;font-weight: normal;font-size: 36px;line-height: 58px;text-align: center;color: #FFFFFF;\n"
"background-color: rgb(159, 255, 124);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Discord AutoPoster"))
        self.token.setPlaceholderText(_translate("MainWindow", "Введите ваш токен"))
        self.token_text.setText(_translate("MainWindow", " Ваш токен:"))
        self.channel_id_text.setText(_translate("MainWindow", " ID канала:"))
        self.message.setText(_translate("MainWindow", " Сообщение:"))
        self.delay_text.setText(_translate("MainWindow", " Переодичность: каждые          секунд"))
        self.image_text.setText(_translate("MainWindow", " Изображение:"))
        self.message_text.setPlaceholderText(_translate("MainWindow", "Введите сообщение"))
        self.channel_id.setPlaceholderText(_translate("MainWindow", "Введите id канала"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "5"))
        self.channel_id_2.setPlaceholderText(_translate("MainWindow", "Ссылка на изображение: (img/вашеИзображение.png)"))
        self.pushButton.setText(_translate("MainWindow", "START"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
