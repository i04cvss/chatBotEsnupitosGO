# 🤖 Esnupitos GO Agent

---

# 📌 Descripción

Este proyecto consiste en el desarrollo de un agente inteligente basado en modelos de lenguaje (LLM), arquitectura RAG y el framework LangChain, aplicado al emprendimiento Esnupitos GO, dedicado a la importación de productos K-POP desde Asia hacia Chile.

El sistema permite automatizar consultas frecuentes de clientes mediante herramientas conectadas a una base de datos MySQL, mejorando la eficiencia operativa y reduciendo tiempos de respuesta.

---

# 🎯 Objetivo

Automatizar la atención de clientes mediante un agente capaz de:

- Consultar estados de pedidos.
- Entregar costos de envío y aduana.
- Responder preguntas frecuentes.
- Mantener contexto conversacional durante la interacción.

---

# 🧠 Tecnologías utilizadas

- Python  
- LangChain  
- MySQL  
- GPT-4o-mini  
- GitHub Models  
- Arquitectura RAG  

---

# ⚙️ Funcionamiento

El sistema funciona mediante las siguientes etapas:

1. El usuario selecciona una opción del menú.

2. El agente interpreta la consulta realizada.

3. Se selecciona automáticamente la herramienta adecuada.

4. El sistema consulta información en MySQL.

5. La memoria conversacional mantiene el contexto.

6. El modelo genera una respuesta basada en los datos recuperados.

---

# 📂 Estructura del proyecto

```text
chatBotGO/

├── main.py
├── tools.py
├── db.py
├── esnupitosgo.sql
├── requirements.txt
└── README.md
```

---

# 🚀 Cómo ejecutar el proyecto

## 1️⃣ Clonar repositorio

```bash
git clone <url-del-repo>

cd chatBotGO
```

---

## 2️⃣ Crear entorno virtual

```bash
python -m venv venv

venv\Scripts\activate
```

---

## 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configurar variable de entorno

```bash
setx GITHUB_TOKEN "TU_TOKEN"
```

---

## 5️⃣ Importar base de datos

Importar el archivo:

```text
esnupitosgo.sql
```

en MySQL Workbench.

---

# ▶️ Ejecutar proyecto

```bash
python main.py
```

---

# ⚠️ Consideraciones

- El sistema requiere conexión a internet.

- Utiliza GitHub Models para acceder al modelo GPT-4o-mini.

- La memoria implementada corresponde a memoria conversacional de corto plazo.

- Las respuestas dependen de la información almacenada en la base de datos.

---

# 👩‍💻 Autor

Camila Hernández  
Ingeniería en Informática
└── README.md
