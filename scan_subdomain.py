import requests, argparse, threading

parser = argparse.ArgumentParser()

parser.add_argument('--url', type=str, required=True)
parser.add_argument('--wordlist', type=str, required=True)
#parser.add_argument('-h', type=str, required=True)
valor = parser.parse_args()

def scanner_domain(dominio, subdominio):
    url = f'https://{subdominio}.{dominio}'
    
    try:
        requests.get(url, timeout=2)
        print(f'[+] {url}')
    except requests.ConnectionError:
        pass 
        
threads = []
if __name__ == '__main__':
    url = valor.url
    print('\n')

    wordlist = valor.wordlist
    with open(wordlist) as file:
        nome = file.read()
        subdominio = nome.splitlines()
    
    print("Iniciando o Scan de Subdominios...")
    for sub_dominio in subdominio:
        t = threading.Thread(target=scanner_domain, args=(url,sub_dominio)) #definindo a função que trabalhará com threads e seus parametros
        threads.append(t) #adicionando a função com paralelismo na lista        
        t.start() #iniciando os threads
    print("Fim do Scanner")
