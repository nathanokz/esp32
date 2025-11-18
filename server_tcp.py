import socket #bilbioteca utilizada para comunicação entre computadores
import threading #biblioteca utilizada para executar multiplas tarefas ao mesmo tempo

host = '192.168.1.109' #ip do servidor
porta = 5000 #porta do servidor 

clientes = [] #lista de clientes conectados

def cliente(conn, ender): #função para comunicação com o cliente
    print('cliente conectado: ', ender) #mostra o cliente que se conectou
    while True: #inicia o loop
        try: #tenta realizar o bloco
            data = conn.recv(1024) #recebe mensagens de ate 1024 bytes 
            if not data: #se não receber nada
                break #finaliza o loop
            print("cliente:", ender, " mensagem:", data.decode()) #printa as informações do cliente ja decodificada byte -> string
            conn.sendall(data) #envia de volta para o cliente
        
        except: #se não conseguir realizar o bloco cai aqui
            break #finaliza o codigo
    
    print('cliente desconectado: ', ender) #mostra caso o cliente tenha se desconectado 
    conn.close() #fecha a conexão
    clientes.remove(conn) #remove o cliente da lista de clientes

metodoSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria um socket tcp
metodoSocket.bind((host, porta)) #conecta o socket tcp no host e porta especificados
metodoSocket.listen(3) #escuta pelo menos 3 clientes no servidor

print('aguardando conexão do cliente...') #printa enquando aguarda alguem se conectar

while True: #inicia o loop
    conn, ender = metodoSocket.accept() #aceita a conexão tcp do cliente
    clientes.append(conn) #acumula o cliente dentro da lista clientes
    print('conectado em: ', ender) #informa o endereço do cliente esta conectado

    thread = threading.Thread(target=cliente, args=(conn, ender)) #cria a thread que vai executar a função cliente
    thread.start() #inicia a thread
