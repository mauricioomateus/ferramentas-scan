import subprocess 

r = subprocess.run(["netsh", "wlan", "show", "network"],capture_output=True, text=True).stdout
lista = r.split("\n")

ssids = [k for k in lista if 'SSID' in k]
ssids = [v.strip() for k,v in (p.split(':') for p in lista if 'SSID' in p )]
print(ssids)
