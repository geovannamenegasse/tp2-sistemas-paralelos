import grpc
import sys

import consulta_pb2
import consulta_pb2_grpc

if __name__ == '__main__':
    with grpc.insecure_channel(sys.argv[1]) as channel:
        stub = consulta_pb2_grpc.ConsultadorStub(channel)

        while True:
            entrada = input().split(',')

            if entrada[0] == "C": # consulta de um item no servidor
                response = stub.consulta(consulta_pb2.ConsultaRequest(ch=int(entrada[1])))
                print(response.nome + "," + str(response.matr) + "," + response.curso + "," + str(response.cred))

            if entrada[0] == "T": # comando para parar o servidor
                response = stub.termino(consulta_pb2.TerminoRequest())
                print(0)
                break