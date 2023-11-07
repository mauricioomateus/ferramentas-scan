import socket, sys, requests

ip = sys.argv[1]

file = open(sys.argv[2], "r")

for linha in file.readlines():
    porta = linha.split(":")
    porta = int(porta[1].strip())
    try:
        socket.setdefaulttimeout(15)
        s = socket.socket()
        s.connect((ip, porta))
        if porta == 80 or porta == 443:
            http_request = 'GET HTPP/1.1 \r\n'
            s.send(http_request.encode())

        banner = s.recv(2048)
        banner = banner.decode()
        s.close()
        print("[+] " + ip + " >>> " + str(banner))

        arquivo = open("servicos_" + ip + ".txt", "+a")
        arquivo.write("Servico da porta: " + str(porta))
        arquivo.write(str(banner) + '\n')
        arquivo.close()
    except:
        print("Nao foi possivel detectar o banner")
