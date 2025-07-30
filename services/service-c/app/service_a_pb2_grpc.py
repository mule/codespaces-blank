from service_c.service_a_pb2_grpc import *
        + f' but the generated code in service_a_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ServiceAStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CallService = channel.unary_unary(
                '/service_a.ServiceA/CallService',
                request_serializer=service__a__pb2.Request.SerializeToString,
                response_deserializer=service__a__pb2.Response.FromString,
                _registered_method=True)


class ServiceAServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CallService(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServiceAServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CallService': grpc.unary_unary_rpc_method_handler(
                    servicer.CallService,
                    request_deserializer=service__a__pb2.Request.FromString,
                    response_serializer=service__a__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'service_a.ServiceA', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('service_a.ServiceA', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ServiceA(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CallService(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/service_a.ServiceA/CallService',
            service__a__pb2.Request.SerializeToString,
            service__a__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
