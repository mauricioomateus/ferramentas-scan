import socket, sys

if len(sys.argv) > 1:
    print("[+] Varrendo o host: ")
    ip = sys.argv[1]
    print("Inciando o Scan no Host {}...".format(ip))
    for porta in range(1,65535):
        meuSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if meuSocket.connect_ex((ip,porta)) == 0:
            print("Porta: " + str(porta) + " [ABERTA]")
            meuSocket.close()
else:
    print("[+] Informe o Ip para realizar o scan [+]")
    exit(0)
