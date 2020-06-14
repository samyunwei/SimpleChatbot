import grpc
import server.pb.SimpleChatbot_pb2_grpc
import server.pb.SimpleChatbot_pb2
from concurrent import futures
import logging
import server.SimpleChatBotServer
import server.SimpleChatProcessor
import sys

ADDR = "[::]:50052"


def serve():
    s = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    processor = server.SimpleChatProcessor.SimpleChatProcessor()
    server.pb.SimpleChatbot_pb2_grpc.add_SimpleChatBotServerServicer_to_server(
        server.SimpleChatBotServer.SimpleChatBotServicerImp(processor), s)
    s.add_insecure_port(ADDR)
    s.start()
    print("SimpleChatBot Begin to Serve at:%s" % ADDR)
    s.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
