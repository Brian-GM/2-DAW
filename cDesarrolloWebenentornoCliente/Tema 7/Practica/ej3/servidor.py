#!C:\Users\brian\AppData\Local\Microsoft\WindowsApps\python3.11.exe
import sys
import json

data = json.loads(sys.stdin.read())

array1 = ["Pedro", "Rosa", "Pablo", "Laura", "David"]
array2 = ["ama", "mata", "juega", "acompaña", "ayuda"]
array3 = ["Juan", "María", "Luisa", "Carlos", "Ana"]


frase1 = ""
frase2 = ""
frase3 = ""

for i, text in enumerate(array1):
    if i == int(data["campo1"]):
        frase1 = text

for i, text in enumerate(array2):
    if i == int(data["campo2"]):
        frase2 = text

for i, text in enumerate(array3):
    if i == int(data["campo3"]):
        frase3 = text

response_data = {"palabra1": frase1, "palabra2": frase2, "palabra3": frase3}

print("Content-Type: application/json")
print("")
print(json.dumps(response_data))
