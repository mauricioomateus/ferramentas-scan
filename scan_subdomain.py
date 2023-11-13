import requests, sys

def scanner_domain(dominio, subdominio):
    url = f'https://{subdominio}.{dominio}'
    
    try:
        requests.get(url, timeout=2)
        print(f'[+] {url} [200 Ok]')
    except requests.ConnectionError:
        pass 

if __name__ == '__main__':
    dominio = sys.argv[1]
    print('\n')

    wordlist = sys.argv[2]
    with open(wordlist) as file:
        nome = file.read()
        subdominio = nome.splitlines()
    
    print("Iniciando o Scan de Subdominios...")
    for sub_dominio in subdominio:
       scanner_domain(dominio, sub_dominio)
    print("Fim do Scanner")
