def log_transaction(func):
    def wrapper():
        print('Log de transacción...')
        func()
        print('log terminado...')
    return wrapper()

def process_payment():
    print('Procesando el pago...')

