import socket


class Server:
    def __init__(self, port: int):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # create socket
        self.sock.bind(('localhost', port))                            # open socket

    def run(self):
        clients = []                                                   # create users array
        while True:
            data, addr = self.sock.recvfrom(1024)                      # receive data and address
            print(addr)                                                # addresses of use send messages
            if addr not in clients:
                clients.append(addr)                                   # add address client to clients

            for client in clients:
                if client == addr:
                    continue
                self.sock.sendto(data, client)                         # send data to other use


if __name__ == '__main__':
    server = Server(9090)
    server.run()