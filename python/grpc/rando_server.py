from concurrent import futures
import logging
import random

import grpc
import rando_pb2
import rando_pb2_grpc

class Rando(rando_pb2_grpc.RandoServicer):
    def GetRando(self, request, context):
        return rando_pb2.RandoResponse(res=99)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rando_pb2_grpc.add_RandoServicer_to_server(Rando(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()

