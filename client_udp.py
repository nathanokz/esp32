import socket
import threading

host = '192.168.1.109'
porta = 5000

nome = "cliente_udp"

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

cliente.sendto(nome.encode(), (host, porta))

def receber():
    while True:
        try:
            data, _ = cliente.recvfrom(1024)
            print(data.decode())
        except:
            break

thread = threading.Thread(target=receber)
thread.daemon = True
thread.start()

while True:
    mensagem = input('digite uma mensagem: ')

    if mensagem.startswith("/nick "):
        nome = mensagem.split(" ", 1)[1]
        print("nome alterado para: ", nome)
        cliente.sendto(nome.encode(), (host, porta))

    elif mensagem == "/sair":
        cliente.sendto(f"{nome} saiu do servidor".encode(), (host, porta))
        break

    else:
        cliente.sendto(f"{nome}: {mensagem}".encode(), (host, porta))

print("fechando conexão")
cliente.close()
