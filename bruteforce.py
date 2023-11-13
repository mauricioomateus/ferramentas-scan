import hashlib

my_file = open("rockyou.txt", "r", encoding="ISO-8859-1")
count = 0
for password in my_file:
    hash_first = hashlib.md5(f"{password}".encode())
    hash_second = hashlib.md5(hash_first.encode()+b"segredo").hexdigest()
    if hash_second == "239i4rujfkcdowijdemenqwjfik3ec":
        print("deu bom com a senha: " + password)
        print("hash da senha gerado: " + hash_second)
        break
    else:
        print("deu ruim com a senha: "+password)
    count += 1
