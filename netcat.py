import getopt
import socket
import sys
from threading import Thread

HOST = ""
PORT = 0

def send_message(connection, message):
    connection.send(message.encode())
    connection.close()

def main():
    global HOST, PORT
    args = sys.argv[1:]
    opts, _ = getopt.getopt(sys.argv[1:], "h:p:", ["host=", "port="])
    for key, value in opts:
        if key == "-h" or key == "--host":
            HOST = value
        if key == "-p" or key == "--port":
            PORT = int(value)
    
    sock = socket.socket()
    sock.bind((HOST, PORT))
    try:
        while(True):
            con, _ = sock.accept()
            msg = eval(input("Insert Message: "))
            Thread(target=send_message, args=(con, msg,)).start()
    except:
        sock.close()

if __name__ == "__main__":
    main()