import os
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
load_dotenv()

# Function to create database if it does not exist
def create_database(dbname):
    # Connect to the default database
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD')
    )
    conn.autocommit = True
    cur = conn.cursor()

    # Check if the database exists
    cur.execute(sql.SQL("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s"), [dbname])
    exists = cur.fetchone()

    if not exists:
        # Create the database if it does not exist
        cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(dbname)))
        print(f"Database '{dbname}' created.")
    else:
        print(f"Database '{dbname}' already exists.")

    cur.close()
    conn.close()

# Call the function to create the database
create_database("flask_db")

# Now connect to the newly created (or existing) database
conn = psycopg2.connect(
    host="localhost",
    database="flask_db",
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD']
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table

cur.execute('''
CREATE TABLE IF NOT EXISTS "Role" (
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR(20) NOT NULL UNIQUE,
    "description" TEXT NOT NULL
);
''')
cur.execute('''
CREATE TABLE IF NOT EXISTS "User" (
    id SERIAL PRIMARY KEY,
    username VARCHAR(150) NOT NULL UNIQUE,
    email VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    role_id INTEGER,
    is_admin BOOLEAN DEFAULT FALSE,
    active BOOLEAN,
    fs_uniquifier VARCHAR(255) NOT NULL UNIQUE,
    FOREIGN KEY (role_id) REFERENCES "Role" (id)
);
''')
cur.execute('''
CREATE TABLE IF NOT EXISTS "UserRole" (
    "user_id" INTEGER,
    "role_id" INTEGER,
    FOREIGN KEY ("user_id") REFERENCES "User" ("id"),
    FOREIGN KEY ("role_id") REFERENCES "Role" ("id"),
    PRIMARY KEY ("user_id", "role_id")
);
''')



# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
