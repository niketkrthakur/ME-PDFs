import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        port=os.getenv("DB_PORT"),
        sslmode="require"
    )

def init_db():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pdf_sessions (
            id SERIAL PRIMARY KEY,
            filename TEXT,
            extracted_text TEXT,
            created_at TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_messages (
            id SERIAL PRIMARY KEY,
            session_id INTEGER,
            role TEXT,
            message TEXT,
            created_at TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS files (
            id SERIAL PRIMARY KEY,
            filename TEXT,
            url TEXT,
            uploaded_at TIMESTAMP,
            user_id TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS contact_messages (
            id SERIAL PRIMARY KEY,
            name TEXT,
            email TEXT,
            message TEXT,
            created_at TIMESTAMP
        )
        """)

        conn.commit()
        conn.close()

        print("DB CONNECTED & TABLES READY")

    except Exception as e:
        print("DB ERROR:", e)