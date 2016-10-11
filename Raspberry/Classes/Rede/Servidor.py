import socket


class Servidor:
    enderecoServidor = None
    porta = None
    tcp = None
    origemConexao = None
    nomeArquivo = None

    def __init__(self, endereco, porta):
        self.enderecoServidor = endereco
        self.porta = porta
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.origemConexao = (self.enderecoServidor, self.porta)
        self.tcp.bind(self.origemConexao)
        self.tcp.listen(9999)
