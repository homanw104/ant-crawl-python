#!/usr/bin/python
# -*- coding: UTF-8 -*

from playroom import Playroom


def greetings():
    print('This is an ant simulator.')
    print('Starting...\n')


if __name__ == '__main__':
    greetings()
    room = Playroom()
    room.run_simulations()
