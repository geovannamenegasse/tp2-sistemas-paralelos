import grpc
import sys

import armazenamento_pb2
import armazenamento_pb2_grpc

from concurrent import futures

server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))# crio servidor


class Armazem(armazenamento_pb2_grpc.ArmazemServicer):#classe responsavel pelo armazenamento feito no servidor
    itens = {}#dicionario que ira armazenar os dados inseridos no servidor. Cada dado e armazenado no formato: (descricao, valor)

    def insercao(self, request, context):#procedimento de insercao a ser exportado
        
        if request.ch in self.itens.keys():#verifico se a chave passada ja existe e atribuo o valor de retorno da requisicao
            retorno = -1
        else:
            self.itens[request.ch] = (request.desc, request.val)
            retorno = 0
        
        return armazenamento_pb2.InsercaoReply(retorno=retorno)

    def consulta(self, request, context):#procedimento de consulta a ser exportado
        
        if request.ch in self.itens.keys():#verifico se a chave passada ja existe e atribuo os valores de retorno da requisicao
            desc = self.itens[request.ch][0]
            val = self.itens[request.ch][1]
        else:
            desc = ""
            val = 0
        
        return armazenamento_pb2.ConsultaReply(desc=desc, val=val)

    def termino(self, request, context):#procedimento de termino a ser exportado
        server.stop(5)
        return armazenamento_pb2.TerminoReply(retorno=0)


armazenamento_pb2_grpc.add_ArmazemServicer_to_server(Armazem(), server)# associo o servico ao servidor

server.add_insecure_port('{}:{}'.format("localhost", sys.argv[1]))# associo um ip e uma porta ao servidor

server.start()# inicio o servidor
server.wait_for_termination()# aguarda o comando para parar o servidor