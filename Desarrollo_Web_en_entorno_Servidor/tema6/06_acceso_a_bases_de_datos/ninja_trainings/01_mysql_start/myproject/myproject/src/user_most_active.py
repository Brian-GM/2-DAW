from mysql.connector import connect
import logging

logging.basicConfig(level=logging.DEBUG)


def user_most_active() -> None:
    try:
        with connect(
            host="db", user="dwes", password="dwes", database="dwesdb"
        ) as conn:
            with conn.cursor() as cursor:
                sql = """
                    select u.first_name,u.last_name, count(r.reviewer_id) as total 
                    from ratings as r, reviewers as u 
                    where u.id = r.reviewer_id
                    GROUP BY u.id
                    order by total desc
                    limit 1
                """

                cursor.execute(
                    sql,
                )
                results = cursor.fetchall()
                for row in results:
                    print(f"Nombre: {row[0]}")
                    print(f"Apellidos: {row[1]}")
                    print(f"Valoraciones: {row[2]}")

    except Exception as e:
        logging.debug(f"Error {e}")
