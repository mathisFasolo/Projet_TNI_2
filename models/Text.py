from collections import Counter
import math

PATH_FILE_TXT = "./data/exemple1.txt"


class Text():
    @staticmethod
    def compteurDeLettres():
        with open(PATH_FILE_TXT, "r") as text:
            traite = text.read()
            compteur = sum(Counter(traite).values())
            return compteur

    @staticmethod
    def compteurParLettres(lettre):
        with open(PATH_FILE_TXT, "r") as text:
            traite = text.read()
            compteur = Counter(traite)
            if lettre in compteur.keys():
                return compteur[lettre]
            else:
                return 0

    @staticmethod
    def probabiliteParLettres(lettre):
        return Text.compteurParLettres(lettre) / Text.compteurDeLettres()

    @staticmethod
    def enthropie():
        with open(PATH_FILE_TXT, "r") as text:
            traite = text.read()
            compteur = Counter(traite)
            enth = 0
            for lettre in compteur.keys():
                enth = enth + Text.probabiliteParLettres(lettre) * math.log(Text.probabiliteParLettres(lettre), 2)
            return -enth

    @staticmethod
    def getDictFromText():
        with open(PATH_FILE_TXT, "r") as text:
            ASCII_TABLE = "".join(chr(x) for x in range(128))
            traite = text.read()
            compteur = Counter(traite)
            if lettre in compteur.keys():
                return compteur[lettre]
            else:
                return 0

