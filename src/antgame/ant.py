#!/usr/bin/python
# -*- coding: UTF-8 -*-

from src.antgame.stick import Stick


class Ant:
    """
    Ant class.
    """

    def __init__(self,
                 ant_id: int,
                 velocity: int,
                 position: int,
                 direction: str,
                 on_stick: bool):
        # direction is whether 'left' or 'right'
        self.ant_id = ant_id
        self.velocity = velocity
        self.position = position
        self.direction = direction
        self.on_stick = on_stick

    def change_direction(self):
        """
        Change the direction of this ant.
        :return: Nothing.
        """
        if self.direction == 'left':
            self.direction = 'right'
        else:
            self.direction = 'left'

    def crawl(self, stick: Stick):
        """
        Update ant's position in the next time_tick according to its current
        position and direction. on_stick is set to False if ant reaches either
        endpoint.
        :return: Nothing.
        """
        if self.on_stick:
            if self.direction == 'left':
                self.position -= self.velocity
            else:
                self.position += self.velocity

        if self.position >= stick.length or self.position <= 0:
            self.on_stick = False
