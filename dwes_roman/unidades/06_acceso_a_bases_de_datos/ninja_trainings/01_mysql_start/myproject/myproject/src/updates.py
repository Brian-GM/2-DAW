from mysql.connector import connect


def update_movie_by_id() -> None:
    with connect(host="db", user="dwes", password="dwes", database="dwesdb") as conn:
        with conn.cursor() as cursor:
            id_p = input("id")
            title = input("Titulo")
            release = input("Año")
            genre = input("Genero")
            sql = """
                update movies set title=%s,release_year=%s,genre=%s
                where id = %s
            """
            values = (title, release, genre, id_p)

            cursor.execute(sql, values)

            conn.commit()

            print(f"Se han actualizado {cursor.rowcount} peliculas")
