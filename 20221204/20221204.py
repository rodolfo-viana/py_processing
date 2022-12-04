# 2022-12-04
# Made with Thonny and thonny-py5mode library
#
# Code heavily based on Alexandre Villares' work, on
# https://github.com/villares/sketch-a-day/tree/main/2022/sketch_2022_01_01a
#
# Kudos to Villares, the most notable Processing guru
# in Brazil, whose works and classes have inspired so
# many people, including myself.

from itertools import product

grid = product(range(100), repeat=2)

def elem(pos, step=7):
    line(
        pos[0] * step,
        pos[1] * step,
        pos[0] * step,
        pos[1] * step + random(pos[0] * pos[1] / 100.0)
    )


def setup():
    size(600, 600)
    background('#264653')


def draw():
    stroke('#C6DCE5')
    stroke_weight(2)
    for i in grid:
        elem(i) 
    save('20221204.png')
