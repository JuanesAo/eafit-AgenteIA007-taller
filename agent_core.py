import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Cargar variables de entorno
load_dotenv()

# Verificar que la API key existe
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    print("⚠️ WARNING: GROQ_API_KEY no está configurada en el archivo .env")
    print("El bot podrá guardar mensajes pero NO podrá responder con IA")

# 1. Inicializar el LLM
# Usamos Llama 3 vía Groq. Es rápido y potente.
llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0.3
)

# Función para invocar al agente
def invoke_agent(user_input, chat_history_messages):
    """
    Invoca al LLM con la entrada del usuario y el historial.
    Esta es una versión simplificada que no usa agentes complejos
    pero funciona de manera confiable en cualquier entorno.
    """
    # Construir el contexto de la conversación
    messages = [
        SystemMessage(content="Eres un asistente de IA útil. Responde al usuario de forma concisa y amigable.")
    ]
    
    # Agregar el historial de chat
    messages.extend(chat_history_messages)
    
    # Agregar la pregunta actual del usuario
    messages.append(HumanMessage(content=user_input))
    
    # Invocar al LLM
    response = llm.invoke(messages)
    
    # Retornar en el formato esperado
    return {"output": response.content}
