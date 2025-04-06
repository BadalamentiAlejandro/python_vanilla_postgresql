from conexion import connect

def create_table():
# Table creation.
    conn = connect() # Creates connection.
    cursor = conn.cursor() # Permits querys.

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMATY KEY,
            name VARCHAR(100) NOT NULL,
            password VARCHAR(255) NOT NULL
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()