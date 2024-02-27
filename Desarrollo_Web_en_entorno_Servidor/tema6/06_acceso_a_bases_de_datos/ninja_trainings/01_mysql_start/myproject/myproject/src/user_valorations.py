from mysql.connector import connect
import logging

logging.basicConfig(level=logging.DEBUG)


def user_valorations() -> None:
    name: str = input("Dime el nombre del usuario que quieres ver: ")
    try:
        with connect(
            host="db", user="dwes", password="dwes", database="dwesdb"
        ) as conn:
            with conn.cursor() as cursor:
                sql = """
                    select mv.title 
                    from reviewers as rw, ratings as rt, movies as mv 
                    where rw.id = rt.reviewer_id and rt.movie_id = mv.id and rw.first_name like %s
                """
                values = (name,)

                cursor.execute(sql, values)
                results: list[tuple] = cursor.fetchall()

                print(f"{name} ha valorado {len(results)} películas:")
                for row in results:
                    print(row[0])

    except Exception as e:
        logging.debug(f"Error {e}")
