from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)

# Database connection settings
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "postgres",  # Replace with your PostgreSQL database name
    "user": "postgres",  # Replace with your PostgreSQL username
    "password": 1234  # Replace with your PostgreSQL password
}

# Function to connect to PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    return conn

@app.route('/')
def index():
    # Connect to the database
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Query the coordinators and events
    cur.execute('SELECT * FROM coordinators;')  # Fetching coordinators
    coordinators = cur.fetchall()
    
    cur.execute('SELECT * FROM events;')  # Fetching events
    events = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return render_template('index.html', coordinators=coordinators, events=events)

@app.route('/wall-of-fame')
def wall_of_fame():
    # Connect to the database
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Query the winners
    cur.execute('SELECT * FROM winners ORDER BY rank;')  # Fetching winners
    winners = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return render_template('wall_of_fame.html', winners=winners)

if __name__ == "__main__":
    app.run(debug=True)
