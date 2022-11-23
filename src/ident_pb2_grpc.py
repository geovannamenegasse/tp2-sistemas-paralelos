# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ident_pb2 as ident__pb2


class IdentificadorStub(object):
    """Servico para consulta de dados.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.autenticacao = channel.unary_unary(
                '/ident.Identificador/autenticacao',
                request_serializer=ident__pb2.AuthRequest.SerializeToString,
                response_deserializer=ident__pb2.AuthReply.FromString,
                )
        self.criacao = channel.unary_unary(
                '/ident.Identificador/criacao',
                request_serializer=ident__pb2.CreateRequest.SerializeToString,
                response_deserializer=ident__pb2.CreateReply.FromString,
                )
        self.acesso = channel.unary_unary(
                '/ident.Identificador/acesso',
                request_serializer=ident__pb2.AccessRequest.SerializeToString,
                response_deserializer=ident__pb2.AccessReply.FromString,
                )
        self.termino = channel.unary_unary(
                '/ident.Identificador/termino',
                request_serializer=ident__pb2.TerminoRequest.SerializeToString,
                response_deserializer=ident__pb2.TerminoReply.FromString,
                )


class IdentificadorServicer(object):
    """Servico para consulta de dados.
    """

    def autenticacao(self, request, context):
        """faz uma consulta nos servidores de armazenamento
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def criacao(self, request, context):
        """faz uma consulta nos servidores de armazenamento
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def acesso(self, request, context):
        """faz uma consulta nos servidores de armazenamento
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def termino(self, request, context):
        """termina a conexao com os servidores de armazenamento e termina o servidor que contêm este servico
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IdentificadorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'autenticacao': grpc.unary_unary_rpc_method_handler(
                    servicer.autenticacao,
                    request_deserializer=ident__pb2.AuthRequest.FromString,
                    response_serializer=ident__pb2.AuthReply.SerializeToString,
            ),
            'criacao': grpc.unary_unary_rpc_method_handler(
                    servicer.criacao,
                    request_deserializer=ident__pb2.CreateRequest.FromString,
                    response_serializer=ident__pb2.CreateReply.SerializeToString,
            ),
            'acesso': grpc.unary_unary_rpc_method_handler(
                    servicer.acesso,
                    request_deserializer=ident__pb2.AccessRequest.FromString,
                    response_serializer=ident__pb2.AccessReply.SerializeToString,
            ),
            'termino': grpc.unary_unary_rpc_method_handler(
                    servicer.termino,
                    request_deserializer=ident__pb2.TerminoRequest.FromString,
                    response_serializer=ident__pb2.TerminoReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ident.Identificador', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Identificador(object):
    """Servico para consulta de dados.
    """

    @staticmethod
    def autenticacao(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ident.Identificador/autenticacao',
            ident__pb2.AuthRequest.SerializeToString,
            ident__pb2.AuthReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def criacao(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ident.Identificador/criacao',
            ident__pb2.CreateRequest.SerializeToString,
            ident__pb2.CreateReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def acesso(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ident.Identificador/acesso',
            ident__pb2.AccessRequest.SerializeToString,
            ident__pb2.AccessReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def termino(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ident.Identificador/termino',
            ident__pb2.TerminoRequest.SerializeToString,
            ident__pb2.TerminoReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)