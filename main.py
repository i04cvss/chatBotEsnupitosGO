import os
from openai import OpenAI

print("ARCHIVO EJECUTÁNDOSE")
# api
client = OpenAI(api_key="TU_API_KEY_AQUI")


# datos
def cargar_datos():
    try:
        with open("datosGo.txt", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "No hay información disponible."

# rag
def generar_respuesta(datos, pregunta, opcion):

    prompt = f"""
Eres un asistente virtual del emprendimiento Esnupitos GO.

Tu función es responder consultas de clientes basándote únicamente en la información entregada en el contexto.

El usuario seleccionará una opción del sistema, y debes limitar tu respuesta SOLO a esa categoría.

Opciones disponibles:
- Estado de pedido
- Costos de envío
- Tiempos de entrega
- Preguntas frecuentes

Instrucciones:
- Responde únicamente en función de la opción seleccionada.
- No mezcles información de otras categorías.
- No inventes información.
- Usa solo el contexto proporcionado.
- Mantén un lenguaje claro, breve y amigable.
- Si no existe información suficiente en el contexto, responde: "No dispongo de esa información en este momento."

Datos de entrada:
Opción seleccionada: {opcion}
Pregunta del cliente: {pregunta}

Contexto:
{datos}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    except:
        return "No se pudo generar respuesta en este momento."

# menu
def mostrar_menu():
    
    print("\n=== Esnupitos GO Chatbot ===")
    print("1. Estado de pedido")
    print("2. Costos de envío")
    print("3. Tiempos de entrega")
    print("4. Pregunta libre")

# respuesta
def main():
    print("ENTRÓ AL MAIN")
    datos = cargar_datos()
    mostrar_menu()

    opcion = input("Elige una opción: ")

    if opcion == "1":
        pedido = input("Ingresa tu número de pedido: ")
        pregunta = f"¿Cuál es el estado del pedido {pedido}?"

    elif opcion == "2":
        peso = input("¿Cuánto pesa el producto? ")
        pregunta = f"¿Cuál es el costo de envío para un producto de {peso} gramos?"

    elif opcion == "3":
        pregunta = "¿Cuáles son los tiempos de entrega?"

    else:
        pregunta = input("Escribe tu pregunta: ")

    respuesta = generar_respuesta(datos, pregunta, opcion)
    print("\nRespuesta:")
    print(respuesta)

# ejecutar
if __name__ == "__main__":
    main()