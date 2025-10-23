#  Sistema de Agente Multi-Interfaz

Sistema de agente de IA con interfaz de Telegram y dashboard de administración en Streamlit, desarrollado para el taller de IA de EAFIT.

##  Descripción

Este sistema cuenta con:
- **Bot de Telegram**: Interfaz conversacional que recuerda el historial de chat
- **Dashboard Streamlit**: Panel de administración para monitorear conversaciones en tiempo real
- **Agente LLM**: Cerebro basado en LangChain + Groq (Llama 3)
- **Memoria Persistente**: Base de datos Supabase para almacenar conversaciones

##  Arquitectura

```
Usuario → [Telegram Bot]
             ↓
    Agente (LangChain + Groq)
             ↓↑
    Memoria (Supabase PostgreSQL)
             ↑
      [Dashboard Streamlit] ← Admin
```

##  Stack Tecnológico

- **Lenguaje**: Python 3.10+
- **LLM**: Groq API (Llama 3)
- **Framework de Agentes**: LangChain
- **Base de Datos**: Supabase (PostgreSQL)
- **Interfaz Usuario**: python-telegram-bot
- **Dashboard Admin**: Streamlit
- **Herramientas Opcionales**: Tavily API (búsqueda web)

##  Estructura del Proyecto

```
eafit-AgenteIA007-taller/
├── .env                    # Variables de entorno (NO incluir en git)
├── .gitignore             # Archivos a ignorar en git
├── requirements.txt       # Dependencias de Python
├── agent_core.py          # Lógica del agente (LangChain + Groq)
├── memory_manager.py      # Funciones para Supabase
├── bot.py                 # Script del bot de Telegram
├── dashboard.py           # Script del dashboard de Streamlit
├── setup_database.sql     # Script SQL para crear tabla en Supabase
└── README.md              # Este archivo
```

##  Configuración Inicial

### 1. Clonar el Repositorio

```bash
git clone <tu-repositorio>
cd eafit-AgenteIA007-taller
```

### 2. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto:

```env
TELEGRAM_TOKEN=tu_token_de_telegram
GROQ_API_KEY=tu_key_de_groq
SUPABASE_URL=tu_supabase_url
SUPABASE_KEY=tu_supabase_key
```

### 4. Configurar la Base de Datos en Supabase

1. Ve a tu proyecto en [Supabase](https://supabase.com/dashboard)
2. Navega a **SQL Editor**
3. Ejecuta el script `setup_database.sql` para crear la tabla `chat_history`
4. Verifica que la tabla se creó correctamente en la sección **Table Editor**

##  Uso del Sistema

### Ejecutar el Bot de Telegram

```bash
python bot.py
```

### Ejecutar el Dashboard de Administración

```bash
streamlit run dashboard.py
```

##  Obtener las API Keys

### Groq API
1. Visita [console.groq.com](https://console.groq.com)
2. Crea una cuenta o inicia sesión
3. Ve a **API Keys** y genera una nueva key

### Telegram Bot Token
1. Abre Telegram y busca [@BotFather](https://t.me/botfather)
2. Envía el comando `/newbot`
3. Sigue las instrucciones para crear tu bot
4. Copia el token que te proporciona

### Supabase
1. Visita [supabase.com](https://supabase.com)
2. Crea un nuevo proyecto
3. Ve a **Settings** → **API**
4. Copia la **URL** y la **anon/public key**

##  Funcionalidades

### Bot de Telegram
-  Conversación natural con IA (en proceso)

### Dashboard de Administración
-  Vista de todas las conversaciones
-  Filtrado por usuario
-  Visualización cronológica de mensajes
-  Datos crudos exportables
-  Actualización en tiempo real

## 🔧 Personalización

### Cambiar el Modelo de LLM

En `agent_core.py`, modifica la línea:

```python
llm = ChatGroq(
    model="llama3-8b-8192",  # Cambia aquí el modelo
    temperature=0.3
)
```

Modelos disponibles en Groq:
- `llama3-8b-8192`
- `llama3-70b-8192`
- `mixtral-8x7b-32768`

##  Solución de Problemas

### Error de conexión a Supabase
- Verifica que `SUPABASE_URL` y `SUPABASE_KEY` sean correctos
- Asegúrate de que la tabla `chat_history` exista

### El bot no responde
- Verifica que el `TELEGRAM_TOKEN` sea correcto
- Asegúrate de que el bot esté corriendo (`python bot.py`)

### Error con Groq API
- Verifica que `GROQ_API_KEY` sea válida
- Revisa los límites de tu plan en Groq

##  Notas de Seguridad

- ** NUNCA subas el archivo `.env` a git**
- El archivo `.gitignore` ya está configurado para proteger tus claves
- Usa variables de entorno en los servicios de hosting

##  Desarrollo

Creado para el Taller de Agentes IA - Universidad EAFIT 2025-02

##  Licencia

Este proyecto es de uso educativo para el curso de IA de EAFIT.

