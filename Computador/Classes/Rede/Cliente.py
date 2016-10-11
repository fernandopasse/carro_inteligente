import socket


class Cliente:
    endereco = None
    porta = None
    tcp = None
    destino = None
    nomeArquivo = None

    def __init__(self, endereco, porta):
        self.endereco = endereco
        self.porta = porta
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.destino = (self.endereco, self.porta)
        self.tcp.connect(self.destino)

    def fecharConexao(self):
        self.tcp.close()