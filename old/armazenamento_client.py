import grpc
import sys

import armazenamento_pb2
import armazenamento_pb2_grpc

if __name__ == '__main__':
    with grpc.insecure_channel(sys.argv[1]) as channel:
        stub = armazenamento_pb2_grpc.ArmazemStub(channel)

        while True:
            entrada = input().split(',')

            if entrada[0] == "I":# insercao de um item no servidor
                response = stub.insercao(armazenamento_pb2.InsercaoRequest(ch=int(entrada[1]), desc=entrada[2], val=int(entrada[3])))
                print(response.retorno)

            if entrada[0] == "C": # consulta de um item no servidor
                response = stub.consulta(armazenamento_pb2.ConsultaRequest(ch=int(entrada[1])))

                if (response.val == 0) and (response.desc == ""):
                     print(-1)
                else:
                    print(str(response.desc) + "," + str(response.val))

            if entrada[0] == "T": # comando para parar o servidor
                response = stub.termino(armazenamento_pb2.TerminoRequest())
                print(0)
                break
