from mysql.connector import connect
import logging

logging.basicConfig(level=logging.DEBUG)


def update_movie_by_id() -> None:
    id_film: str = int(input("Dime el id de la pelicula quieres actualizar: "))
    title: str = input("Dime el titulo: ")
    release_year: int = int(input("Dime el año de estreno: "))
    genre: str = input("Dime el genero: ")

    try:
        with connect(host="db", user="dwes", password="dwes", database="dwesdb") as conn:
            with conn.cursor() as cursor:
                sql = """
                    update movies set title = %s, release_year = %s, genre = %s where id=%s 
                """
                values = (title, release_year, genre, id_film)

                cursor.execute(sql, values)
                conn.commit()

                print(f"Se han actualizado {cursor.rowcount} películas")
    except Exception as e:
        logging.debug(f"Error {e}")

