import socket
import threading

host = '192.168.1.109'
porta = 5000

clientes = []

def cliente(conn, ender):
    print('cliente conectado: ', ender)
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            print("cliente:", ender, " mensagem:", data.decode())
            conn.sendall(data)
        
        except:
            break
    
    print('cliente desconectado: ', ender)
    conn.close()
    clientes.remove(conn)


metodoSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
metodoSocket.bind((host, porta))
metodoSocket.listen(3)

print('aguardando conexão do cliente...')

while True:
    conn, ender = metodoSocket.accept()
    clientes.append(conn)
    print('conectado em: ', ender)

    thread = threading.Thread(target=cliente, args=(conn, ender))
    thread.start()
