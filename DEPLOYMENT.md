# 🚀 Guía de Despliegue

Esta guía te ayudará a desplegar el Sistema de Agente Multi-Interfaz en servicios cloud gratuitos.

## 📋 Prerequisitos

- Cuenta de GitHub
- Cuenta de Render (para el bot)
- Cuenta de Streamlit Cloud (para el dashboard)
- Supabase configurado con la tabla `chat_history`

## 🗄️ Paso 1: Configurar Supabase

### 1.1 Crear Proyecto en Supabase

1. Ve a [supabase.com](https://supabase.com) y crea una cuenta
2. Crea un nuevo proyecto
3. Anota la **URL del proyecto** y la **anon/public key** (Settings → API)

### 1.2 Crear la Tabla

1. En tu proyecto de Supabase, ve a **SQL Editor**
2. Copia y pega el contenido del archivo `setup_database.sql`
3. Ejecuta el script
4. Verifica en **Table Editor** que la tabla `chat_history` se creó correctamente

## 🤖 Paso 2: Desplegar el Bot de Telegram en Render

### 2.1 Preparar el Repositorio

1. Sube tu código a GitHub (si aún no lo has hecho)
2. Asegúrate de que `.env` esté en `.gitignore` (ya está incluido)

### 2.2 Crear el Servicio en Render

1. Ve a [render.com](https://render.com) y crea una cuenta
2. Haz clic en **New +** → **Background Worker**
3. Conecta tu repositorio de GitHub
4. Configura el servicio:
   - **Name**: `eafit-telegram-bot` (o el nombre que prefieras)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python bot.py`

### 2.3 Configurar Variables de Entorno

En la sección **Environment**, agrega:

```
TELEGRAM_TOKEN=tu_token_de_telegram
GROQ_API_KEY=tu_groq_api_key
SUPABASE_URL=https://tu-proyecto.supabase.co
SUPABASE_KEY=tu_supabase_anon_key
```

### 2.4 Desplegar

1. Haz clic en **Create Background Worker**
2. Espera a que el despliegue termine (puede tardar 2-3 minutos)
3. Verifica en los logs que el bot se inició correctamente

## 📊 Paso 3: Desplegar el Dashboard en Streamlit Cloud

### 3.1 Crear la App en Streamlit Cloud

1. Ve a [streamlit.io/cloud](https://streamlit.io/cloud) y crea una cuenta
2. Haz clic en **New app**
3. Selecciona tu repositorio de GitHub
4. Configura:
   - **Branch**: main (o tu rama principal)
   - **Main file path**: `dashboard.py`
   - **App URL**: elige un nombre único

### 3.2 Configurar Variables de Entorno

1. Haz clic en **Advanced settings**
2. En la sección **Secrets**, agrega:

```toml
SUPABASE_URL = "https://tu-proyecto.supabase.co"
SUPABASE_KEY = "tu_supabase_anon_key"
```

**Nota**: Streamlit usa formato TOML para secretos, no .env

### 3.3 Desplegar

1. Haz clic en **Deploy**
2. Espera a que el despliegue termine (puede tardar 2-3 minutos)
3. Tu dashboard estará disponible en la URL que elegiste

## ✅ Paso 4: Verificar el Despliegue

### 4.1 Probar el Bot

1. Abre Telegram
2. Busca tu bot por el username que le diste
3. Envía `/start`
4. Envía un mensaje de prueba
5. Verifica que el bot responde correctamente

### 4.2 Probar el Dashboard

1. Abre la URL de tu dashboard en Streamlit
2. Verifica que puedes ver las conversaciones
3. Selecciona el user_id de tu prueba
4. Verifica que aparece el historial de chat

## 🔧 Solución de Problemas

### El bot no responde en Telegram

**Problema**: El bot está offline o no responde

**Soluciones**:
1. Verifica en Render que el servicio está "Running"
2. Revisa los logs en Render para ver errores
3. Verifica que el `TELEGRAM_TOKEN` sea correcto
4. Asegúrate de que todas las dependencias se instalaron

### Error de conexión a Supabase

**Problema**: "Error al guardar en Supabase" o "Error al cargar datos"

**Soluciones**:
1. Verifica que `SUPABASE_URL` y `SUPABASE_KEY` sean correctos
2. Asegúrate de que la tabla `chat_history` existe
3. Verifica que las políticas RLS están configuradas correctamente
4. Revisa los logs de Supabase en su dashboard

### El dashboard no muestra datos

**Problema**: "Aún no hay conversaciones en la base de datos"

**Soluciones**:
1. Primero envía mensajes al bot para generar datos
2. Verifica la conexión a Supabase
3. Haz clic en "Refrescar Datos"
4. Revisa que las variables de entorno estén correctas

### Error con Groq API

**Problema**: "Error invocando al agente"

**Soluciones**:
1. Verifica que `GROQ_API_KEY` sea válida
2. Revisa los límites de tu plan en Groq
3. Puede que necesites esperar si excediste el rate limit
4. Intenta con un modelo diferente (e.g., `llama3-70b-8192`)

## 📝 Notas Importantes

### Capa Gratuita de Render

- **Limitaciones**: 
  - El servicio puede "dormirse" después de 15 minutos de inactividad
  - La primera respuesta después de despertar puede tardar ~30 segundos
  - 750 horas gratis por mes (suficiente para un servicio)

- **Solución**: Considera usar un servicio de "ping" como [cron-job.org](https://cron-job.org) para mantener el bot activo

### Capa Gratuita de Streamlit

- **Limitaciones**:
  - 1 app privada gratis
  - Apps públicas ilimitadas
  - 1 GB de recursos

- **Nota**: El dashboard será público por defecto. Si quieres hacerlo privado, configura autenticación o usa la opción de app privada

### Capa Gratuita de Supabase

- **Limitaciones**:
  - 500 MB de base de datos
  - 2 GB de transferencia por mes
  - Proyectos pausados después de 1 semana de inactividad

- **Solución**: Visita tu proyecto al menos una vez por semana para mantenerlo activo

## 🔄 Actualizaciones

Para actualizar tu código después del despliegue:

### Actualizar el Bot (Render)

1. Haz push de tus cambios a GitHub
2. Render detectará automáticamente los cambios
3. El servicio se redespliegará automáticamente

### Actualizar el Dashboard (Streamlit)

1. Haz push de tus cambios a GitHub
2. Streamlit detectará automáticamente los cambios
3. La app se redespliegará automáticamente

## 📊 Monitoreo

### Ver Logs del Bot

1. Ve a tu servicio en Render
2. Haz clic en la pestaña **Logs**
3. Aquí verás todos los mensajes y errores del bot

### Ver Logs del Dashboard

1. Ve a tu app en Streamlit Cloud
2. Haz clic en **Manage app** → **Logs**
3. Aquí verás todos los mensajes y errores del dashboard

## 🎉 ¡Listo!

Tu sistema está ahora desplegado y funcionando 24/7 de forma gratuita. Los usuarios pueden interactuar con el bot en Telegram y tú puedes monitorear todas las conversaciones desde el dashboard.

### Próximos Pasos Opcionales

1. **Agregar búsqueda web**: Configura Tavily API
2. **Mejorar el prompt**: Personaliza la personalidad del agente
3. **Agregar más herramientas**: Calculadora, clima, etc.
4. **Implementar autenticación**: Proteger el dashboard
5. **Agregar analytics**: Métricas de uso y rendimiento

