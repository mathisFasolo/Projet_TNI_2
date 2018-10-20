import itertools
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


def codage_arithmetique(dict_pixel_proba, list_length):
    pass


if __name__ == '__main__':
    # transform text to ascii
    Text.transformationText()
    # genere 3 dictionnaire en fonction des unigramme, digramme et trigramme
    dicoUnigram = Text.generer_dico_ngramme(1)
    dicoDigram = Text.generer_dico_ngramme(2)
    dicoTrigram = Text.generer_dico_ngramme(3)
    print(len(dicoUnigram))
    print(len(dicoDigram))
    print(len(dicoTrigram))
    # associe un byte à un n_gramme dans un nouveau dictionnaire
    dicoNgram = Text.creerDictionnaire(dicoUnigram, dicoDigram[:100], dicoTrigram[:98])
    print(len(dicoNgram))
    finalDictionnary = Text.generateByteList(dicoNgram)
    print(finalDictionnary)

    newText = Text.encode(finalDictionnary)
    with open("./data/text_ascii_compressed", 'wb+') as compressed_file:
        for bytes in newText:
            compressed_file.write(bytes)
    print(Text.tauxDeCompression())

    #print(Text.encode(dicoUnigram, dicoDigram))
    # dictPixel = Pixel.getDictPixel()
    # packets = list(Pixel.splitListValuesByPacket(dictPixel))
    # print(len(packets))
    # for packet in packets:
    #     print(packet)
