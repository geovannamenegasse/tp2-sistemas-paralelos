import grpc
import sys

import pares_pb2
import pares_pb2_grpc

import ident_pb2
import ident_pb2_grpc

if __name__ == '__main__':

    with grpc.insecure_channel(sys.argv[2]) as channel:
        with grpc.insecure_channel(sys.argv[1]) as channel2:

            stub = pares_pb2_grpc.ParesStub(channel)
            stub2 = ident_pb2_grpc.IdentidadesStub(channel2)
            vetor_atual = []

            for entrada in sys.stdin:
                entrada = (entrada.split('\n'))[0].split(' ')

                if entrada[0] == "I": # insere um usuario no servidor
                    if vetor_atual == []:
                        print("-9")
                    else:
                        response = stub.insercao(pares_pb2.InsertRequest(chave=int(entrada[1]), valor=entrada[2], vetor=vetor_atual))
                        print(response.retorno)

                if entrada[0] == "C": # consulta um usuario no servidor
                    response = stub.consulta(pares_pb2.SearchRequest(chave=int(entrada[1]),vetor=vetor_atual))
                    print(response.valor)

                if entrada[0] == "T": # para a execucao do servidor de pares
                    response = stub.termino(pares_pb2.TerminoRequest())
                    print(response.retorno)
                    break

                if entrada[0] == "A": # autenticacao de um usuario no servidor de identidades
                    response = stub2.autenticacao(ident_pb2.AuthRequest(identificacao=entrada[1], senha=int(entrada[2])))
                    
                    print(response.retorno)
                   
                    if response.retorno == 0:
                        vetor_atual = response.vetor
                    elif response.retorno == -1:
                        vetor_atual = []

                if entrada[0] == "F": # para a execucao do servidor de identidades
                    response = stub2.termino(ident_pb2.TerminoRequest())
                    print(response.retorno)
                    break
