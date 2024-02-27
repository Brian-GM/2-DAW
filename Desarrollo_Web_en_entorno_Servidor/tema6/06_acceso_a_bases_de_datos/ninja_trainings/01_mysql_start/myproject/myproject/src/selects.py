from mysql.connector import connect
import logging

def select_movies_by_title() -> None:
    logging.basicConfig(level=logging.DEBUG)

    title: str = input("Que pelicula quieres bucar: ")
    with connect(host="db", user="dwes", password="dwes", database="dwesdb") as conn:
        with conn.cursor() as cursor:
            sql = """
                select title from movies where title like %s
            """
            values = (f"%{title}%",)
            
            cursor.execute(sql, values)

            results = cursor.fetchall()
            logging.debug(results)
            for row in results:
                print(f"Pelicula: {row[0]}")


                        
