from __future__ import print_function
import logging
from urllib import response
import grpc
import server_pb2
import server_pb2_grpc
import sys
import const

def ShowScore():
    with grpc.insecure_channel(const.CHAT_SERVER_HOST) as channel:
        stub = server_pb2_grpc.ScoreDataStub(channel)
        response = stub.ConsultScore(server_pb2.EmptyMessage())
        print(f'Score Atual: {response}\n')

def UpdateScore(score):
    with grpc.insecure_channel(const.CHAT_SERVER_HOST) as channel:
        stub = server_pb2_grpc.ScoreDataStub(channel)

        calc = stub.CalcScore(server_pb2.ValueScore(score=score))
        print(f'Valor a ser adicionado: {calc.score}\n')

        new = stub.UpdateScore(server_pb2.EmptyMessage())
        print(f'Novo Score: {new}\n')

if __name__ == '__main__':
    logging.basicConfig()
    while True:
        choice = int(input("Digite 1 para ver o Score e 2 para aumentar o Score: "))
        if(choice == 1):
            ShowScore()
        else:
            score = int(input("Valor a ser adicionado ao score: "))
            if(score==0):
                print(f'Valor precisa ser maior que 0 \n')
            else:
                UpdateScore(score)
