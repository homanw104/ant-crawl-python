#!/usr/bin/python
# -*- coding: UTF-8 -*

from typing import List

from ant import Ant
from stick import Stick


class Game:
    """
    Game class. Runs unique simulation sessions.
    """

    def __init__(self, ants: List[Ant], stick: Stick):
        self.ants = ants
        self.stick = stick
        self.timer = 0

    def run(self):
        """
        Run the whole simulation from the current status of ants and stick.
        :return: time_tick passed during the simulation.
        """
        time_tick = 0
        while True:
            # Update the position of ants in the next time_tick.
            for ant in self.ants:
                ant.crawl(self.stick)
            time_tick += 1

            # Determine whether the game has over, if ture, return time_tick.
            game_over = True
            for ant in self.ants:
                if ant.on_stick:
                    game_over = False
            if game_over:
                return time_tick

            # Determine whether ants has collided, if true, change their directions.
            ant_count = 5
            for i in range(0, ant_count):
                for j in range(i + 1, ant_count):
                    if self.ants[i].position == self.ants[j].position:
                        self.ants[i].change_direction()
                        self.ants[j].change_direction()