def log_transaction(func):
    def wrapper():
        print('1 Log de transacción...') 
        func()
        print('log terminado...')
    return wrapper



@log_transaction

def process_payment():
    print('Procesando el pago...')

process_payment()


#Pasos:
# Primero se Ejecuta la transacción en este caso 1 log de la transaccion
# Segundo se Ejecuta la funcion que esta dentro del decorador
# Y por ultimo se ejecuta el valor de la funcion iniciaal que es log de la transaccion