from kafka import KafkaConsumer
import json
import numpy as np
from sklearn.ensemble import IsolationForest
from tensorflow.keras.models import load_model
from database.db import SessionLocal, insert_patient_data
from utils.preprocessing import preprocess_vitals
from utils.email_alert import send_email_alert

# Load pre-trained models
autoencoder = load_model("models/autoencoder_model.h5")
iso_forest = IsolationForest(contamination=0.1)
# If pre-trained: iso_forest = joblib.load("models/isolation_forest.pkl")

consumer = KafkaConsumer(
    'patient_vitals',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

session = SessionLocal()

def compute_anomaly(vitals):
    x = preprocess_vitals(vitals)
    # Autoencoder reconstruction error
    recon = autoencoder.predict(np.array([x]))
    error = np.mean(np.square(x - recon))
    # Isolation Forest
    iso_score = iso_forest.score_samples(np.array([x]))[0]
    anomaly_score = (error + abs(iso_score)) / 2
    return anomaly_score

def classify_severity(score):
    if score < 0.3:
        return "LOW"
    elif score < 0.6:
        return "MEDIUM"
    else:
        return "HIGH"

for message in consumer:
    vitals = message.value
    score = compute_anomaly(vitals)
    severity = classify_severity(score)
    vitals.update({"anomaly_score": score, "severity": severity})
    

    insert_patient_data(session, vitals)

    if severity == "HIGH":
        send_email_alert(vitals)

    print("Processed:", vitals)
