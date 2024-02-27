#!C:\Users\brian\AppData\Local\Microsoft\WindowsApps\python3.11.exe
import sys
import json

print("Content-Type: text/html")
print("")


number: int = json.loads(sys.stdin.read())
number = int(number) * 5
print(f"El numero multiplicado por 5 es: {number}")
