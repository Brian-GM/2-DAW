import os

from src.inserts import insert_movies
from src.selects import select_movies_by_title
from src.deletes import delete_movies_between_dates
from src.updates import update_movie_by_id
from src.user_valorations import user_valorations
from src.ranking_film import ranking_film
from src.user_most_active import user_most_active


option: int = -1
while option != 0:
    os.system("clear")
    print("MENÚ")
    print("--------------------------------------------------------------")
    print("1.- Insertar película")
    print("2.- Buscar películas por título")
    print("3.- Eliminar película")
    print("4.- Modificar película por id")
    print("5.- Ver las valoraciones de un usuario")
    print("6.- Ver ranking de peliculas")
    print("7.- Ver usuario mas activo")
    print("0.- Salir")

    option = int(input("Opción: "))

    if option == 1:
        os.system("clear")
        insert_movies()
        input("Pulsa intro para continuar... ")
    elif option == 2:
        os.system("clear")
        select_movies_by_title()
        input("Pulsa intro para continuar... ")
    elif option == 3:
        os.system("clear")
        delete_movies_between_dates()
        input("Pulsa intro para continuar... ")
    elif option == 4:
        os.system("clear")
        update_movie_by_id()
        input("Pulsa intro para continuar... ")
    elif option == 5:
        os.system("clear")
        user_valorations()
        input("Pulsa intro para continuar... ")
    elif option == 6:
        os.system("clear")
        ranking_film()
        input("Pulsa intro para continuar... ")
    elif option == 7:
        os.system("clear")
        user_most_active()
        input("Pulsa intro para continuar... ")
    elif option == 0:
        print("Hasta pronto!")
    else:
        print("Error: opción desconocida")
        input("Pulsa intro para continuar... ")
