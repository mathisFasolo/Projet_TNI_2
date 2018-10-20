from collections import Counter
import math
import unicodedata

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
    def getDictByASCII():
        result = {}
        ASCII_TABLE = [chr(i) for i in range(256)]
        for charASCII in ASCII_TABLE[32:]:
            result[charASCII] = Text.probabiliteParLettres(charASCII)
        return result

    @staticmethod
    def transformationText():
        with open(PATH_FILE_TXT, 'r') as text:
            brut = text.read()
            traite = unicodedata.normalize('NFD', brut).encode('ascii', 'ignore')
            with open("./data/text_ascii.txt", "w") as outfile:
                outfile.write(str(traite))


    @staticmethod
    def generer_dico_digramme():
        with open(PATH_FILE_TXT, "r") as text:
            texte = text.read()
            i = 0
            seen = []

            dico = {}
            while i < len(texte):
                if(i)
                tempDiagramme = texte[i]+texte[i+1]
                print(tempDiagramme)
                if tempDiagramme in seen:
                    dico[tempDiagramme] = dico[tempDiagramme] + 1
                else:
                    dico[tempDiagramme] = 1
                    seen.append(tempDiagramme)
                i = i + 1
            return dico




