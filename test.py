#!/usr/bin/python3

from tkinter.font import ROMAN


class livres:
    def __init__(self, name="", auteur="", edition=""):
        self.name = name
        self.auteur = auteur
        self.edition = edition

    @property
    def auteur(self):
        return self.__auteur

    @auteur.setter
    def auteur(self, auteur=""):
        if auteur != "Emile Zola":
            print("Nous ne possédons aucun livre avec ce nom")
        else:
            print(" veuillez patienter qq minutes pour votre livre")

novel = livres("Les miisérables", "Emile Zola", "kaki")
