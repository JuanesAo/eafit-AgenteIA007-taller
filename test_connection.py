"""
Script de prueba para verificar la conectividad con todos los servicios
Ejecuta este script antes de iniciar el bot para asegurarte de que todo funciona
"""

import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def test_environment_variables():
    """Verifica que todas las variables de entorno estén configuradas"""
    print("🔍 Verificando variables de entorno...")
    
    required_vars = {
        'TELEGRAM_TOKEN': os.getenv('TELEGRAM_TOKEN'),
        'GROQ_API_KEY': os.getenv('GROQ_API_KEY'),
        'SUPABASE_URL': os.getenv('SUPABASE_URL'),
        'SUPABASE_KEY': os.getenv('SUPABASE_KEY')
    }
    
    all_good = True
    for var_name, var_value in required_vars.items():
        if var_value:
            print(f"  ✅ {var_name}: Configurada")
        else:
            print(f"  ❌ {var_name}: NO CONFIGURADA")
            all_good = False
    
    return all_good

def test_groq_connection():
    """Prueba la conexión con Groq API"""
    print("\n🧠 Probando conexión con Groq...")
    try:
        from langchain_groq import ChatGroq
        
        llm = ChatGroq(
            model="llama3-8b-8192",
            temperature=0.3
        )
        
        response = llm.invoke("Di 'Hola mundo' en una palabra")
        print(f"  ✅ Groq funciona correctamente")
        print(f"  📝 Respuesta de prueba: {response.content}")
        return True
    except Exception as e:
        print(f"  ❌ Error con Groq: {e}")
        return False

def test_supabase_connection():
    """Prueba la conexión con Supabase"""
    print("\n💾 Probando conexión con Supabase...")
    try:
        from supabase import create_client
        
        SUPABASE_URL = os.getenv("SUPABASE_URL")
        SUPABASE_KEY = os.getenv("SUPABASE_KEY")
        
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        # Intentar leer de la tabla
        response = supabase.table('chat_history').select('*').limit(1).execute()
        
        print(f"  ✅ Supabase funciona correctamente")
        print(f"  📊 Tabla 'chat_history' accesible")
        return True
    except Exception as e:
        print(f"  ❌ Error con Supabase: {e}")
        print(f"  💡 Asegúrate de haber ejecutado el script setup_database.sql")
        return False

def test_telegram_token():
    """Valida el formato del token de Telegram"""
    print("\n📱 Validando token de Telegram...")
    
    token = os.getenv('TELEGRAM_TOKEN')
    if not token:
        print("  ❌ Token no configurado")
        return False
    
    # Los tokens de Telegram tienen el formato: 123456789:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
    if ':' in token and len(token.split(':')) == 2:
        print("  ✅ Formato del token válido")
        return True
    else:
        print("  ❌ Formato del token inválido")
        return False

def main():
    print("=" * 60)
    print("🔧 TEST DE CONECTIVIDAD - Sistema de Agente Multi-Interfaz")
    print("=" * 60)
    
    results = []
    
    # Test 1: Variables de entorno
    results.append(test_environment_variables())
    
    # Test 2: Token de Telegram
    results.append(test_telegram_token())
    
    # Test 3: Supabase
    results.append(test_supabase_connection())
    
    # Test 4: Groq
    results.append(test_groq_connection())
    
    # Resultado final
    print("\n" + "=" * 60)
    if all(results):
        print("✅ TODOS LOS TESTS PASARON - El sistema está listo para usarse")
        print("=" * 60)
        print("\n📋 Próximos pasos:")
        print("  1. Ejecutar el bot: python bot.py")
        print("  2. Ejecutar el dashboard: streamlit run dashboard.py")
    else:
        print("❌ ALGUNOS TESTS FALLARON - Revisa los errores arriba")
        print("=" * 60)
        print("\n💡 Soluciones comunes:")
        print("  - Crea un archivo .env basado en .env.example")
        print("  - Ejecuta setup_database.sql en Supabase SQL Editor")
        print("  - Verifica que todas las API keys sean válidas")
    
    print()

if __name__ == '__main__':
    main()

