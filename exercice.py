#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import pi

# import sys
# sys.path.append("C:\Users\SkyLab\OneDrive\Sessions - H2021\INF1007\GitHub\2021h-ch6-1-exercice-SkyLabSeb\settings\")
# from _exercice_version_prof import frequence
import sys
sys.path.insert(0, 'C:\\Users\SkyLab\OneDrive\Sessions - H2021\INF1007\GitHub\\2021h-ch6-1-exercices-SkyLabSeb')
from exercice_version_prof import frequence
from turtle import *





# TODO: Importez vos modules ici



# TODO: Définissez vos fonction ici

def compute_volume_and_masse(a=5, b=8, c=10, mass_vol=4):
    volume = pi * a * b * c * 4 / 3
    mass = volume * mass_vol

    return volume, mass

def draw_branch(branch_len, pen_size, angle):
    if branch_len > 0 and pen_size > 0:
        pensize(pen_size)
        forward(branch_len)
        right(angle)
        draw_branch(branch_len - 10, pen_size - 1, angle - 5)
        left(angle*2)
        draw_branch(branch_len - 10, pen_size - 1, angle - 5)
        right(angle)
        backward(branch_len)

    else:
        pass

def arbre():
    setheading(90)
    color("green")
    draw_branch(70, 7, 35)








rt(-90)

# the acute angle between
# the base and branch of the Y
angle = 30

# function to plot a Y
def y(sz, level):
    if level > 0:
        colormode(255)

        # splitting the rgb range for green
        # into equal intervals for each level
        # setting the colour according
        # to the current level
        pencolor(0, 255 // level, 0)

        # drawing the base
        fd(sz)

        rt(angle)

        # recursive call for
        # the right subtree
        y(0.8 * sz, level - 1)

        pencolor(0, 255 // level, 0)

        lt(2 * angle)

        # recursive call for
        # the left subtree
        y(0.8 * sz, level - 1)

        pencolor(0, 255 // level, 0)

        rt(angle)
        fd(-sz)

        # tree of size 80 and level 7














if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    mass_vol = compute_volume_and_masse()
    print(mass_vol)

    print((lambda x: sorted(frequence(x), key=frequence(x).__getitem__)[-1])("test test test test"))

    # turtle.position()
    # turtle.forward(25)
    # turtle.left(15)
    # turtle.forward(25)
    y(80, 7)




