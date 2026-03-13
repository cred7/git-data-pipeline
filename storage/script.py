import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5445,
    database="github",
    user="postgres",
    password="postgres"
)
cur = conn.cursor()
cur.execute("""
CREATE TABLE github_events (
    id SERIAL PRIMARY KEY,
    event_type TEXT,
    repo TEXT,
    user_login TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

conn.commit()
cur.close()
conn.close()

print("Database and table ready!")

# cur = conn.cursor()
# with open('schema.sql', 'r') as f:
#     sql_commands = f.read()
# cur.execute(sql_commands)
# conn.commit()
# cur.close()
# conn.close()
# print("Database setup completed successfully!")
