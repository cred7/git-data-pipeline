import requests
import json
from kafka import KafkaProducer
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

url = "https://api.github.com/events"

while True:
    response = requests.get(url)
    events = response.json()

    for event in events:
        producer.send("github-event", event)
    producer.flush()

    print("sent batch")
    time.sleep(60)
