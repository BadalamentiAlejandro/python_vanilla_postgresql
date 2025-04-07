from conexion import connect
from hash_password import hash_password


def update_password(id):

    with connect() as conn:

        with conn.cursor() as cursor:

            try:

                cursor.execute("SELECT * FROM users WHERE id = %s", (id,))

                user = cursor.fetchone()

                if user:

                    new_hash_password = hash_password(input("Introduce una nueva contraseña: "))

                    cursor.execute("UPDATE users SET password = %s WHERE id = %s", (new_hash_password, user[0]))

                    print("Contraseña modificada correctamente.")

                else:

                    print("No se encuentra el usuario")

            except Exception as e:

                print(f"Ha surgido un problema al modificar la contraseña: {e}")

        conn.commit()