from models.Text import Text
from models.Pixel import Pixel

def codage_huffman(list_traite):
    dictForHuffman = Text.getDictByASCII()
    dictValues = list(dictForHuffman.values())
    minProba = min(list(filter(lambda a: a != 0.0, dictValues)))
    for key in dictForHuffman:
        if dictForHuffman[key] == 0.0 or dictForHuffman[key] == 0:
            dictForHuffman[key] = minProba
    codage_huffman(dictForHuffman)

def codage_arithmetique(dict_pixel_proba):
    pass


if __name__ == '__main__':
    print(Pixel.getDictPixel())