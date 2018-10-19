from models.Text import Text
from models.Pixel import Pixel

def codage_huffman(list_traite):
    print(sorted(list_traite.values(), key=list_traite.keys()))


if __name__ == '__main__':

    probas=[0.4, 0.2, 0.15, 0.15]
    print(Pixel.getTag(probas))


