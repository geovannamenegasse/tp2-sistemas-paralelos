import grpc
import sys

import pares_pb2
import pares_pb2_grpc

import ident_pb2
import ident_pb2_grpc

from concurrent import futures

import socket
hostname = socket.gethostname() # caso seja tudo na mesma maquina, pode-se mudar para "localhost"

server = grpc.server(futures.ThreadPoolExecutor(max_workers=1)) # crio servidor

class Pares(pares_pb2_grpc.ParesServicer): 

    stub = ident_pb2_grpc.IdentidadesStub(grpc.insecure_channel(sys.argv[2])) # crio um stub para o servidor de identidades

    itens = {}
    
    def insercao (self, request, context): # insercao de um usuario
        response = self.stub.acesso(ident_pb2.AccessRequest(vetor=request.vetor))   
        retorno = 0

        if response.permissao == "RW":
            self.itens[request.chave] = request.valor
            retorno = 0
        elif response.permissao == "RO": 
            retorno = -1
        elif response.permissao == "NE": 
            retorno = -2
        elif response.permissao == "SP": 
            retorno = -3
                
        return pares_pb2.InsertReply(retorno=retorno)

    def consulta (self, request, context): # consulta por uma chave
        response = self.stub.acesso(ident_pb2.AccessRequest(vetor=request.vetor))   
        retorno = "null"

        if response.permissao == "RW" or response.permissao == "RO":
            retorno = self.itens[request.chave]

        return pares_pb2.SearchReply(valor=retorno)

    def termino(self, request, context): # procedimento de termino do servidor de pares
        server.stop(5)
        return pares_pb2.TerminoReply(retorno=0)


pares_pb2_grpc.add_ParesServicer_to_server(Pares(), server) # associo o servico ao servidor

server.add_insecure_port('{}:{}'.format(hostname, sys.argv[1])) # associo um ip e uma porta ao servidor

server.start() # inicio o servidor
server.wait_for_termination() # aguarda o comando para parar o servidor