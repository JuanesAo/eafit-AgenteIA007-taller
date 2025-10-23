# 🔒 Guía de Seguridad

## ⚠️ IMPORTANTE: Protección de Claves API

Este proyecto utiliza varias claves API sensibles que **NUNCA** deben compartirse públicamente o subirse a GitHub.

## 📋 Archivo `.env` - NO SUBIR A GIT

### ✅ Configuración Correcta

El archivo `.gitignore` ya está configurado para excluir el archivo `.env`:

```gitignore
# Environment variables
.env
```

### 🔧 Cómo Configurar tus Claves

1. **Crea tu archivo `.env` local:**
   ```bash
   # Copia el archivo de ejemplo
   cp env.example .env
   ```

2. **Edita `.env` con tus claves reales:**
   ```env
   TELEGRAM_TOKEN=tu_token_real_de_telegram
   GROQ_API_KEY=tu_groq_api_key_real
   SUPABASE_URL=tu_supabase_url_real
   SUPABASE_KEY=tu_supabase_key_real
   ```
   
   **Para el propietario del proyecto**: Las claves reales están en el archivo `KEYS.md` (que NO está en git).

3. **Verifica que `.env` NO se suba a git:**
   ```bash
   git status
   # El archivo .env NO debe aparecer en la lista
   ```

## 🚨 ¿Qué hacer si subiste las claves por error?

Si accidentalmente subiste el archivo `.env` con claves reales a GitHub:

### Paso 1: Regenerar TODAS las claves

#### Telegram Bot Token
1. Abre Telegram y busca [@BotFather](https://t.me/botfather)
2. Envía `/revoke`
3. Selecciona tu bot
4. Envía `/token` para generar uno nuevo

#### Groq API Key
1. Ve a [console.groq.com/keys](https://console.groq.com/keys)
2. Elimina la clave comprometida
3. Crea una nueva clave

#### Supabase Keys
1. Ve a tu proyecto en [supabase.com](https://supabase.com/dashboard)
2. Settings → API
3. Regenera las claves

### Paso 2: Limpiar el Historial de Git

```bash
# Eliminar el archivo del historial
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch .env" \
  --prune-empty --tag-name-filter cat -- --all

# Forzar el push (CUIDADO: esto reescribe la historia)
git push origin --force --all
```

**NOTA**: Es más seguro simplemente regenerar las claves que intentar limpiar el historial.

## 📁 Archivos que SÍ se deben subir al repositorio

- ✅ `env.example` - Plantilla sin claves reales
- ✅ `.gitignore` - Configuración de archivos a ignorar
- ✅ `README.md` - Documentación
- ✅ `*.py` - Código fuente
- ✅ `requirements.txt` - Dependencias
- ✅ `*.sql` - Scripts de base de datos
- ✅ `*.md` - Documentación

## 📁 Archivos que NO se deben subir

- ❌ `.env` - Contiene claves secretas
- ❌ `__pycache__/` - Archivos compilados de Python
- ❌ `venv/` o `env/` - Entornos virtuales
- ❌ `.vscode/` o `.idea/` - Configuración del IDE

## 🔐 Mejores Prácticas

### Durante el Desarrollo

1. **Siempre verifica antes de hacer commit:**
   ```bash
   git status
   git diff
   ```

2. **Usa el archivo de ejemplo:**
   - Mantén `env.example` actualizado
   - Documenta qué hace cada variable
   - NO pongas valores reales en `env.example`

3. **Revisa el `.gitignore`:**
   - Asegúrate de que `.env` esté listado
   - Verifica que funcione correctamente

### Durante el Despliegue

1. **En Render (Bot):**
   - Configura las variables de entorno en el dashboard
   - NO las pongas en el código

2. **En Streamlit Cloud (Dashboard):**
   - Usa la sección "Secrets" en Advanced Settings
   - Formato TOML, no .env

3. **En GitHub Actions (CI/CD):**
   - Usa GitHub Secrets
   - Settings → Secrets and variables → Actions

## 🎓 Para el Profesor/Evaluador

Si necesitas las claves para probar el proyecto:

1. **NO busques el archivo `.env`** (no debe estar en el repo)
2. **Usa `env.example`** como guía
3. **Pide las claves por un canal seguro** (no por GitHub Issues)
4. **O crea tus propias claves** siguiendo el README.md

## ✅ Verificación de Seguridad

Ejecuta este checklist antes de hacer push:

```bash
# 1. Verifica que .env esté en .gitignore
cat .gitignore | grep ".env"

# 2. Verifica que .env NO esté en staging
git status | grep ".env"

# 3. Verifica que .env NO esté en el repositorio
git ls-files | grep ".env"

# Si alguno de los comandos 2 o 3 muestra .env, NO HAGAS PUSH
```

## 📞 Contacto de Seguridad

Si descubres alguna clave expuesta en el repositorio:
1. NO la uses
2. Contacta inmediatamente al propietario
3. El propietario debe regenerar TODAS las claves

---

**Recuerda**: Es mejor prevenir que curar. Nunca subas claves API a repositorios públicos.

