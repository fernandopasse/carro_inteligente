# coding: utf-8
import picamera.PiCamera as picamera

DEBUG = True

class Camera:
    camera = None
    nomeImagem = None

    def __init__(self, nomeImagem):
        if DEBUG:
            print "NOME DA IMAGEM: %s (__init__(camera)) " % (nomeImagem)
        self.camera = picamera.PiCamera()

    def capturaImagem(self):
        self.camera.capture(self.nomeImagem)