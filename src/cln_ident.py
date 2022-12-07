import grpc
import sys

import ident_pb2
import ident_pb2_grpc

if __name__ == '__main__':

    with grpc.insecure_channel(sys.argv[1]) as channel:

        stub = ident_pb2_grpc.IdentidadesStub(channel)
        vetor_atual = []

        for entrada in sys.stdin:
            entrada = (entrada.split('\n'))[0].split(' ')

            if entrada[0] == "A": # autenticacao de um usuario no servidor
                response = stub.autenticacao(ident_pb2.AuthRequest(identificacao=entrada[1], senha=int(entrada[2])))

                print(response.retorno)
                
                if response.retorno == 0:
                    vetor_atual = response.vetor
                elif response.retorno == -1:
                    vetor_atual = []

            if entrada[0] == "C": # consulta por um usuario no servidor
                if vetor_atual == []:
                    print("-9")
                else:
                    response = stub.criacao(ident_pb2.CreateRequest(identificacao=entrada[1], senha=int(entrada[2]), permissao=entrada[3], vetor=vetor_atual))
                    print(response.retorno)

            if entrada[0] == "V": # verifica o acesso de um usuario no servidor
                if vetor_atual == []:
                    print("-9")
                else:
                    response = stub.acesso(ident_pb2.AccessRequest(vetor=vetor_atual))
                    print(response.permissao)

            if entrada[0] == "F": # para a execucao do servidor
                response = stub.termino(ident_pb2.TerminoRequest())
                print(response.retorno)
                break
