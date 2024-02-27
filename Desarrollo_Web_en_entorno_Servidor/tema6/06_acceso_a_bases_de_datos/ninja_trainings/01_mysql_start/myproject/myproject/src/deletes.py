from mysql.connector import connect

def delete_movies_between_dates() -> None:
    initial_date:int = input("Dime la fecha de inicio: ")
    end_date:int = input("Dime la fecha de final: ")

    with connect(host="db", user="dwes", password="dwes", database="dwesdb") as conn:
        with conn.cursor() as cursor:
            sql = """
                delete from movies where release_year between %s and %s
            """
            values = (initial_date,end_date)
            
            cursor.execute(sql, values)
            
            conn.commit()
            print(f"Se han eliminado {cursor.rowcount} peliculas")

