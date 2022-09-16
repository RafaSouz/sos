from __future__ import print_function
import logging
from urllib import response
import grpc
import server_pb2
import server_pb2_grpc
import sys
import const

def ShowScore(self, request, context):
    with grpc.insecure_channel(const.CHAT_SERVER_HOST) as channel:
        stub = server_pb2_grpc.ScoreDataStub(channel)
        response = stub.ConsultScore(server_pb2.EmptyMessage())
        print(f'Score Atual: {response}\n')

def UpdateScore(self, request, context):
    with grpc.insecure_channel(const.CHAT_SERVER_HOST) as channel:
        stub = server_pb2_grpc.ScoreDataStub(channel)
        new = stub.UpdateScore(server_pb2.EmptyMessage())
        print(f'Novo Score: {new}\n')

if __name__ == '__main__':
    logging.basicConfig()
    while True:
        choice = int(input("Digite 1 para ver o Score e 2 para aumentar o Score: "))
        if(choice == 1):
            ShowScore()
        else:   
            UpdateScore()
