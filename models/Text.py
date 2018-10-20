from collections import Counter
import math
import json
from operator import itemgetter, attrgetter
import unicodedata
import unidecode

PATH_FILE_TXT = "./data/text_ascii.txt"


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
            #traite = unicodedata.normalize('NFD', brut).encode('ascii', 'ignore')
            traite = unidecode.unidecode(brut)
            with open("./data/text_ascii.txt", "w") as outfile:
                outfile.write(str(traite))

    '''
        Cette fonction trie genere un tableau de dictionnaire avec une association 
        n_gram / occurence dans le texte de tallgrand
        @:param Taille n_gram
        @:returns list
    '''
    @staticmethod
    def generer_dico_ngramme(taille_n):
        with open(PATH_FILE_TXT, "r") as text:
            texte = text.read()
            i = 0
            seen = []
            dico = {}
            result = []
            bound = taille_n - 1
            while i < len(texte) - bound:
                tempDiagramme = ""
                for j in range(taille_n):
                    tempDiagramme = tempDiagramme + texte[i+j]
                if tempDiagramme in seen:
                    dico[tempDiagramme] = dico[tempDiagramme] + 1
                else:
                    dico[tempDiagramme] = 1
                    seen.append(tempDiagramme)
                i = i + 1
            for key, value in dico.items():
                result.append({key: value})
            return sorted(result, reverse=True, key=lambda dictionnarie: list(dictionnarie.values())[0])

    @staticmethod
    def generateByteList(list_dict_ngram):
        dictResult = {}
        i = 0
        if len(list_dict_ngram) > 256:
            list_dict_ngram = list_dict_ngram[:255]
        for dict_ngram in list_dict_ngram:
            dictResult[list(dict_ngram.keys())[0]] = bytes([i])
            #dictResult[list(dict_ngram.keys())[0]] = i
            i = i + 1
        return dictResult

    @staticmethod
    def saveDictionnaire(dictionnaire):
        with open('./dictionnaire/Dictionnaire.json', 'w+') as final_file:
            json.dump(dictionnaire, final_file)

    @staticmethod
    def creerDictionnaire(listUnigram = list(), listDigram = list(), listTrigram = list()):
        result = []
        for unigram in listUnigram:
            result.append({list(unigram.keys())[0]: list(unigram.values())[0]})
        for digram in listDigram:
            result.append({list(digram.keys())[0]: list(digram.values())[0]})
        for trigram in listTrigram:
            result.append({list(trigram.keys())[0]: list(trigram.values())[0]})
        return result

    @staticmethod
    def encode(dictionnaire):
        with open(PATH_FILE_TXT, 'r') as file:
            result = []
            i = 0
            text = file.read()
            while i < len(text) - 3:
                bound = 0
                for j in reversed(range(4)):
                    temp_naire = text[i:i + j]
                    if temp_naire in dictionnaire:
                        result.append(dictionnaire[temp_naire])
                        bound = j
                        break
                i = i + bound
            return result

    @staticmethod
    def tauxDeCompression():
        nbBytesUncompressed = 1
        nbBytesCompressed = 0
        with open(PATH_FILE_TXT, 'rb') as uncompressedFile:
            data = uncompressedFile.read()
            print("Taille fichier origine: %d" % len(data))
            nbBytesUncompressed = len(data)
        with open("./data/text_ascii_compressed", 'rb') as compressedFile:
            data = compressedFile.read()
            print("Taille fichier compressé: %d" % len(data))
            nbBytesCompressed = len(data)
        return (nbBytesCompressed/nbBytesUncompressed) * 100