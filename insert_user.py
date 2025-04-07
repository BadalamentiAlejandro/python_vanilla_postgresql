from conexion import connect
from hash_password import hash_password


def insert_user(name, password):
    
    hashed_pw = hash_password(password)

    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO users (name, password) VALUES (%s, %s)", (name, hashed_pw))
        conn.commit()
