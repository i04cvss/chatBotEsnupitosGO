# 🤖 Esnupitos GO Chatbot

## 📌 Descripción

Este proyecto consiste en el desarrollo de un chatbot inteligente basado en modelos de lenguaje (LLM) y técnicas de recuperación aumentada (RAG), aplicado al emprendimiento **Esnupitos GO**, dedicado a la importación de productos K-POP desde Asia hacia Chile.

El sistema permite responder automáticamente consultas frecuentes de clientes, mejorando la eficiencia operativa y reduciendo los tiempos de respuesta.

---

## 🎯 Objetivo

Automatizar la atención de clientes mediante un asistente virtual capaz de:

* Responder preguntas frecuentes
* Informar estados de pedidos
* Entregar estimaciones de costos
* Indicar tiempos de entrega

---

## 🧠 Tecnologías utilizadas

* Python
* OpenAI API
* Modelo LLM (GPT-4o-mini)
* Enfoque RAG (Retrieval-Augmented Generation)

---

## ⚙️ Funcionamiento

El sistema funciona mediante:

1. Selección de una opción por parte del usuario
2. Generación de una consulta estructurada
3. Uso de un contexto interno (`datosGo.txt`)
4. Envío del prompt al modelo LLM
5. Generación de respuesta basada en contexto (RAG)

---

## 📂 Estructura del proyecto

* `main.py`: lógica principal del chatbot
* `datosGo.txt`: base de conocimiento del sistema
* `venv/`: entorno virtual (no incluido en repositorio)

---

## 🚀 Cómo ejecutar el proyecto

1. Clonar repositorio:

```
git clone <url-del-repo>
cd chatBotGO
```

2. Crear entorno virtual:

```
python -m venv venv
venv\Scripts\activate
```

3. Instalar dependencias:

```
pip install openai
```

4. Configurar API Key:

```
setx OPENAI_API_KEY "TU_API_KEY"
```

5. Ejecutar:

```
python main.py
```

---

## ⚠️ Consideraciones

* El sistema depende de la API de OpenAI
* Puede presentar limitaciones por cuota de uso
* Las respuestas se generan únicamente con información del contexto

---

## 📌 Autor

Camila Hernández – Ingeniería en Informática
