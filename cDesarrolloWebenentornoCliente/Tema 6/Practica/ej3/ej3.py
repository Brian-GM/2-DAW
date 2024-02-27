#!C:\Users\brian\AppData\Local\Microsoft\WindowsApps\python3.11.exe

import mysql.connector
import json


print("Content-Type: text/html")
print("")


mydb = mysql.connector.connect(
    host="localhost", user="brian", password="brian", database="uwu"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM products")


products = mycursor.fetchall()

product_list = []
for product in products:
    product_dict = {
        "title": product[1],
        "img": product[2],
        "description": product[3],
        "precio": product[4],
    }
    product_list.append(product_dict)

json_data = json.dumps(product_list)
print(json_data)
