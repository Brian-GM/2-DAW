from mysql.connector import connect
import logging

logging.basicConfig(level=logging.DEBUG)


def ranking_film() -> None:
    try:
        with connect(
            host="db", user="dwes", password="dwes", database="dwesdb"
        ) as conn:
            with conn.cursor() as cursor:
                sql = """
                    select mv.title,avg(rt.rating) as si
                    from ratings as rt, movies as mv 
                    where rt.movie_id = mv.id
                    GROUP BY mv.title
                    order by si desc
                """

                cursor.execute(
                    sql,
                )
                results: list[tuple] = cursor.fetchall()
                for row in results:
                    print(f"La pelicula: {row[0]}")
                    print(f"Tuvo una valoracion media de: {row[1]}")

    except Exception as e:
        logging.debug(f"Error {e}")
