from conexion import connect

# En el caso de list_users() se utiliza una bandera o flag para menejar el problema de la falta de usuarios ya que no se utiliza el método "feltchall()" porque no es optimo en memorio cuando hay muchos usuarios.
def list_users():

    with connect() as conn:

        with conn.cursor() as cursor:

            try:

                cursor.execute("SELECT id, name FROM users")

                flag = False

                for user in cursor:

                    flag = True

                    print(f"\nID de usuario: {user[0]}\nNombre de usuario: {user[1]}")

                if not flag:

                    print("No hay usuarios registrados")

            except Exception as e:

                print(f"Ha ocurrido un error: {e}")


# En este caso se usa fetchone() ya que solo necesitamos un usuario y usar fetchall() sería redundante y poco práctico.
def list_specific_user(id):

    with connect() as conn:

        with conn.cursor() as cursor:

            try:

                cursor.execute("SELECT id, name FROM users WHERE id=%s", (id,))

                user = cursor.fetchone()

                print(user)

                if user:
                    
                    print(f"El usuario con el ID {id}, es {user[1]}")

                else:

                    print("No hay ningun usuario con ese número de ID")

            except Exception as e:

                print(f"Ha ocurrido un error: {e}")