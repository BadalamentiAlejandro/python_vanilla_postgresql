from create_table import create_table
from insert_user import insert_user
from list_users import list_users, list_specific_user
from update_user import update_password

from dotenv import load_dotenv


load_dotenv()

def menu():
    create_table()

    while True:

        print("\n--- Menu de Usuarios ---")
        print("1. Agregar usuario")
        print("2. Ver usuarios")
        print("3. Ver un usuario específico")
        print("4. Cambiar contraseña")
        print("6. Salir")

        choice = int(input("Elige una opción"))

        if choice == 1:

            name = input("Nombre: ")

            password = input("Contraseña: ")

            insert_user(name, password)

            print(f"Usuario {name} agregado")

        elif choice == 2:

            list_users()

        elif choice == 3:

            id = int(input("Por favor indica un ID"))

            list_specific_user(id)

        elif choice == 4:

            id = int(input("Por favor indica un ID"))

            update_password(id)

        elif choice == 6:

            print("Hasta luego!")

            break

        else:
            
            print("Opción inválida, por favor elige una opción válida.")


if __name__ == "__main__":
    menu()
