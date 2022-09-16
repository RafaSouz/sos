from concurrent import futures
import logging
import const
import grpc
import server_pb2
import server_pb2_grpc

cont = 0
calc = 0

class ScoreData(server_pb2_grpc.ScoreDataServicer):

    def ConsultScore (self, request, context):
        return server_pb2.ValueScore(score=cont) 

    def CalcScore (self, request, context):
        global calc
        calc = request.value
        return UpdateScore()

    def UpdateScore (self, request, context):
        global cont
        global calc
        cont = calc + cont
        return server_pb2.ValueScore(score=cont) 

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server_pb2_grpc.add_ScoreDataServicer_to_server(ScoreData(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
