from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

while True:
    vitals = {
        "patient_id": f"P{random.randint(1,10)}",
        "heart_rate": random.randint(60, 130),
        "temperature": round(random.uniform(36, 40), 1),
        "blood_pressure": random.randint(110, 180)
    }
    producer.send('patient_vitals', vitals)
    print("Sent:", vitals)
    time.sleep(2)
