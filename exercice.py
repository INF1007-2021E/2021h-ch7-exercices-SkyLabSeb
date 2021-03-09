#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import pi

# import sys
# sys.path.append("C:\Users\SkyLab\OneDrive\Sessions - H2021\INF1007\GitHub\2021h-ch6-1-exercice-SkyLabSeb\settings\")
# from _exercice_version_prof import frequence
import sys
sys.path.insert(0, 'C:\\Users\SkyLab\OneDrive\Sessions - H2021\INF1007\GitHub\\2021h-ch6-1-exercices-SkyLabSeb')
from exercice_version_prof import frequence
import turtle





# TODO: Importez vos modules ici



# TODO: Définissez vos fonction ici

def compute_volume_and_masse(a=5, b=8, c=10, mass_vol=4):
    volume = pi * a * b * c * 4 / 3
    mass = volume * mass_vol

    return volume, mass

def arbre()













if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    mass_vol = compute_volume_and_masse()
    print(mass_vol)

    print((lambda x: sorted(frequence(x), key=frequence(x).__getitem__)[-1])("test test test test"))

    turtle.position()
    turtle.forward(25)
    turtle.left(15)
    turtle.forward(25)





