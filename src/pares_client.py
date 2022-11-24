import grpc
import sys

import pares_pb2
import pares_pb2_grpc

import ident_pb2
import ident_pb2_grpc

if __name__ == '__main__':
    with grpc.insecure_channel(sys.argv[2]) as channel:
        with grpc.insecure_channel(sys.argv[1]) as channel2:
            stub = pares_pb2_grpc.ArmazenamentoStub(channel)
            stub2 = ident_pb2_grpc.IdentificadorStub(channel2)
            vetor_atual = []

            while True:
                entrada = input().split(' ')

                if entrada[0] == "I": # consulta de um item no servidor
                    response = stub.insercao(pares_pb2.InsertRequest(chave=int(entrada[1]), valor=entrada[2], vetor=vetor_atual))
                    print(response.retorno)

                if entrada[0] == "C": # consulta de um item no servidor
                    response = stub.consulta(pares_pb2.SearchRequest(chave=int(entrada[1])))
                    print(response.permissao)

                if entrada[0] == "T": # comando para parar o servidor
                    response = stub.termino(pares_pb2.TerminoRequest())
                    print(0)
                    break

                if entrada[0] == "A":# insercao de um item no servidor
                    response = stub2.autenticacao(ident_pb2.AuthRequest(identificacao=entrada[1], senha=int(entrada[2])))
                    print(response.retorno)
                    if response.retorno == 0:
                        vetor_atual = response.vetor

                if entrada[0] == "F": # comando para parar o servidor
                    response = stub2.termino(ident_pb2.TerminoRequest())
                    print(0)
                    break
