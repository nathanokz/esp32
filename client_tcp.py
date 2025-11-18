import socket
import threading

host = '192.168.1.109'  
porta = 5000

nome = "cliente_tcp"

metodoSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
metodoSocket.connect((host, porta))

def receber():
    while True:
        try:
            data = metodoSocket.recv(1024)
            if not data:
                print("servidor desconectado.")
                break
            print(data.decode())

        except:
            break

thread = threading.Thread(target=receber)
thread.daemon = True
thread.start()

while True:
    mensagem = input('digite uma mensagem:')

    if mensagem.startswith("/nick "):
        nome = mensagem.split(" ", 1)[1]
        print("nome alterado para: ", nome)

    elif mensagem == "/sair":
        metodoSocket.send(f"{nome} saiu do servidor".encode())
        break

    else:
        metodoSocket.send(f"{nome}: {mensagem}".encode())

metodoSocket.close()
print("fechando conexão")
