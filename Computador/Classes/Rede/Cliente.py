import socket

DEBUG = True


class Cliente:
    endereco = None
    porta = None
    tcp = None
    destino = None
    nomeArquivo = None
    textoMarcador = None

    def __init__(self, endereco, porta):
        self.endereco = endereco
        self.porta = porta
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.destino = (self.endereco, self.porta)
        self.tcp.connect(self.destino)

    def fecharConexao(self):
        self.tcp.close()

    def lerArquivo(self):
        abreArquivo = open(self.nomeArquivo, "r")
        self.montaPacote()
        tmp = self.abreArquivo.read()
        self.textoMarcador = self.textoMarcador + tmp
        abreArquivo.close()

    def enviaArquivo(self):
        self.tcp.send(self.textoMarcador)

    def montaPacote(self):
        self.textoMarcador = self.nomeArquivo + '_##'
        if DEBUG:
            print self.textoMarcador
