import threading
import socket
import pickle
from time import sleep
import os

class Packet:
    def __init__(self):
        self.is_file = False
        self.file_name = ""
        self.messageBytes = b''
    def decode_message(self):
        if self.is_file:
            os.system('cls||clear')
            with open(f"{self.file_name}", "wb") as f:
                for i in range(0,15):
                    loading_bar = "[]"
                    print("file download:" + loading_bar[0] + (i*"*") + loading_bar[1] + " "  + f"{i + 1}/15")
                    sleep(.3)
                    if i != 14:
                        os.system('cls||clear')
                    else:
                        print("download comlete!")
                f.write(self.messageBytes)

        else:
            print(self.messageBytes.decode() + "  - From Peer") 
    

