from Raspberry.Classes.Ultrasonico import *
from Raspberry.Classes.Camera import *

DEBUG = False

if __name__ == "__main__":
    Ultrasonico(3, 4, False)
    Camera("imagem.jpg")