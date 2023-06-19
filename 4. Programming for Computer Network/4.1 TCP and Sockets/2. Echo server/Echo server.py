import socket
port = 1235
address = "127.0.0.1"
BUFF_SIZE = 1024

# Create a socket object name 'server'
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((address,port))
server.listen(5)
print("Listening...")

while True:
        con, addr = server.accept()
        print("Connection address is ", addr)
        data = con.recv(BUFF_SIZE)
        print(data.decode("utf-8"))
        con.send(data)