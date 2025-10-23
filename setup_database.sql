-- Script SQL para crear la tabla de historial de chat en Supabase
-- Ejecuta este script en el SQL Editor de tu proyecto Supabase

-- Crear la tabla chat_history
CREATE TABLE IF NOT EXISTS chat_history (
    id BIGSERIAL PRIMARY KEY,
    user_id TEXT NOT NULL,
    sender_role TEXT NOT NULL CHECK (sender_role IN ('user', 'ai')),
    message TEXT NOT NULL,
    timestamp TIMESTAMPTZ DEFAULT NOW()
);

-- Crear índices para mejorar el rendimiento de las consultas
CREATE INDEX IF NOT EXISTS idx_chat_history_user_id ON chat_history(user_id);
CREATE INDEX IF NOT EXISTS idx_chat_history_timestamp ON chat_history(timestamp);
CREATE INDEX IF NOT EXISTS idx_chat_history_user_timestamp ON chat_history(user_id, timestamp);

-- Habilitar Row Level Security (RLS) - Opcional pero recomendado
ALTER TABLE chat_history ENABLE ROW LEVEL SECURITY;

-- Crear política para permitir todas las operaciones (para desarrollo)
-- NOTA: En producción, deberías crear políticas más restrictivas
CREATE POLICY "Enable all operations for service role" 
ON chat_history 
FOR ALL 
USING (true) 
WITH CHECK (true);

-- Comentarios en las columnas para documentación
COMMENT ON TABLE chat_history IS 'Almacena el historial completo de conversaciones entre usuarios y el agente IA';
COMMENT ON COLUMN chat_history.id IS 'Identificador único del mensaje';
COMMENT ON COLUMN chat_history.user_id IS 'ID del usuario de Telegram';
COMMENT ON COLUMN chat_history.sender_role IS 'Rol del emisor: "user" para mensajes del usuario, "ai" para respuestas del agente';
COMMENT ON COLUMN chat_history.message IS 'Contenido del mensaje';
COMMENT ON COLUMN chat_history.timestamp IS 'Fecha y hora de creación del mensaje';

