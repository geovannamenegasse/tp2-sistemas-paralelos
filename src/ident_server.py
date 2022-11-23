import grpc
import sys
import secrets

import ident_pb2
import ident_pb2_grpc

from concurrent import futures

server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))# crio servidor

class Ident(ident_pb2_grpc.IdentificadorServicer):#classe responsavel pelo armazenamento feito no servidor
    itens = {'super' : ([secrets.token_bytes(32)], int(sys.argv[2]), "SP")}#dicionario que ira armazenar os dados inseridos no servidor. Cada dado e armazenado no formato: (descricao, valor)

    def autenticacao(self, request, context):#procedimento de insercao a ser exportado
        print(request)
        if request.identificacao not in self.itens.keys() or self.itens[request.identificacao][1] != request.senha:
            retorno = -1
            vetor = [secrets.token_bytes(32)]
        else:
            retorno = 0
            if request.identificacao != 'super':
                self.itens[request.identificacao] = ([secrets.token_bytes(32)],request.senha,self.itens[request.identificacao][2])
            vetor = self.itens[request.identificacao][0]
        
        return ident_pb2.AuthReply(retorno=retorno, vetor=vetor)

    def criacao(self, request, context):#procedimento de consulta a ser exportado
        print(request)

        if request.vetor != self.itens['super'][0]:
            retorno = -1
        else:
            self.itens[request.identificacao] = ([], request.senha, request.permissao)
            retorno = 0
        
        return ident_pb2.CreateReply(retorno=retorno)

    def acesso(self, request, context):#procedimento de consulta a ser exportado
        print(request)
        
        for value in self.itens.values():
            if value[0] == request.vetor:
                return ident_pb2.AccessReply(permissao=value[2])
        
        return ident_pb2.AccessReply(permissao="NE")

    def termino(self, request, context):#procedimento de termino a ser exportado
        server.stop(5)
        return ident_pb2.TerminoReply(retorno=0)


ident_pb2_grpc.add_IdentificadorServicer_to_server(Ident(), server)# associo o servico ao servidor

server.add_insecure_port('{}:{}'.format("localhost", sys.argv[1]))# associo um ip e uma porta ao servidor

server.start()# inicio o servidor
server.wait_for_termination()# aguarda o comando para parar o servidor