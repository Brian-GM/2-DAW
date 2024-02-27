from mysql.connector import connect


def delete_movies_between_dates() -> None:
    with connect(host="db", user="dwes", password="dwes", database="dwesdb") as conn:
        with conn.cursor() as cursor:
            year1 = input("Fecha1")
            year2 = input("Fecha2")
            sql = """
                delete from movies
                where release_year >= %s and release_year <= %s
            """
            values: tuple[int, int] = (year1, year2)

            cursor.execute(sql, values)

            conn.commit()

            print(f"Se han eliminado {cursor.rowcount} peliculos")
