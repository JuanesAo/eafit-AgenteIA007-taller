# 🚀 Instrucciones de Configuración Rápida

## Paso a Paso para Comenzar

### 1️⃣ Instalar Dependencias

Abre una terminal en el directorio del proyecto y ejecuta:

```bash
pip install -r requirements.txt
```

### 2️⃣ Configurar Variables de Entorno

Ya que el archivo `.env` está bloqueado por seguridad, necesitas crearlo manualmente:

1. Abre el proyecto en tu editor
2. Busca el archivo `.env` en la raíz del proyecto (puede estar oculto)
3. Si no existe, créalo con el siguiente contenido:

```env
TELEGRAM_TOKEN=8412590436:AAHXiaIekjiOKkJrEfofvbvwiOvocqqTZmU
GROQ_API_KEY=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
SUPABASE_URL=https://untyvuhdtcaabbzniurd.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVudHl2dWhkdGNhYWJiem5pdXJkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjExOTQ1MzAsImV4cCI6MjA3Njc3MDUzMH0.hZGH4hMrLNzDlpEOnwAgwwxLrTt3CdrSk3t6VSsrt6w
```

**⚠️ IMPORTANTE**: Este archivo contiene claves sensibles. NUNCA lo subas a GitHub.

### 3️⃣ Configurar la Base de Datos en Supabase

1. Ve a tu proyecto en Supabase: https://supabase.com/dashboard/project/untyvuhdtcaabbzniurd
2. Navega a **SQL Editor** (en el menú lateral)
3. Copia todo el contenido del archivo `setup_database.sql`
4. Pégalo en el editor SQL
5. Haz clic en **Run** (o presiona Ctrl+Enter)
6. Verifica que aparezca un mensaje de éxito
7. Ve a **Table Editor** → Deberías ver la tabla `chat_history`

### 4️⃣ Probar la Conexión

Antes de ejecutar el bot, verifica que todo esté configurado correctamente:

```bash
python test_connection.py
```

Este script verificará:
- ✅ Variables de entorno configuradas
- ✅ Conexión a Groq (LLM)
- ✅ Conexión a Supabase (Base de datos)
- ✅ Token de Telegram válido

### 5️⃣ Ejecutar el Bot de Telegram

Si todos los tests pasaron, ejecuta:

```bash
python bot.py
```

Deberías ver:
```
Iniciando el bot...
Bot iniciado. Presiona Ctrl+C para detener.
```

### 6️⃣ Probar el Bot

1. Abre Telegram en tu teléfono o computadora
2. Busca tu bot (usa el username que le diste cuando lo creaste con BotFather)
3. Envía `/start`
4. Envía cualquier mensaje, por ejemplo: "Hola, ¿cómo estás?"
5. El bot debería responder

### 7️⃣ Ejecutar el Dashboard (en otra terminal)

Abre una **nueva terminal** en el mismo directorio y ejecuta:

```bash
streamlit run dashboard.py
```

El dashboard se abrirá automáticamente en tu navegador (http://localhost:8501)

## 🎯 Resumen de Comandos

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Probar conexiones
python test_connection.py

# 3. Ejecutar el bot (Terminal 1)
python bot.py

# 4. Ejecutar el dashboard (Terminal 2)
streamlit run dashboard.py
```

## 🐛 Solución Rápida de Problemas

### "Module not found"
```bash
pip install -r requirements.txt
```

### "TELEGRAM_TOKEN not found"
Verifica que creaste el archivo `.env` con las claves correctas

### "Error al guardar en Supabase"
Ejecuta el script `setup_database.sql` en Supabase SQL Editor

### "Error invocando al agente"
Verifica que tu `GROQ_API_KEY` sea válida en https://console.groq.com

## 📱 Información de tus Servicios

### Bot de Telegram
- **Token**: 8412590436:AAHXiaIekjiOKkJrEfofvbvwiOvocqqTZmU
- Para cambiar la configuración del bot, habla con @BotFather en Telegram

### Supabase
- **Project URL**: https://untyvuhdtcaabbzniurd.supabase.co
- **Dashboard**: https://supabase.com/dashboard/project/untyvuhdtcaabbzniurd

### Groq API
- **Dashboard**: https://console.groq.com

## ✅ ¡Todo Listo!

Una vez que el bot y el dashboard estén corriendo:

1. **Interactúa con el bot** en Telegram
2. **Monitorea las conversaciones** en el dashboard (http://localhost:8501)
3. **Haz clic en "Refrescar Datos"** en el dashboard para ver las nuevas conversaciones

## 📚 Más Información

- Ver `README.md` para documentación completa
- Ver `DEPLOYMENT.md` para desplegar en la nube
- Ver los comentarios en el código para entender cómo funciona

