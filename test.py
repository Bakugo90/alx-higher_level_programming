#!/usr/bin/python3

class Humain():
    pass

samadou = Humain()
samadou.sexe = 'masculin'
samadou.profession = 'Developeur'
samadou.age = 19
getattr(samadou, 'etude', 'physique')

