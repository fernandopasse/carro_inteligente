from Raspberry.Classes.Camera import *
from Raspberry.Classes.Ultrasonico import *

DEBUG = False

if __name__ == "__main__":
    Ultrasonico(3, 4, False)
    Camera("imagem.jpg")
