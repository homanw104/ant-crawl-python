#!/usr/bin/python
# -*- coding: UTF-8 -*
import time

from antgame.uidriver import UiDriver
from antgame.ant import Ant
from antgame.stick import Stick
from antgame.game import Game


class Playroom:
    """
    Playroom class. In charge of issuing all simulations.
    """

    def __init__(self, driver: UiDriver):
        # Initial positions of every ant.
        self.init_positions = [30, 80, 110, 160, 250]

        # Total of ants derived from list init_positions.
        self.ant_total = len(self.init_positions)

        # The speed of ants (unit: cm / sec)
        self.ant_velocity = 5

        # The length of stick to be defined for Stick object (unit: cm).
        self.stick_length = 300     # Must be a multiple of ant_velocity due to implementation.

        # An empty result list for every simulation (unit: sec)
        self.results = []

        # Set UI driver.
        self.driver = driver

    def run_simulations(self):
        """
        Run (2 ^ ant_count) times of simulations, print out time spent in every
        case, also the time spent in the worse case & the optimal case. The
        List[Ant] and Stick object are initialized and passed to each Game.
        :return: Nothing.
        """
        for case_num in range(2 ** self.ant_total):
            # Update case number in UI.
            self.driver.update_label_case_num(case_num + 1)

            # Create ants.
            ants = []
            for ant_num in range(self.ant_total):
                ants.append(Ant(
                    ant_id=ant_num,
                    velocity=self.ant_velocity,
                    position=self.init_positions[ant_num],
                    direction=self.get_ant_direction(case_num, ant_num),
                    on_stick=True
                ))

            # Create stick.
            stick = Stick(length=self.stick_length)

            # Run this simulation.
            game = Game(ants, stick)
            result = game.run()

            # Print and store the result.
            print(f'Case [{case_num+1}] \t {result} s')
            self.results.append(result)

            # Update min / max number in UI.
            self.driver.update_label_max_num(max(self.results))
            self.driver.update_label_min_num(min(self.results))

        # Final results.
        print(f'Final MAX time: \t {max(self.results)} s')
        print(f'Final MIN time: \t {min(self.results)} s')

    def get_ant_direction(self, case_num: int, ant_num: int) -> str:
        """
        Utility Method, return 'left' or 'right' regarding the given parameters.
        We tear down the case_num into a binary number and dim each digit as
        the direction of an ant.

        E.g. In the case of 5 ants (ant_total = 5), given case_num = 11 and
        ant_num = 3, we tear 11 into binary 01011.

            Position: [4] [3] [2] [1] [0]
            Binary:    0   1   0   1   1

        0 stands for 'left', and 1 stands for 'right'. Since the direction of
        ant number 3 is wanted, the digit in position 3 is translated to 'left'
        and returned.

        :param case_num: case number, range from 0 to (2^ant_count - 1)
        :param ant_num: ant number, range from 0 to (ant_count - 1)
        :return: 'left' or 'right'
        """
        digit = (case_num // (2**ant_num)) % 2
        if ant_num >= self.ant_total:
            return 'undefined'
        if digit == 0:
            return 'left'
        if digit == 1:
            return 'right'
        else:
            return 'error'
