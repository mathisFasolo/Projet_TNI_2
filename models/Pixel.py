import numpy
import math

PATH_FILE_IMG = "./data/lena_gray.raw.txt"


class Pixel():

    @staticmethod
    def compteurDePixel():
        with open(PATH_FILE_IMG, "r") as img:
            traite = img.read().split(" ")
            listTraite = numpy.array(traite)
            return listTraite.size - 1

    @staticmethod
    def compteurParPixel(pixel):
        with open(PATH_FILE_IMG, "r") as img:
            traite = img.read().split(" ")
            listTraite = numpy.array(traite)
            unique, counts = numpy.unique(listTraite, return_counts=True)
            dictTraite = dict(zip(unique, counts))
            if pixel in dictTraite.keys():
                return dictTraite[pixel]
            else:
                return 0

    @staticmethod
    def probabiliteParPixel(pixel):
        return Pixel.compteurParPixel(pixel) / Pixel.compteurDePixel()

    @staticmethod
    def enthropiePixel():
        with open(PATH_FILE_IMG, "r") as img:
            traite = img.read().split(" ")
            listTraite = numpy.array(traite)
            enth = 0
            for traitement in numpy.unique(listTraite):
                enth = enth + Pixel.probabiliteParPixel(traitement) * math.log(Pixel.probabiliteParPixel(traitement), 2)
            return -enth

    @staticmethod
    ## tabProbas est un paquet, soit 8 pixels
    def getTag(tabProbas):

        print(tabProbas)

        tabProbas





        return res
