from conexion import connect
from hash_password import hash_password


def insert_user(name, password):
    conn = connect()
    cursor = conn.cursor()

    hashed_pw = hash_password(password)

    cursor.execute("INSERT INTO userts (name, password) VALUES (%s, %s)" (name, hashed_pw))

    conn.commit()
    cursor.close()
    conn.close()
