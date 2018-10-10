from models.Text import Text
from models.Pixel import Pixel

def codage_huffman(list_traite):
    print(sorted(list_traite.values(), key=list_traite.keys()))


if __name__ == '__main__':
    """dictForHuffman = Text.getDictByASCII()
    dictValues = list(dictForHuffman.values())
    minProba = min(list(filter(lambda a: a != 0.0, dictValues)))
    for key in dictForHuffman:
        if dictForHuffman[key] == 0.0 or dictForHuffman[key] == 0:
            dictForHuffman[key] = minProba
    codage_huffman(dictForHuffman)"""

