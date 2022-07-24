#!/usr/bin/python
# -*- coding: UTF-8 -*

import time
from typing import List

from src.antgame.uidriver import UiDriver
from src.antgame.ant import Ant
from src.antgame.stick import Stick


class Game:
    """
    Game class. Runs unique simulation sessions.
    """

    def __init__(self, ants: List[Ant], stick: Stick):
        self.ants = ants
        self.stick = stick
        self.timer = 0

    def run(self, driver: UiDriver):
        """
        Run the whole simulation from the current status of ants and stick.
        :return: time_tick passed during the simulation.
        """
        time_tick = 0
        while True:
            # Update the position of ants and time_tick.
            for ant in self.ants:
                ant.crawl(self.stick)
            time_tick += 1
            driver.update_label_time_num(time_tick)
            print('Positions: ' + str(list(map(lambda a: a.position, self.ants))))
            time.sleep(0.03)     # Thus this function need to be run in a thread.

            # Determine whether the game has over, if ture, return time_tick.
            game_over = True
            for ant in self.ants:
                if ant.on_stick:
                    game_over = False
            if game_over:
                return time_tick

            # Determine whether ants have collided, if true, change their directions.
            ant_count = 5
            for i in range(0, ant_count):
                for j in range(i + 1, ant_count):
                    if self.ants[i].position == self.ants[j].position:
                        self.ants[i].change_direction()
                        self.ants[j].change_direction()
