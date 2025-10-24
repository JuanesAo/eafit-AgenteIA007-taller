"""
Script para resetear el bot de Telegram y limpiar webhooks
"""
import os
from dotenv import load_dotenv
import requests

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    print("❌ No se encontró TELEGRAM_TOKEN en .env")
    exit(1)

# 1. Eliminar webhook
print("🔄 Eliminando webhook...")
url = f"https://api.telegram.org/bot{TOKEN}/deleteWebhook?drop_pending_updates=True"
response = requests.get(url)
print(f"✅ Respuesta: {response.json()}")

# 2. Ver información del bot
print("\n📊 Información del bot:")
url = f"https://api.telegram.org/bot{TOKEN}/getMe"
response = requests.get(url)
print(f"✅ {response.json()}")

# 3. Ver información de webhook
print("\n🔍 Estado del webhook:")
url = f"https://api.telegram.org/bot{TOKEN}/getWebhookInfo"
response = requests.get(url)
print(f"✅ {response.json()}")

print("\n✅ Bot reseteado. Ahora puedes ejecutar: python bot.py")

