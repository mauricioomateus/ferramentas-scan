import socket, sys, threading


def portscan(porta):
    meuSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    meuSocket.settimeout(0.5)
     if meuSocket.connect_ex((ip,porta)) == 0:
            print("Porta: " + str(porta) + " [ABERTA]")
            meuSocket.close()

        #salvar resultado
        arquivo = open("portas_" + ip + ".txt", "a+")
        arquivo.write("Porta: " + str(porta) + "[ABERTA]" + '\n')
        arquivo.close()

r = 1 #variavel para interação

if len(sys.argv) > 1:
    ip = sys.argv[1]    
    print("[+] Varrendo o host: {}".format(ip))
    for porta in range(1,65535):
        t = threading.Thread(target=portscan, kwargs={'porta':r})
        r += 1
        t.start()
else:
    print("[+] Informe o Ip para realizar o scan [+]")
    exit(0)
