# Form implementation generated from reading ui file 'MontyHallGUI.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_montyHallGame(object):
    def setupUi(self, montyHallGame):
        montyHallGame.setObjectName("montyHallGame")
        montyHallGame.resize(900, 550)
        self.tab_current = QtWidgets.QTabWidget(parent=montyHallGame)
        self.tab_current.setGeometry(QtCore.QRect(0, 0, 901, 551))
        self.tab_current.setObjectName("tab_current")
        self.screen_main = QtWidgets.QWidget()
        self.screen_main.setObjectName("screen_main")
        self.label_login = QtWidgets.QLabel(parent=self.screen_main)
        self.label_login.setGeometry(QtCore.QRect(20, 50, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_login.setFont(font)
        self.label_login.setObjectName("label_login")
        self.entry_username = QtWidgets.QLineEdit(parent=self.screen_main)
        self.entry_username.setGeometry(QtCore.QRect(90, 50, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.entry_username.setFont(font)
        self.entry_username.setObjectName("entry_username")
        self.label_login_instruction = QtWidgets.QLabel(parent=self.screen_main)
        self.label_login_instruction.setGeometry(QtCore.QRect(0, 0, 781, 41))
        self.label_login_instruction.setObjectName("label_login_instruction")
        self.button_login = QtWidgets.QPushButton(parent=self.screen_main)
        self.button_login.setGeometry(QtCore.QRect(10, 100, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_login.setFont(font)
        self.button_login.setObjectName("button_login")
        self.button_register = QtWidgets.QPushButton(parent=self.screen_main)
        self.button_register.setGeometry(QtCore.QRect(130, 100, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_register.setFont(font)
        self.button_register.setObjectName("button_register")
        self.text_game_explanation = QtWidgets.QTextBrowser(parent=self.screen_main)
        self.text_game_explanation.setGeometry(QtCore.QRect(10, 160, 741, 291))
        self.text_game_explanation.setObjectName("text_game_explanation")
        self.button_moveToGame = QtWidgets.QPushButton(parent=self.screen_main)
        self.button_moveToGame.setGeometry(QtCore.QRect(770, 460, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_moveToGame.setFont(font)
        self.button_moveToGame.setObjectName("button_moveToGame")
        self.label_login_status = QtWidgets.QLabel(parent=self.screen_main)
        self.label_login_status.setGeometry(QtCore.QRect(230, 40, 481, 41))
        self.label_login_status.setText("")
        self.label_login_status.setObjectName("label_login_status")
        self.button_main_movetostats = QtWidgets.QPushButton(parent=self.screen_main)
        self.button_main_movetostats.setGeometry(QtCore.QRect(770, 400, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_main_movetostats.setFont(font)
        self.button_main_movetostats.setObjectName("button_main_movetostats")
        self.tab_current.addTab(self.screen_main, "")
        self.screen_game = QtWidgets.QWidget()
        self.screen_game.setObjectName("screen_game")
        self.image_door_1 = QtWidgets.QLabel(parent=self.screen_game)
        self.image_door_1.setGeometry(QtCore.QRect(10, 10, 161, 341))
        self.image_door_1.setText("")
        self.image_door_1.setPixmap(QtGui.QPixmap("door.png"))
        self.image_door_1.setScaledContents(True)
        self.image_door_1.setObjectName("image_door_1")
        self.image_door_2 = QtWidgets.QLabel(parent=self.screen_game)
        self.image_door_2.setGeometry(QtCore.QRect(190, 10, 161, 341))
        self.image_door_2.setText("")
        self.image_door_2.setPixmap(QtGui.QPixmap("door.png"))
        self.image_door_2.setScaledContents(True)
        self.image_door_2.setObjectName("image_door_2")
        self.image_door_3 = QtWidgets.QLabel(parent=self.screen_game)
        self.image_door_3.setGeometry(QtCore.QRect(370, 10, 161, 341))
        self.image_door_3.setText("")
        self.image_door_3.setPixmap(QtGui.QPixmap("door.png"))
        self.image_door_3.setScaledContents(True)
        self.image_door_3.setObjectName("image_door_3")
        self.radioButton_door_1 = QtWidgets.QRadioButton(parent=self.screen_game)
        self.radioButton_door_1.setGeometry(QtCore.QRect(10, 350, 161, 31))
        self.radioButton_door_1.setObjectName("radioButton_door_1")
        self.radioButton_door_2 = QtWidgets.QRadioButton(parent=self.screen_game)
        self.radioButton_door_2.setGeometry(QtCore.QRect(190, 350, 161, 31))
        self.radioButton_door_2.setObjectName("radioButton_door_2")
        self.radioButton_door_3 = QtWidgets.QRadioButton(parent=self.screen_game)
        self.radioButton_door_3.setGeometry(QtCore.QRect(370, 350, 161, 31))
        self.radioButton_door_3.setObjectName("radioButton_door_3")
        self.label = QtWidgets.QLabel(parent=self.screen_game)
        self.label.setGeometry(QtCore.QRect(10, 380, 521, 131))
        self.label.setObjectName("label")
        self.button_submit = QtWidgets.QPushButton(parent=self.screen_game)
        self.button_submit.setGeometry(QtCore.QRect(550, 450, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_submit.setFont(font)
        self.button_submit.setObjectName("button_submit")
        self.button_game_next = QtWidgets.QPushButton(parent=self.screen_game)
        self.button_game_next.setGeometry(QtCore.QRect(770, 460, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_game_next.setFont(font)
        self.button_game_next.setObjectName("button_game_next")
        self.button_game_back = QtWidgets.QPushButton(parent=self.screen_game)
        self.button_game_back.setGeometry(QtCore.QRect(770, 400, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_game_back.setFont(font)
        self.button_game_back.setObjectName("button_game_back")
        self.button_Switch = QtWidgets.QPushButton(parent=self.screen_game)
        self.button_Switch.setGeometry(QtCore.QRect(420, 390, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_Switch.setFont(font)
        self.button_Switch.setObjectName("button_Switch")
        self.button_stay = QtWidgets.QPushButton(parent=self.screen_game)
        self.button_stay.setGeometry(QtCore.QRect(420, 450, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_stay.setFont(font)
        self.button_stay.setObjectName("button_stay")
        self.label_game_instructions = QtWidgets.QLabel(parent=self.screen_game)
        self.label_game_instructions.setGeometry(QtCore.QRect(550, 10, 331, 341))
        self.label_game_instructions.setObjectName("label_game_instructions")
        self.tab_current.addTab(self.screen_game, "")
        self.screen_stats = QtWidgets.QWidget()
        self.screen_stats.setObjectName("screen_stats")
        self.button_stats_back = QtWidgets.QPushButton(parent=self.screen_stats)
        self.button_stats_back.setGeometry(QtCore.QRect(770, 460, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_stats_back.setFont(font)
        self.button_stats_back.setObjectName("button_stats_back")
        self.button_stats_movetomain = QtWidgets.QPushButton(parent=self.screen_stats)
        self.button_stats_movetomain.setGeometry(QtCore.QRect(770, 400, 111, 51))
        self.button_savestats = QtWidgets.QPushButton(parent=self.screen_stats)
        self.button_savestats.setGeometry(QtCore.QRect(770, 340, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_stats_movetomain.setFont(font)
        self.button_stats_movetomain.setObjectName("button_stats_movetomain")
        self.button_savestats.setFont(font)
        self.button_savestats.setObjectName("button_savestats")
        self.label_stats_readout = QtWidgets.QLabel(parent=self.screen_stats)
        self.label_stats_readout.setGeometry(QtCore.QRect(10, 20, 751, 481))
        self.label_stats_readout.setText("")
        self.label_stats_readout.setObjectName("label_stats_readout")
        self.tab_current.addTab(self.screen_stats, "")

        self.retranslateUi(montyHallGame)
        self.tab_current.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(montyHallGame)

    def retranslateUi(self, montyHallGame):
        _translate = QtCore.QCoreApplication.translate
        montyHallGame.setWindowTitle(_translate("montyHallGame", "Dialog"))
        self.label_login.setText(_translate("montyHallGame", "Login"))
        self.entry_username.setPlaceholderText(_translate("montyHallGame", "Username"))
        self.label_login_instruction.setText(_translate("montyHallGame", "Enter a unique username and select login or register depending of if you have played before (Do NOT enter a password)"))
        self.button_login.setText(_translate("montyHallGame", "LOGIN"))
        self.button_register.setText(_translate("montyHallGame", "REGISTER"))
        self.text_game_explanation.setHtml(_translate("montyHallGame", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">The Monty Hall problem is a brain teazer in the form of a probabilty puzzle. It is based on the TV show &quot;Let\'s Make a Deal&quot; and named after its original host Monty Hall.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">In the puzzle, players are given the choice between 3 doors. Behind one door, there is a desireble prize. Behind the other two is nothing. The player is to make a choice of which door they think the prize is behind. After that, the host would open one of the doors which does not contain the prize. The player then has to choose weather to remain on the door he/she selected originally or switch to the door that has not been opened or selected. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Now that you know how the game works, lets try it out.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p></body></html>"))
        self.button_moveToGame.setText(_translate("montyHallGame", "Play"))
        self.button_main_movetostats.setText(_translate("montyHallGame", "Statistics"))
        self.tab_current.setTabText(self.tab_current.indexOf(self.screen_main), _translate("montyHallGame", "Login"))
        self.radioButton_door_1.setText(_translate("montyHallGame", "Door 1"))
        self.radioButton_door_2.setText(_translate("montyHallGame", "Door 2"))
        self.radioButton_door_3.setText(_translate("montyHallGame", "Door 3"))
        self.label.setText(_translate("montyHallGame", "End game text"))
        self.button_submit.setText(_translate("montyHallGame", "SUBMIT"))
        self.button_game_next.setText(_translate("montyHallGame", "Statistics"))
        self.button_game_back.setText(_translate("montyHallGame", "Back"))
        self.button_Switch.setText(_translate("montyHallGame", "Switch"))
        self.button_stay.setText(_translate("montyHallGame", "Stay"))
        self.label_game_instructions.setText(_translate("montyHallGame", "TextLabel"))
        self.tab_current.setTabText(self.tab_current.indexOf(self.screen_game), _translate("montyHallGame", "Game"))
        self.button_stats_back.setText(_translate("montyHallGame", "Back"))
        self.button_stats_movetomain.setText(_translate("montyHallGame", "Main Menu"))
        self.button_savestats.setText(_translate("montyHallGame", "Save"))
        self.tab_current.setTabText(self.tab_current.indexOf(self.screen_stats), _translate("montyHallGame", "Statistics"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    montyHallGame = QtWidgets.QDialog()
    ui = Ui_montyHallGame()
    ui.setupUi(montyHallGame)
    montyHallGame.show()
    sys.exit(app.exec())
