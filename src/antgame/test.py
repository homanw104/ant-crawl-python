#!/usr/bin/python
# -*- coding: UTF-8 -*

from unittest import TestCase

from src.antgame.uidriver import UiDriver
from src.antgame.playroom import Playroom


class TestPlayroom(TestCase):

    def test_get_ant_direction(self):
        ui = UiDriver()
        room = Playroom(ui)
        self.assertEqual(room.get_ant_direction(11, 0), 'right')
        self.assertEqual(room.get_ant_direction(11, 1), 'right')
        self.assertEqual(room.get_ant_direction(11, 2), 'left')
        self.assertEqual(room.get_ant_direction(11, 3), 'right')
        self.assertEqual(room.get_ant_direction(11, 4), 'left')
