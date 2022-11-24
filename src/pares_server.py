import grpc
import sys
import secrets

import pares_pb2
import pares_pb2_grpc

import ident_pb2
import ident_pb2_grpc

from concurrent import futures

server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))# crio servidor

class Pares(pares_pb2_grpc.ArmazenamentoServicer):#classe responsavel pelo armazenamento feito no servidor
    itens = {}#dicionario que ira armazenar os dados inseridos no servidor. Cada dado e armazenado no formato: (descricao, valor)

    def insercao (self, request, context):#procedimento de insercao a ser exportado
        print(request)       
        # print(ident_pb2_grpc.acesso(ident_pb2.AccessRequest(vetor=[]))) 
        return pares_pb2.InsertReply(retorno=0)

    def consulta (self, request, context):#procedimento de consulta a ser exportado
        print(request)
        return pares_pb2.SearchReply(valor="oi")

    def termino(self, request, context):#procedimento de termino a ser exportado
        server.stop(5)
        return pares_pb2.TerminoReply(retorno=0)


pares_pb2_grpc.add_ArmazenamentoServicer_to_server(Pares(), server)# associo o servico ao servidor
# ident_pb2_grpc.add_IdentificadorServicer_to_server(Ident(), server)# associo o servico ao servidor

server.add_insecure_port('{}:{}'.format("localhost", sys.argv[1]))# associo um ip e uma porta ao servidor

server.start()# inicio o servidor
server.wait_for_termination()# aguarda o comando para parar o servidor