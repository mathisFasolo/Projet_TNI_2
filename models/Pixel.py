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
    def getDictPixel():
        result = {}
        PIXEL_POSSIBLE = [i for i in range(256)]
        for pixel in PIXEL_POSSIBLE:
            result[pixel] = Pixel.probabiliteParPixel(str(pixel))
        minProba = min(filter(lambda a: a != 0.0, result.values()))
        for pixel in result:
                result[pixel] = minProba if result[pixel] == 0 else result[pixel]
        return result

    @staticmethod
    def splitListValuesByPacket(dictPixel):
        valuesDict = list(dictPixel.values())
        for i in range(0, len(valuesDict), 8):
            yield valuesDict[i:i+8]