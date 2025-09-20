import psycopg2
import json
import numpy as np
from BackEnd import Comparison
# Database connection details
DB_NAME = "neuroshield"
DB_USER = "postgres"
DB_PASSWORD = "Root"
DB_HOST = "localhost"
DB_PORT = "5432"

def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

def create_table():
    """Creates the table to store neural keys if it doesn't exist."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS neural_keys (
            user_id int PRIMARY KEY,
            features TEXT NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def save_neural_key(user_id, features):
    features_str = json.dumps(features.tolist()) 
    """Insert or update a neural key for a given user ID."""
    conn = get_connection()
    cur = conn.cursor()
    # Upsert: insert or update if exists
    cur.execute("""
        INSERT INTO neural_keys (user_id, features)
        VALUES (%s, %s)
        ON CONFLICT (user_id) 
        DO UPDATE SET features = EXCLUDED.features;
    """, (user_id, features_str))
    conn.commit()
    cur.close()
    conn.close()

def verify_neural_key(user_id, features_new):
    """Check if the neural key for a given user ID matches."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT features FROM neural_keys WHERE user_id = %s;", (user_id,))
    result = cur.fetchone()
    
    cur.close()
    conn.close()
    
    # Convert stored features to numpy array or set to None if user doesn't exist
    features_stored = np.array(json.loads(result[0])) if result else None
    
    # Call the comparison function
    return Comparison.is_match(features_new, features_stored, 0.85)

