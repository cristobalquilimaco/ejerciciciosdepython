from collections import deque

def manage_delivery_queue() -> deque:
    # Crea una cola para gestionar entregas de productos
    delivery_queue = deque(["order_1", "order_2", "order_3"])
    delivery_queue.append("order_4") #Agrega valor al final de la cola
    delivery_queue.appendleft("order_0") #Grega valor al principio de la cola
    delivery_queue.pop() #Elimina el valor que esta al final de la lista
    delivery_queue.popleft() #Elimina el valor al inicio de la cola
    return delivery_queue

queue = manage_delivery_queue()
print(queue)