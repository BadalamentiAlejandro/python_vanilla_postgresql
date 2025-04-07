from conexion import connect


def create_table():

    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    password VARCHAR(255) NOT NULL
                )
            """)
        conn.commit()