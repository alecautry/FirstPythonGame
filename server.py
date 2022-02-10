import socket  
from _thread import *
import sys

server = "192.168.1.5" #  ip of machine running server
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server,port))  #creating the socket

except socket.error as e:
    str(e)

s.listen(4) #opens up the port, 4 people can connect
print("Waiting for connection, Server Started")


#threaded function
def threaded_client(conn): # a thread is another proccess running in the background
    conn.send(str.encode("Connected"))
    replay = ""

    while True:
        try:
            data = conn.recv(2048) # 2048 bits
            reply = data.decode("utf-8")

            if not data: #lost connection to client or left
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ",reply)

            conn.sendall(str.encode(reply))
        except:
            print("Some error, break")
            break

    print("Lost connection")
    conn.close()
while True: #continue to look for connections
    conn, addr = s.accept() #accept any incoming transmission
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,))