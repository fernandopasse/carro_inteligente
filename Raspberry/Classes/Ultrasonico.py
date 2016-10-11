# coding: utf-8

import time

import RPi.GPIO as GPIO

DEBUG = None


class Ultrasonico:
    pinoTrigger = None
    pinoEcho = None
    VELOCIDADE_SOM_CM = 34029
    VELOCIDADE_SOM_M = 340.29

    # Define e inicializa os pinos TRIGGER e ECHO
    def __init__(self, pinoTrigger, pinoEcho, mode):
        self.pinoEcho = pinoEcho
        self.pinoTrigger = pinoTrigger
        if mode:
            GPIO.setmode(GPIO.BOARD)
        else:
            GPIO.setmode(GPIO.BCM)
        GPIO.setup(pinoTrigger, GPIO.OUT)
        GPIO.setup(pinoEcho, GPIO.IN)

    def leDistanciaMetro(self):
        # Prepara para emitir o sinal
        GPIO.output(self.pinoTrigger, GPIO.LOW)
        time.sleep(1)

        # Emite o sinal com duração de 10us marcando o inicio da medição
        GPIO.output(self.pinoTrigger, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.pinoTrigger, GPIO.LOW)

        while GPIO.input(self.pinoEcho) == GPIO.LOW:
            tempo_inicial = time.time()

        while GPIO.input(self.pinoEcho) == GPIO.HIGH:
            tempo_final = time.time()

        tempo_total = tempo_final - tempo_inicial

        distancia = (tempo_total * self.VELOCIDADE_SOM_M) / 2

        if DEBUG:
            print "O VALOR RETORNADO (leDistanciaMetro): %.2f" % (distancia)

        return distancia

    def leDistanciaCM(self):
        # Prepara para emitir o sinal
        GPIO.output(self.pinoTrigger, GPIO.LOW)
        time.sleep(1)

        # Emite o sinal com duração de 10us marcando o inicio da medição
        GPIO.output(self.pinoTrigger, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.pinoTrigger, GPIO.LOW)

        while GPIO.input(self.pinoEcho) == GPIO.LOW:
            tempo_inicial = time.time()

        while GPIO.input(self.pinoEcho) == GPIO.HIGH:
            tempo_final = time.time()

        tempo_total = tempo_final - tempo_inicial

        distancia = (tempo_total * self.VELOCIDADE_SOM_CM) / 2

        if DEBUG:
            print "O VALOR RETORNADO (leDistanciaCM): %.2f" % (distancia)

        return distancia
