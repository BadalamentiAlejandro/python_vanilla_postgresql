from conexion import connect


def list_users():
    with connect() as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute("SELECT id, name FROM users")
                for item in cursor:
                    print(f"\nID de usuario: {item[0]}\nNombre de usuario: {item[1]}")
            except:
                print("No hay usuarios registrados.")


def list_specific_user(id):
    with connect() as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute("SELECT id, name FROM users WHERE id=%s", (id,))
                for item in cursor:
                    print(f"El usuario con el ID {id}, es {item[1]}")
            except:
                print("Usuario incorrecto.")