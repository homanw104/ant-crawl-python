#!/usr/bin/python
# -*- coding: UTF-8 -*

import threading
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QMainWindow
from res.antcrawl_ui import Ui_AntGame


class UiDriver(QMainWindow, Ui_AntGame):

    def __init__(self, parent=None):
        super(UiDriver, self).__init__(parent)
        self.setupUi(self)

        # Setup playroom and buttons' onclick events.
        from antgame.playroom import Playroom
        self.room = Playroom(self)
        self.room_thread = threading.Thread(target=self.room.run_simulations)
        self.button_start.clicked.connect(self.button_start_clicked)
        self.button_reset.clicked.connect(self.button_reset_clicked)

    def button_start_clicked(self):
        self.room_thread.start()

    def button_reset_clicked(self):
        if not self.room_thread.is_alive():
            self.label_min_num.setText('0 sec')
            self.label_max_num.setText('0 sec')
            self.label_case_num.setText('0')
            self.text_output.setPlainText('')
            self.room_thread = threading.Thread(target=self.room.run_simulations)   # Start a new thread.

    def update_label_min_num(self, n: int):
        self.label_min_num.setText(str(n) + ' sec')

    def update_label_max_num(self, n: int):
        self.label_max_num.setText(str(n) + ' sec')

    def update_label_time_num(self, n: int):
        self.label_time_num.setText(str(n) + ' sec')

    def update_label_case_num(self, n: int):
        self.label_case_num.setNum(n)

    def update_label_output(self, txt: str):
        self.label_output.setText(txt)
