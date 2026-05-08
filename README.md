# 🤖 Esnupitos GO Agent

---

## 📌 Descripción

Este proyecto consiste en el desarrollo de un agente inteligente basado en modelos de lenguaje (LLM), arquitectura RAG y el framework LangChain, aplicado al emprendimiento Esnupitos GO, dedicado a la importación de productos K-POP desde Asia hacia Chile.

El sistema permite automatizar consultas frecuentes de clientes mediante herramientas conectadas a una base de datos MySQL, mejorando la eficiencia operativa y reduciendo tiempos de respuesta.

---

## 🎯 Objetivo

Automatizar la atención de clientes mediante un agente capaz de:

- Consultar estados de pedidos.
- Entregar costos de envío y aduana.
- Responder preguntas frecuentes.
- Mantener contexto conversacional durante la interacción.

---

## 🧠 Tecnologías utilizadas

- Python
- LangChain
- MySQL
- GPT-4o-mini
- GitHub Models
- Arquitectura RAG

---

## ⚙️ Funcionamiento

El sistema funciona mediante:

1. Selección de una opción por parte del usuario.
2. Interpretación de la consulta por el agente.
3. Uso de tools especializadas según la consulta.
4. Recuperación de información desde MySQL.
5. Uso de memoria conversacional.
6. Generación de respuesta mediante el modelo LLM.

---

## 📂 Estructura del proyecto

```text
chatBotGO/
│
├── main.py
├── tools.py
├── db.py
├── esnupitosgo.sql
├── requirements.txt
└── README.md
