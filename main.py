from langchain_openai import ChatOpenAI
from langchain_classic.agents import initialize_agent, Tool, AgentType
from langchain_classic.memory import ConversationBufferMemory

from tools import estado, costos, faq

import os


# LLM
llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    temperature=0,
    base_url="https://models.github.ai/inference",
    openai_api_key=os.environ.get("GITHUB_TOKEN")
)

memory = ConversationBufferMemory(memory_key="chat_history")

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

def mostrar_menu():
    print("\n=== Esnupitos GO ===")
    print("1. Estado de pedido")
    print("2. Costos de envío")
    print("3. Preguntas frecuentes")
    print("4. Salir")

def main():

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "4":
            break

        if opcion == "1":
            pedido = input("Ingresa nombre del pedido: ")
            pregunta = f"¿Cuál es el estado del pedido {pedido}?"

        elif opcion == "2":
            categoria = input("Categoría: ")
            pregunta = f"¿Cuál es el costo de envío para {categoria}?"

        respuesta = agent.run(pregunta)

        print("\nRespuesta:")
        print(respuesta)

if __name__ == "__main__":
    main()