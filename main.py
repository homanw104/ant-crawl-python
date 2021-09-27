#!/usr/bin/python
# -*- coding: UTF-8 -*

import sys
from antgame import *
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UiDriver()
    ui.show()
    sys.exit(app.exec_())
