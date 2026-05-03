from db import get_connection

def estado(order_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT nombre_producto, estado FROM pedidos WHERE id = %s"
    cursor.execute(query, (order_id,))

    result = cursor.fetchone()
    conn.close()

    if result:
        nombre, estado = result
        return f"Tu pedido '{nombre}' está {estado}"
    else:
        return "Pedido no encontrado"
    

def costos(categoria):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT costo_envio_aprox, costo_aduana_aprox FROM costos_envio WHERE categoria = %s"
    cursor.execute(query, (categoria,))

    result = cursor.fetchone()
    conn.close()

    if result:
        envio, aduana = result
        return f"Para el producto'{categoria}': {envio}, {aduana}."
    else:
        return "Tipo de producto no cuenta con un aproximado"    

def faq(pregunta):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT respuesta FROM faq WHERE pregunta LIKE %s"
    cursor.execute(query, (f"%{pregunta}%",))

    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]
    else:
        return "Contactate cn un administrador para tener una respuesta para esta pregunta"