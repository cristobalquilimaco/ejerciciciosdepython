#Decorador que comprueba si un empeado tiene un rol en especifico

def check_access(reuired):



@check_access('admin')
@log_action
def delete_employee(employee):
    print(f'El empleado {employee['name']}, ha sido eliminado')

