import streamlit as st
import pandas as pd
from supabase import create_client, Client

# --- Configuración de la página ---
st.set_page_config(page_title="Dashboard de Agente IA", layout="wide")

# --- Sidebar para Configuración ---
with st.sidebar:
    st.title("⚙️ Configuración")
    
    # Intentar obtener credenciales de st.secrets primero (para Streamlit Cloud)
    # Si no existen, pedir al usuario que las ingrese
    try:
        supabase_url = st.secrets.get("SUPABASE_URL", "")
        supabase_key = st.secrets.get("SUPABASE_KEY", "")
    except:
        supabase_url = ""
        supabase_key = ""
    
    # Si no hay credenciales en secrets, permitir ingresarlas manualmente
    if not supabase_url or not supabase_key:
        st.warning("⚠️ Por favor, ingresa tus credenciales de Supabase")
        
        supabase_url = st.text_input(
            "Supabase URL",
            value=supabase_url,
            type="default",
            help="URL de tu proyecto Supabase (ej: https://xxxxx.supabase.co)"
        )
        
        supabase_key = st.text_input(
            "Supabase Anon Key",
            value=supabase_key,
            type="password",
            help="Clave anon/public de tu proyecto Supabase"
        )
        
        if supabase_url and supabase_key:
            st.success("✅ Credenciales configuradas")
        else:
            st.info("💡 Encuentra estas credenciales en: Supabase Dashboard → Settings → API")
    else:
        st.success("✅ Credenciales cargadas desde Secrets")

# --- Función para cargar datos ---
@st.cache_data(ttl=10)  # Cache por 10 segundos
def load_all_data(_supabase_client):
    """Carga todos los chats de la base de datos."""
    try:
        response = _supabase_client.table('chat_history') \
            .select('*') \
            .order('timestamp', desc=True) \
            .execute()
        return pd.DataFrame(response.data)
    except Exception as e:
        st.error(f"❌ Error al cargar datos: {e}")
        return pd.DataFrame()

# --- Título Principal ---
st.title("🤖 Monitoring Dashboard del Agente IA")

# --- Verificar credenciales antes de continuar ---
if not supabase_url or not supabase_key:
    st.warning("⚠️ Por favor, configura tus credenciales de Supabase en la barra lateral")
    st.stop()

# --- Inicializar cliente de Supabase ---
try:
    supabase: Client = create_client(supabase_url, supabase_key)
    
    # --- Cuerpo de la App ---
    df = load_all_data(supabase)
    
    if df.empty:
        st.warning("📭 Aún no hay conversaciones en la base de datos.")
        st.info("💡 Envía mensajes al bot de Telegram para que aparezcan aquí.")
    else:
        # Métricas
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Mensajes", len(df))
        with col2:
            st.metric("Usuarios Únicos", df['user_id'].nunique())
        with col3:
            last_message_time = pd.to_datetime(df['timestamp']).max()
            st.metric("Último Mensaje", last_message_time.strftime("%H:%M:%S"))
        
        st.divider()
        
        st.header("📊 Visor de Conversaciones")
        
        # 1. Filtro por Usuario
        all_users = df['user_id'].unique()
        selected_user = st.selectbox(
            "Selecciona un User ID para ver su chat:",
            all_users,
            help="ID de Telegram del usuario"
        )
        
        if selected_user:
            st.subheader(f"💬 Historial de Chat para: {selected_user}")
            
            # Filtrar DF para ese usuario y ordenar por tiempo
            user_chat_df = df[df['user_id'] == selected_user].sort_values(by="timestamp")
            
            # Mostrar estadísticas del usuario
            col1, col2 = st.columns(2)
            with col1:
                user_messages = len(user_chat_df[user_chat_df['sender_role'] == 'user'])
                st.metric("Mensajes del Usuario", user_messages)
            with col2:
                ai_messages = len(user_chat_df[user_chat_df['sender_role'] == 'ai'])
                st.metric("Respuestas del Bot", ai_messages)
            
            st.divider()
            
            # Mostrar el chat en formato de chat
            for index, row in user_chat_df.iterrows():
                with st.chat_message(
                    name=row['sender_role'],
                    avatar="👤" if row['sender_role'] == 'user' else "🤖"
                ):
                    st.write(row['message'])
                    st.caption(f"_{row['timestamp']}_")
        
        # 2. Vista de Datos Crudos
        with st.expander("📄 Ver todos los datos crudos (Raw Data)"):
            st.dataframe(df, use_container_width=True)
            
            # Botón para descargar CSV
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="⬇️ Descargar como CSV",
                data=csv,
                file_name="chat_history.csv",
                mime="text/csv",
            )
    
    # Botón para refrescar
    if st.button("🔄 Refrescar Datos", type="primary"):
        st.cache_data.clear()
        st.rerun()

except Exception as e:
    st.error(f"❌ Error al conectar con Supabase: {e}")
    st.info("💡 Verifica que tus credenciales sean correctas y que la tabla 'chat_history' exista.")
