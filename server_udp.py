import socket

host = '192.168.1.109'
porta = 5000

clientes = {}

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host, porta))

print('aguardando mensagem...')

while True:
    data, ender = server.recvfrom(1024)
    mensagem = data.decode().strip()

    if ender not in clientes:
        clientes[ender] = mensagem
        print(f"novo cliente: {mensagem} - {ender}")
        for cliente_ender in clientes:
            if cliente_ender != ender:
                server.sendto(f"Servidor: {mensagem} entrou no chat.".encode(), cliente_ender)
        continue

    nome = clientes[ender]
    full_message = f"{nome}: {mensagem}"
    print(full_message)
    for cliente_ender in clientes:
        if cliente_ender != ender:
            server.sendto(full_message.encode(), cliente_ender)
