from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
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
        self.delay = QtWidgets.QLineEdit(MainWindow)
        self.delay.setGeometry(QtCore.QRect(220, 390, 51, 31))
        self.delay.setStyleSheet("background: #C4C4C4;border-radius: 10px;font-family: Sitara;font-style: normal;font-weight: normal;font-size: 18px;line-height: 29px;color: #000000;")
        self.delay.setObjectName("delay")
        self.image = QtWidgets.QLineEdit(MainWindow)
        self.image.setGeometry(QtCore.QRect(10, 460, 581, 31))
        self.image.setStyleSheet("background: #C4C4C4;border-radius: 10px;font-family: Sitara;font-style: normal;font-weight: normal;font-size: 18px;line-height: 29px;color: #000000;")
        self.image.setObjectName("image")
        self.start_Button = QtWidgets.QPushButton(MainWindow)
        self.start_Button.setGeometry(QtCore.QRect(180, 500, 221, 61))
        self.start_Button.setStyleSheet("background: #9fff7c;border-radius: 15px;font-family: Sitara;font-style: normal;font-weight: normal;font-size: 36px;line-height: 58px;text-align: center;color: #FFFFFF;\n"
"background-color: rgb(159, 255, 124);")
        self.start_Button.setObjectName("start_Button")
        self.logs_text = QtWidgets.QTextEdit(MainWindow)
        self.logs_text.setGeometry(QtCore.QRect(10, 650, 581, 141))
        self.logs_text.setStyleSheet("background: #C4C4C4;border-radius: 20px;font-family: Sitara;font-style: normal;font-weight: normal;font-size: 16px;line-height: 58px;color: #000000;padding: 10px")
        self.logs_text.setReadOnly(True)
        self.logs_text.setObjectName("logs_text")
        self.logs_name = QtWidgets.QLabel(MainWindow)
        self.logs_name.setGeometry(QtCore.QRect(10, 620, 110, 30))
        self.logs_name.setStyleSheet("font-family: Sitara;font-style: normal;font-weight: normal;font-size: 18px;line-height: 29px;color: #FFFFFF;")
        self.logs_name.setObjectName("logs_name")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(0, 0, 351, 41))
        self.label.setStyleSheet("background: rgba(0, 0, 0, 0);font-family: Sitara;font-style: normal;font-weight: normal;font-size: 40px;line-height: 65px;color: #FFFFFF;")
        self.label.setObjectName("label")

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
        self.delay.setPlaceholderText(_translate("MainWindow", "5"))
        self.image.setPlaceholderText(_translate("MainWindow", "Ссылка на изображение: (img/вашеИзображение.png)"))
        self.start_Button.setText(_translate("MainWindow", "START"))
        self.logs_name.setText(_translate("MainWindow", " Логи"))
        self.label.setText(_translate("MainWindow", "Discord Auto Poster"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
