from Raspberry.Classes.Camera import *
from Raspberry.Classes.Ultrasonico import *

DEBUG = False

if __name__ == "__main__":
    #Declara os sensores
    ultrasonicoFrontal = Ultrasonico(3, 4)
    ultrasonicoDireito = Ultrasonico(5, 6)
    ultrasonicoEsquerdo = Ultrasonico(6, 7)
    ultrasonicoTraseiro = Ultrasonico(7, 8)

    while True:
        print ultrasonicoDireito.leDistanciaCM()
        print ultrasonicoEsquerdo.leDistanciaCM()
        print ultrasonicoFrontal.leDistanciaCM()
        print ultrasonicoTraseiro.leDistanciaCM()