import os #Modulo que provee una manera versatil de utilizar funcionalidades dependientes del sistema operativo 
import subprocess

def run_command(command:str):
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            text=True,
            capture_output=True
        )
        print(result.stdout.split())
    except Exception as e:
        print(f"error: {e.stderr.split()}")

def set_working_directory():

    path = input("Introduce el directorio completo de trabajo:")
    if os.path.isdir(path):
        os.chdir(path)
        print(f"El directorio introducido ha cambiado a: {path}")
    else:
        print("El directorio introducido no existe")
    
def create_repository():
    if os.path.isdir(".git"):
            print("Ya existe un repositorio en este directorio")
    else:
        run_command("git init")
        run_command("git branch -M main")
        print("Repositorio inicializado")

def create_branch():
    branch_name = input("Nombre de la nueva rama")
    run_command(f"git branch {branch_name}")
    print(f"Rama {branch_name}")

def switch_branch():
    branch_name = input("Nombre de la rama a la que quieres cambiar")
    run_command(f"git checkout {branch_name}")
    print(f"Rama {branch_name}")

def show_pending_files():
    run_command("git status -s")

def make_commit():
    message = input("introduce un Mensaje para el commit:")
    run_command("git add .")
    run_command(f"git commit -m \"{message}\"")


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

    choice = input("selecciona una opcion (1 al 12): ")
    
    print("Directorio actual de trabajo")

    run_command("cd")

    match choice:
        case "1":
            set_working_directory()
        case "2":
            create_repository()
        case "3":
            create_branch()
        case "4":
            switch_branch()
        case "5":
            show_pending_files()
        case "6":
            make_commit()
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
