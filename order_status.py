from enum import Enum

class OrderStatus(Enum):
    PEDING = 1 #Pendiente
    SHIPPED = 2 #Enviado
    DELIVERED = 3 #Entregado