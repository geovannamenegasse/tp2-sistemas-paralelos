import grpc
import sys

import ident_pb2
import ident_pb2_grpc

if __name__ == '__main__':
    with grpc.insecure_channel(sys.argv[1]) as channel:
        stub = ident_pb2_grpc.IdentificadorStub(channel)
        vetor_atual = []

        while True:
            entrada = input().split(' ')

            if entrada[0] == "A":# insercao de um item no servidor
                response = stub.autenticacao(ident_pb2.AuthRequest(identificacao=entrada[1], senha=int(entrada[2])))
                print(response.retorno)
                if response.retorno == 0:
                    vetor_atual = response.vetor

            if entrada[0] == "C": # consulta de um item no servidor
                response = stub.criacao(ident_pb2.CreateRequest(identificacao=entrada[1], senha=int(entrada[2]), permissao=entrada[3], vetor=vetor_atual))
                print(response.retorno)

            if entrada[0] == "V": # consulta de um item no servidor
                response = stub.acesso(ident_pb2.AccessRequest(vetor=vetor_atual))
                print(response.permissao)

            if entrada[0] == "F": # comando para parar o servidor
                response = stub.termino(ident_pb2.TerminoRequest())
                print(0)
                break
