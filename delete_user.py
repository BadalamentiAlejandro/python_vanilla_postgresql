from conexion import connect


def delete_user(id):

    with connect() as conn:

        with conn.cursor() as cursor:

            try:

                cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
                
                user = cursor.fetchone()

                if user:

                    cursor.execute("DELETE FROM users WHERE id = %s", (id,))

                    print("Usuario borrado correctamente")

                else:
                    print("No se encuentra el usuario")

            except Exception as e:

                print(f"Ha surgido un problema al borrar el usuario: {e}")

        conn.commit()