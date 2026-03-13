from kafka import KafkaConsumer
import json
import psycopg2

consumer = KafkaConsumer(
    "github-event",
    bootstrap_servers="localhost:9092",
    auto_offset_reset='earliest',
    group_id='dev_consumer',
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

conn = psycopg2.connect(
    host="localhost",
    port=5445,
    database="github",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()
count = 0
max = 30
for message in consumer:
    event = message.value

    event_type = event["type"]
    repo = event["repo"]["name"]
    user = event["actor"]["login"]

    cur.execute(
        "INSERT INTO github_events (event_type, repo, user_login) VALUES (%s,%s,%s)",
        (event_type, repo, user)
    )
    count += 1
    if count >= max:
        break

    conn.commit()
    print(f"Consumed: {event_type} | {repo} | {user}")
cur.close()
conn.close()
