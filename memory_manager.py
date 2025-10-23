import os
from supabase import create_client, Client
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Obtener credenciales de variables de entorno
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Inicializar cliente de Supabase solo si las credenciales existen
supabase: Client = None
if SUPABASE_URL and SUPABASE_KEY:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_chat_history(user_id):
    """
    Obtiene el historial de chat para un user_id y lo formatea para LangChain.
    """
    if not supabase:
        print("Error: Supabase no está configurado. Verifica las variables de entorno.")
        return []
    
    try:
        response = supabase.table('chat_history') \
            .select('*') \
            .eq('user_id', str(user_id)) \
            .order('timestamp', desc=False) \
            .execute()
        
        messages = []
        if response.data:
            for record in response.data:
                if record['sender_role'] == 'user':
                    messages.append(HumanMessage(content=record['message']))
                elif record['sender_role'] == 'ai':
                    messages.append(AIMessage(content=record['message']))
        
        return messages
    except Exception as e:
        print(f"Error al obtener historial: {e}")
        return []

def add_message_to_history(user_id, sender_role, message):
    """
    Añade un nuevo mensaje (de 'user' o 'ai') a la base de datos.
    """
    if not supabase:
        print("Error: Supabase no está configurado. Verifica las variables de entorno.")
        return
    
    try:
        supabase.table('chat_history').insert({
            'user_id': str(user_id),
            'sender_role': sender_role,
            'message': message
        }).execute()
    except Exception as e:
        print(f"Error al guardar en Supabase: {e}")
