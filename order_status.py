from enum import Enum

class OrderStatus(Enum):
    PEDING = 1 #Pendiente
    SHIPPED = 2 #Enviado
    DELIVERED = 3 #Entregado

def check_order_status(status: OrderStatus):
    #Comprueba el estado del pedido y develve un mensaje
    if status == OrderStatus.PEDING:
        return "Order is still pending."
    elif status == OrderStatus.SHIPPED:
        return "Order has benn shipped."
    elif status == OrderStatus.DELIVERED:
        return "Order has been Delivered"
    

print(check_order_status(OrderStatus.PEDING))