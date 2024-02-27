from mysql.connector import connect


def insert_movies() -> None:
    title:str = input("Dime el titulo: ")
    release_year:int = input("Dime el año de estreno: ")
    genre:str = input("Dime el genero: ")

    with connect(host="db", user="dwes", password="dwes", database="dwesdb") as conn:
        with conn.cursor() as cursor:
            sql = """
                insert into movies (title, release_year, genre)
                values (%s, %s, %s)
            """
            values = (title, release_year, genre)
            
            cursor.execute(sql, values)
            
            conn.commit()
            
            if cursor.rowcount == 1:
                print("Se ha insertado la pelicula")
            else:
                print("No se ha insertado la pelicula")