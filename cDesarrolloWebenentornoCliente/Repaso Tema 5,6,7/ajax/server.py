#!C:\Users\brian\AppData\Local\Microsoft\WindowsApps\python3.11.exe

import json
from random import randint

# Enviar json a js
print("Content-Type: text/html")
print("")

peliculas = ["1.jpeg","2.png","3.png","4.png","5.png"]
numero: int = randint(0,4)
peli = peliculas[numero]
respuesta = json.dumps(peli)

print(respuesta)
