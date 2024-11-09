import os #Libreria que provee una manera versatil de utilizar funcionalidades dependientes del sistema operativo 
def set_working_directory():

    path = input("Introduce el directorio completo de trabajo:")

while True:

    print("\nGit y gitHub CLI - Opciones:")
    print("1. Establecer el directorio del trabajo")
    print("2. Crear un nuevo repositorio")
    print("3. Crear una nueva rama")
    print("4. Cambiar de rama")
    print("5. Mostrar ficheros pendientes de hacer commit")
    print("6. Hacer commit (+add)")
    print("7. Mostrar el historial de commits")
    print("8. Eliminar rama")
    print("9. Establecer repositorio remoto")
    print("10. Hacer pull")
    print("11. Hacer push")
    print("12. Salir")

    choice = input("selecciona una opcion (1 al 12): ")\

    match choice:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            pass
        case "8":
            pass
        case "9":
            pass
        case "10":
            pass
        case "11":
            pass
        case "12":
            print("Saliendo...")
            break
        case _:
            print("Opcion no valida")
