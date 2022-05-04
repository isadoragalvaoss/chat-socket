import socket
import _thread
import threading
from datetime import datetime
import sys



class Server():

    def __init__(self):

        # Para lembrar os usuários
        self.users_table = {}

        # Cria a TCP/IP socket e liga o Socket a porta
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('localhost', int(sys.argv[1]))
        self.socket.bind(self.server_address)

        #faz o socket pronto para aceitar conexões
        self.socket.listen(10)
        print('Starting up on {} port {}'.format(*self.server_address))
        self._wait_for_new_connections()

    def _wait_for_new_connections(self):
        while True:
            connection, _ = self.socket.accept()

            #enviar o nome da sala para o client
            connection.sendall(bytes(sys.argv[3], encoding='utf-8'))
            _thread.start_new_thread(self._on_new_client, (connection,))
                 

    def _on_new_client(self, connection):
        try:
            if len(self.users_table) < int(sys.argv[2]):
                connection.sendall(bytes(sys.argv[3], encoding='utf-8'))
                # Declare the client's name
                client_name = connection.recv(64).decode('utf-8')
                self.users_table[connection] = client_name
                print(f'{self._get_current_time()} {client_name} entrou em {sys.argv[3]} !!')

                while True:
                    data = connection.recv(64).decode('utf-8')
                    if data != '':
                        self.multicast(data, owner=connection)
                    else:
                        return
            else:
                connection.sendall(bytes('SALA CHEIA!', encoding='utf-8'))

        except:
            print(f'{self._get_current_time()} {client_name} saiu de {sys.argv[3]} !!')
            self.users_table.pop(connection)
            connection.close()

    def _get_current_time(self):
        return datetime.now().strftime("%H:%M:%S")

    def multicast(self, message, owner=None):
        #enviar mensagem com hora exata, nome e mensagem de cada usuário
        for conn in self.users_table:
            data = f'{self._get_current_time()} {self.users_table[owner]}: {message}'
            conn.sendall(bytes(data, encoding='utf-8'))  


if __name__ == "__main__":
    Server()