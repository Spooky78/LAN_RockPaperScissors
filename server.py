import pickle
import socket
from _thread import *
from game import Game

server = "192.168.0.93"
port = 5555
currentSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    currentSocket.bind((server, port))
except socket.error as e:
    str(e)

currentSocket.listen()
print("Waiting for connection, Server started!")

connected = set()
games = {}
idCount = 0


def threadedClient(conn, player, gameId):
    global idCount
    conn.send(str.encode(str(player)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            # check if game still exists, if not make payer choose options, if not get next move
            if gameId in games:
                game = games[gameId]
                if not data:
                    break
                else:
                    if data == "reset":
                        print("resetting")
                        game.resetMoves()
                    elif data != "get":
                        game.play(player, data)

                    reply = game
                    conn.sendall(pickle.dumps(reply))
            else:
                break
        except:
            break

    print("Lost connection")
    # may run into issuses if both players try to exit game at same time
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass

    idCount -= 1
    conn.close()


while True:
    conn, address = currentSocket.accept()
    print("Connected to:", address)

    idCount += 1
    player = 0
    gameId = (idCount - 1) // 2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating new game...")
    else:
        games[gameId].ready = True
        player = 1

    start_new_thread(threadedClient, (conn, player, gameId))
