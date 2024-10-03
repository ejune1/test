from __future__ import print_function

import logging

import grpc
import rando_pb2
import rando_pb2_grpc

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to rando ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = rando_pb2_grpc.RandoStub(channel)
        response = stub.GetRando(rando_pb2.RandoRequest(req=1))
    print("Rando client received: " + str(response.res))


if __name__ == "__main__":
    logging.basicConfig()
    run()

