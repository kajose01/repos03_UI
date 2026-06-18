from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def home():
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'db'),
        user=os.environ.get('DB_USER', 'ubuntu'),
        password=os.environ.get('DB_PASSWORD', 'jose123'),
        database=os.environ.get('DB_NAME', 'mydb')
    )
    cursor = conn.cursor()
    cursor.execute("SELECT message FROM greetings")
    result = cursor.fetchone()
    conn.close()
    return f"""
<h1>3 Tier Docker Compose mydb</h1>
<h2>{result[0]}</h2>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
