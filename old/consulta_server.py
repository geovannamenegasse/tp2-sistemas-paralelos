import grpc
import sys

import consulta_pb2
import consulta_pb2_grpc

import armazenamento_pb2
import armazenamento_pb2_grpc

from concurrent import futures

server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))# crio servidor

siga_channel = grpc.insecure_channel(sys.argv[2]) # Crio conexao com o siga
siga_stub = armazenamento_pb2_grpc.ArmazemStub(siga_channel)# Crio stub do siga

matricula_channel = grpc.insecure_channel(sys.argv[3]) # Crio conexao com o matricula
matricula_stub = armazenamento_pb2_grpc.ArmazemStub(matricula_channel)# Crio stub do matricula



class Consultador(consulta_pb2_grpc.ConsultadorServicer):# classe responsavel pelas consultas feitas no servidor

    def consulta(self, request, context):# procedimento de consulta a ser exportado

        siga_response = siga_stub.consulta(armazenamento_pb2.ConsultaRequest(ch=request.ch))

        if (siga_response.desc == "") and (siga_response.val == 0):# caso o siga nao encontre nada, retorno segundo regra do tp2
            return consulta_pb2.ConsultaReply(nome="", matr=0, curso="", cred=0)

        matricula_response = matricula_stub.consulta(armazenamento_pb2.ConsultaRequest(ch=siga_response.val))

        if (matricula_response.desc == "") and (matricula_response.val == 0):# caso o matricula nao encontre nada, retorno segundo regra do tp2
            return consulta_pb2.ConsultaReply(nome=siga_response.desc, matr=siga_response.val, curso="N/M", cred=0)

        return consulta_pb2.ConsultaReply(nome=siga_response.desc, matr=siga_response.val, curso=matricula_response.desc, cred=matricula_response.val)

    def termino(self, request, context):# procedimento de termino a ser exportado
        siga_response = siga_stub.termino(armazenamento_pb2.TerminoRequest()) # envio uma mensagem para terminar o siga
        siga_channel.close()# fecho a conexao com o siga

        matricula_response = matricula_stub.termino(armazenamento_pb2.TerminoRequest())# envio uma mensagem para terminar o matricula
        matricula_channel.close()# fecho a conexao com o matricula

        server.stop(10)
        return consulta_pb2.TerminoReply(retorno=siga_response.retorno + matricula_response.retorno)




consulta_pb2_grpc.add_ConsultadorServicer_to_server(Consultador(), server)# associo o servico ao servidor

server.add_insecure_port('{}:{}'.format("localhost", sys.argv[1]))# associo um ip e uma porta ao servidor

server.start()# inicio o servidor
server.wait_for_termination()# aguarda o comando para parar o servidor