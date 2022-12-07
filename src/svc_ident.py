import grpc
import sys
import secrets

import ident_pb2
import ident_pb2_grpc

from concurrent import futures

import socket
hostname = socket.gethostname() # caso seja tudo na mesma maquina, pode-se mudar para "localhost"

server = grpc.server(futures.ThreadPoolExecutor(max_workers=1)) # cria servidor

class Ident(ident_pb2_grpc.IdentidadesServicer):

    # dicionario que ira armazenar os dados inseridos no servidor no formato: { identificacao : (vetor, senha, permissao) }
    # de inicio, as informacoes do administrador ja sao inseridas no dicionario
    itens = {'super' : ([secrets.token_bytes(32)], int(sys.argv[2]), "SP")} 

    def autenticacao(self, request, context): # procedimento de autenticacao

        # se o usuario nao existe ou a senha esta errada, retorne -1 e um vetor de zeros
        if request.identificacao not in self.itens.keys() or self.itens[request.identificacao][1] != request.senha:
            retorno = -1
            vetor = [secrets.token_bytes(32)]

        # caso contrario, atualize o valor do vetor do usuario para um novo, retorne 0 e o vetor gerado
        else:
            retorno = 0
            if request.identificacao != 'super':
                self.itens[request.identificacao] = ([secrets.token_bytes(32)], request.senha, self.itens[request.identificacao][2])
            vetor = self.itens[request.identificacao][0]
        
        return ident_pb2.AuthReply(retorno=retorno, vetor=vetor)

    def criacao(self, request, context): # procedimento de insercao de usuario

        # se o vetor da ultima autenticacao for diferente do vetor do super, retorne -1
        if request.vetor != self.itens['super'][0]:
            retorno = -1

        # caso contrario, insira { identificacao : ([], senha, permissao) } no dicionario e retorne 0
        else:
            self.itens[request.identificacao] = ([], request.senha, request.permissao)
            retorno = 0
        
        return ident_pb2.CreateReply(retorno=retorno)

    def acesso(self, request, context): # procedimento de verificacao de acesso
        
        # para todos os usuarios no dicionario, se o vetor for igual ao vetor informado, retorne a permissao do usuario
        for value in self.itens.values():
            if value[0] == request.vetor:
                return ident_pb2.AccessReply(permissao=value[2])

        # se nao encontrar, retorne NE
        return ident_pb2.AccessReply(permissao="NE")

    def termino(self, request, context): # procedimento de termino do servidor de identidades
        retorno = len(self.itens) - 1
        server.stop(5)
        return ident_pb2.TerminoReply(retorno=retorno)


ident_pb2_grpc.add_IdentidadesServicer_to_server(Ident(), server) # associo o servico ao servidor

server.add_insecure_port('{}:{}'.format(hostname, sys.argv[1])) # associo um ip e uma porta ao servidor

server.start() # inicio o servidor
server.wait_for_termination() # aguarda o comando para parar o servidor