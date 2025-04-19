#Decorador que comprueba si un empeado tiene un rol en especifico

def check_access(required_role):
    def decorator(func):
        def wrapper(employe):
            #Si el rol del empleado coincide con el rol requerido
            if employe.get('role') == required_role:
                return func(employe)
            else:
                print(f'ACCESO DENEGADO. Solo {required_role} pueden realizar esta accion')

        return wrapper
    return decorator

def log_action(func):
    def wrapper(employee):
        print(f'Registrando accion para el empleado{employee['name']}')
        return func(employee)
    return wrapper
    

@check_access('admin')
@log_action
def delete_employee(employee):
    print(f'El empleado {employee['name']}, ha sido eliminado')

