import network
import socket
import time

rede = network.WLAN(network.STA_IF)
rede.active(True)

rede.connect('Baco', 'maicon142020')

while not rede.isconnected():
    print('conectando ao wifi...')
    time.sleep(1)
    
print('conectado!')

host = '192.168.1.109'
porta = 5000

metodoSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
metodoSocket.connect((host, porta))

print('conectado ao servidor tcp!')

while True:
    mensagem = 'ola!'
    metodoSocket.send(mensagem.encode())
    
    data = metodoSocket.recv(1024)
    if data:
        print('mensagem do servidor: ', data.decode())

print('fechando conexão...')
metodoSocket.close()


