import socket

s_ip = 'localhost'
s_port = 5566

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((s_ip, s_port))
print('listen at {}:{}'.format(s_ip, s_port))
server.listen(2)

(client, (c_ip, c_port)) = server.accept()
print('{} connected'.format(c_ip))
cmd = '';
while True:
    try:
        cmd = input('$ ').strip()
    except EOFError:
        break;
    if not cmd:
        continue
    client.send(cmd.encode())
    if cmd == 'exit':
        break
    print(client.recv(1024).decode('utf-8'))

client.close()
server.close()
