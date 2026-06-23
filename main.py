from langchain_openai import ChatOpenAI
from langchain_classic.agents import initialize_agent, Tool, AgentType
from langchain_classic.memory import ConversationBufferMemory

from tools import estado, costos, faq

import os
import time
import csv
from datetime import datetime


# FUNCIÓN PARA GUARDAR LOGS


def guardar_log(pregunta, respuesta, latencia, estado_log="OK"):

    archivo_existe = os.path.isfile("logs.csv")

    with open("logs.csv", "a", newline="", encoding="utf-8") as archivo:

        writer = csv.writer(archivo)

        if not archivo_existe:
            writer.writerow([
                "fecha",
                "pregunta",
                "respuesta",
                "latencia",
                "estado"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            pregunta,
            respuesta[:200],
            round(latencia, 2),
            estado_log
        ])


# LLM


llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    temperature=0,
    base_url="https://models.github.ai/inference",
    openai_api_key=os.environ.get("GITHUB_TOKEN")
)


# MEMORIA


memory = ConversationBufferMemory(
    memory_key="chat_history"
)



# TOOLS
tools = [

    Tool(
        name="EstadoPedido",
        func=estado,
        description="Obtiene el estado de un pedido usando su ID"
    ),

    Tool(
        name="CostoEnvio",
        func=costos,
        description="Obtiene costos de envío y aduana según categoría"
    ),

    Tool(
        name="FAQ",
        func=faq,
        description="Responde preguntas frecuentes"
    )
]


# AGENTE


agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    memory=memory,
    verbose=True,
    agent_kwargs={
        "prefix": """
Eres un asistente virtual del emprendimiento Esnupitos GO.

Tu función es responder consultas de clientes utilizando únicamente la información obtenida desde las herramientas del sistema.

Instrucciones:
- No inventes información.
- Responde de forma clara, breve y amigable.
- Utiliza las herramientas disponibles para obtener información.
- Si no existe información suficiente, responde:
"No dispongo de esa información en este momento."
"""
    }
)



# MENU


def mostrar_menu():

    print("\n=== Esnupitos GO ===")
    print("1. Estado de pedido")
    print("2. Costos de envío")
    print("3. Preguntas frecuentes")
    print("4. Salir")



# MAIN


def main():

    while True:

        mostrar_menu()

        opcion = input("Selecciona una opción: ")

        if opcion == "4":
            print("Hasta luego.")
            break

        if opcion == "1":

            pedido = input(
                "Ingresa nombre del pedido: "
            )

            pregunta = (
                f"¿Cuál es el estado del pedido {pedido}?"
            )

        elif opcion == "2":

            categoria = input(
                "Categoría: "
            )

            pregunta = (
                f"¿Cuál es el costo de envío para {categoria}?"
            )

        elif opcion == "3":

            pregunta = input(
                "Escribe tu pregunta: "
            )

        else:

            print("Opción inválida")
            continue

        try:

            inicio = time.time()

            respuesta = agent.run(
                pregunta
            )

            fin = time.time()

            latencia = fin - inicio

            guardar_log(
                pregunta,
                respuesta,
                latencia,
                "OK"
            )

            print("\nRespuesta:")
            print(respuesta)

            print(
                f"\nTiempo de respuesta: {latencia:.2f} segundos"
            )

        except Exception as e:

            guardar_log(
                pregunta,
                str(e),
                0,
                "ERROR"
            )

            print(
                "\nOcurrió un error:"
            )

            print(e)


if __name__ == "__main__":
    main()