import sys
sys.path.append("..")
from utils import *

HOST = "127.0.0.1" 
PORT = 65432 


def listenLoop(conn):
    
    while True:
        size = conn.recv(1024)
        if int.from_bytes(size, "big") == 0:
            break
        data = conn.recv(int.from_bytes(size, "big"))
        recievedPacket = pickle.loads(data)
        recievedPacket.decode_message()

sendPacket = Packet()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    x = threading.Thread(target=listenLoop, args=(conn,))
    x.start()
    while True:
        message = input()
        if message[0:2] == "cp":
            try:
                with open(message[3:], "rb") as f:
                    sendPacket.is_file = True
                    sendPacket.messageBytes = f.read()
                    sendPacket.file_name = message[3:]
                    data = pickle.dumps(sendPacket)
                    conn.send(int.to_bytes(len(data), 8))
                    conn.send(data)
            except Exception as e:
                print(e)
                print("File not found!")
        else:
            sendPacket.is_file = False
            sendPacket.messageBytes = message.encode()
            sendPacket.file_name = ""
            data = pickle.dumps(sendPacket)
            conn.send(int.to_bytes(len(data), 8))
            conn.send(data)