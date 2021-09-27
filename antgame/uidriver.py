#!/usr/bin/python
# -*- coding: UTF-8 -*

from PyQt5.QtWidgets import QMainWindow
from res.antcrawl_ui import Ui_AntGame


class UiDriver(QMainWindow, Ui_AntGame):

    def __init__(self, parent=None):
        super(UiDriver, self).__init__(parent)
        self.setupUi(self)

        # Setup playroom and onclick events.
        from antgame.playroom import Playroom
        self.room = Playroom(self)
        self.button_start.clicked.connect(self.room.run_simulations)

    def update_label_min_num(self, n: int):
        self.label_min_num.setText(str(n) + ' sec')

    def update_label_max_num(self, n: int):
        self.label_max_num.setText(str(n) + ' sec')

    def update_label_case_num(self, n: int):
        self.label_case_num.setNum(n)
