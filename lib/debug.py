#!/usr/bin/env python3
import ipdb

from classes.player import Player
from classes.game import Game
from classes.result import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    snake = Game("Snake")
    jacob = Player("Jacob")
    game1 = Result(jacob, snake, 200)
    game2 = Result(jacob, snake, 400)
    henry = Player("yoiscool")
    game3 = Result(henry, snake, 150)

    ipdb.set_trace()
