# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


#     def greet(self):
#         print(f"Hola mi nombre es {self.name} y tengo {self.age} años")


# persona1 = Person("Ana", 30)
# persona2 = Person("Roberto", 23)

# persona1.greet()
# persona2.greet()


class BankAccount():
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    #Funcion para hacer los depositos 
    def deposit(self, amount):
        if self.is_active: #Valido SI la cuenta Esta activa (is.active)
            self.balance += amount #Si la cuenta esta activa al balance se le va a sumar el monto
            print(f"Se ha depositado {amount}. Saldo actual {self.balance}") #Imprimo en consola el monto que se deposito y el valor del balance una vez tome el deposito
        else: #Si la cuenta no esta activa no se puede depositar y se envia un mensaje
            print("no se puede depositar")
    
    #funcion para retirar dinero
    def withdraw(self, amount):
        if self.is_active: #Se valida si la cuenta esta activa
            if amount <= self.balance: #Si el monto es menor o igual al balance se puede retirar
                self.balance -= amount #Al balance se le resta el monto ingresado en el retiro
                print(f"Se aha retirado {amount}. saldo actual {self.balance}")

    #funcion para desactivar la cuenta 
    def desactivate_account(self):
        self.is_active = False 
        print(f"la cuenta ha sido desactivada")

    #Funcion para activar la cuenta
    def activate_account(self):
        self.is_active = True
        print(f"la cuenta ha sido activada")


#Creacion de cuentas 
account1 = BankAccount("Bulma", 500)
account2 = BankAccount("Vegeta", 200)

#llamada a los metodos 
account1.deposit(200)
account2.deposit(300)
account1.desactivate_account()
account1.deposit(50)