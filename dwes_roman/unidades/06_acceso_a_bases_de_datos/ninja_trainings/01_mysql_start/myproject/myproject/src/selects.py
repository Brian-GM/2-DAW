from mysql.connector import connect


def select_movies_by_title() -> None:
    with connect(host="db", user="dwes", password="dwes", database="dwesdb") as conn:
        with conn.cursor() as cursor:
            title = input("Escribe el titulo")
            sql = "select title from movies where title like %s"
            value = (f"{title}%",)

            cursor.execute(sql, value)
            results = cursor.fetchall()
            for row in results:
                print(f"Peliculas {row[0]}:")
                print()
