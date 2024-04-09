from PyQt6.QtWidgets import *
from gui import *
import random as rnd
import csv


class Logic(QMainWindow, Ui_montyHallGame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stats = {}
        self.users = []
        self.current_user = "not logged in"
        self.player_choice = 0
        self.correct_door = 0

        self.get_information()
        self.update_stats_text()

        self.tab_current.setCurrentIndex(0)
        self.label.setText("")
        self.label_game_instructions.setText("This is the game portion. First, you should select"
                                             "\none of the doors using the buttons labeled door #."
                                             "\nOnce you have your door selected, click the submit"
                                             "\nbutton. The game will open one of the remaining"
                                             "\ndoors without the prize behind it. You then have"
                                             "\nto choose weather to stay or switch to the last"
                                             "\nremaining door.")

        self.button_login.clicked.connect(lambda: self.login())
        self.button_register.clicked.connect(lambda: self.register())
        self.button_moveToGame.clicked.connect(lambda: self.change_to_game())
        self.button_game_next.clicked.connect(lambda: self.change_to_stats())
        self.button_game_back.clicked.connect(lambda: self.change_to_main())
        self.button_stats_back.clicked.connect(lambda: self.change_to_game())
        self.button_main_movetostats.clicked.connect(lambda: self.change_to_stats())
        self.button_stats_movetomain.clicked.connect(lambda: self.change_to_main())
        self.button_submit.clicked.connect(lambda: self.get_door())
        self.button_stay.clicked.connect(lambda: self.stay_resolve())
        self.button_Switch.clicked.connect(lambda: self.switch_resolve())
        self.button_savestats.clicked.connect(lambda: self.write_stats())

        self.button_stay.hide()
        self.button_Switch.hide()
        self.button_savestats.hide()

    def get_information(self):
        self.stats = {}
        with open("stats.csv", "r") as stats_file:
            first_line = True
            for line in stats_file:
                if first_line:
                    first_line = False
                else:
                    line = line.strip().split(",")
                    self.stats[line[0]] = [int(line[1]), int(line[2]), int(line[3]), int(line[4]), int(line[5])]
                    self.users.append(line[0])

    def login(self):
        self.label_login_status.clear()
        username = self.entry_username.text()
        if username == "":
            self.label_login_status.setText(f"Please enter a username to continue")
        elif username in self.users:
            self.current_user = username
            self.label_login_status.setText(f"You have successfully logged in as {username}.")
        else:
            self.label_login_status.setText(f"If you are a new user, click Register\n"
                                            f"If you are returning, make sure you "
                                            f"are using the same username as last time")

    def register(self):
        username = self.entry_username.text()
        if username == "":
            self.label_login_status.setText(f"Please enter a username to continue")
        elif username == "anonymous":
            self.label_login_status.setText(f"This username is reserved for those who want to play anonymously")
        elif username not in self.users:
            self.stats[username] = [0, 0, 0, 0, 0]
            self.current_user = username
            self.label_login_status.setText(f"You have successfully registered the username {username}."
                                            f"\nYou may now press the play button to continue on.")
        else:
            self.label_login_status.setText(f"This user is already registered."
                                            f"\nTry using a different name or adding numbers to the end of yours")

    def change_to_main(self):
        self.tab_current.setCurrentIndex(0)

    def change_to_game(self):
        self.button_clear()
        self.tab_current.setCurrentIndex(1)

    def change_to_stats(self):
        self.tab_current.setCurrentIndex(2)

    def get_door(self):
        if self.current_user == "not logged in":
            self.label.setText("Please log in with your unique username or anonymous first")
        else:
            if self.radioButton_door_1.isChecked():
                self.player_choice = 1
                self.play_game()
            elif self.radioButton_door_2.isChecked():
                self.player_choice = 2
                self.play_game()
            elif self.radioButton_door_3.isChecked():
                self.player_choice = 3
                self.play_game()
            else:
                self.label.setText("Chose a door")

    def play_game(self):
        self.correct_door = rnd.randint(1, 3)
        open_door = [1, 2, 3]
        open_door.remove(self.correct_door)

        if self.player_choice in open_door:  # Player did not choose winning door
            open_door.remove(self.player_choice)
            opened_door = open_door[0]
        elif self.player_choice not in open_door:
            opened_door = open_door[rnd.randint(0, 1)]

        self.label.setText(f"Door {opened_door} is now opened and does not contain the prize"
                           f"\nWould you like to stay on your current selection or switch doors?")
        self.button_stay.show()
        self.button_Switch.show()
        self.button_savestats.show()

    def stay_resolve(self):
        self.button_stay.hide()
        self.button_Switch.hide()

        if self.correct_door == 0:
            self.label.setText("No button selected")
        elif self.correct_door == self.player_choice:
            self.stats[self.current_user][0] += 1
            self.stats[self.current_user][1] += 1
            self.stats[self.current_user][3] += 1
            self.button_clear()
            self.update_stats_text()
        elif self.correct_door != self.player_choice:
            self.stats[self.current_user][0] += 1
            self.stats[self.current_user][4] += 1
            self.button_clear()
            self.update_stats_text()

    def switch_resolve(self):
        self.button_stay.hide()
        self.button_Switch.hide()

        if self.correct_door == 0:
            self.label.setText("No button selected")
        elif self.correct_door != self.player_choice:
            self.stats[self.current_user][0] += 1
            self.stats[self.current_user][2] += 1
            self.stats[self.current_user][4] += 1
            self.button_clear()
            self.update_stats_text()
        elif self.correct_door == self.player_choice:
            self.stats[self.current_user][0] += 1
            self.stats[self.current_user][3] += 1
            self.button_clear()
            self.update_stats_text()

    def update_stats_text(self):
        stats_text = ""
        games_total = 0
        player_stay_wins = 0
        player_switch_wins = 0
        total_stay_wins = 0
        total_switch_wins = 0
        for user, values in self.stats.items():
            stats_text += (f"{user}:\nTotal Games - {values[0]}, Stay Wins - {values[1]}, "
                           f"Switch Wins - {values[2]}\n")
            games_total += values[0]
            player_stay_wins += values[1]
            player_switch_wins += values[2]
            total_stay_wins += values[3]
            total_switch_wins += values[4]
        stats_text += (f"\n\nTotal Games - {games_total}, Stay Wins - {player_stay_wins},"
                       f" Switch Wins - {player_switch_wins}\n"
                       f"Switch win rate - {total_switch_wins / games_total:.2f},"
                       f" Switch win rate - {total_stay_wins / games_total:.2f}")
        self.label_stats_readout.setText(stats_text)

    def button_clear(self):
        if self.radioButton_door_1.isChecked():
            self.radioButton_door_1.nextCheckState()
            self.label.setText("")
        elif self.radioButton_door_2.isChecked():
            self.radioButton_door_2.nextCheckState()
            self.label.setText("")
        elif self.radioButton_door_3.isChecked():
            self.radioButton_door_3.nextCheckState()
            self.label.setText("")

    def write_stats(self):
        with open("stats.csv", "w", newline="") as stats_file:
            content = csv.writer(stats_file)
            content.writerow(['User', 'Total Games Played', 'Stay Wins', 'Switch Wins',
                              'Unrealized Switch Wins', 'Unrealized Stay Wins'])
            for user, stats in self.stats.items():
                content.writerow([user, stats[0], stats[1], stats[2], stats[3], stats[4]])
