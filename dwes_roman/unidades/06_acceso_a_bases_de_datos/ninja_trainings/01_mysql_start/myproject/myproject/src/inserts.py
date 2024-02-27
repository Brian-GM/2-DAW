from mysql.connector import connect


def insert_movies() -> None:
    with connect(host="db", user="dwes", password="dwes", database="dwesdb") as conn:
        with conn.cursor() as cursor:
            title: str = input("Título de la película: ")
            release_year: int = int(input("Año de estreno: "))
            genre: str = input("Género: ")
            sql = """
                insert into movies (title, release_year, genre)
                values (%s, %s, %s)
            """
            values = (title, release_year, genre)

            cursor.execute(sql, values)

            conn.commit()

            if cursor.rowcount == 1:
                print("Se ha insertado el estudiante")
            else:
                print("No se ha insertado el estudiante")
