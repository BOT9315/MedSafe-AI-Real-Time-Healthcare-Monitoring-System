🏥 MedSafe AI – Real-Time Healthcare Monitoring System
📌 Project Overview
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
MedSafe AI is an AI-powered real-time healthcare monitoring system that analyzes patient vital signs and detects abnormal health conditions automatically.

The system streams patient data in real time using Apache Kafka, analyzes it using machine learning models, and displays results on a live dashboard.

If a dangerous health anomaly is detected, the system can trigger alerts to notify medical staff.

🚀 Features

✔ Real-time patient data streaming
✔ AI-based anomaly detection
✔ Autoencoder deep learning model
✔ Isolation Forest anomaly detection
✔ Kafka-based event streaming
✔ Live monitoring dashboard (Streamlit)
✔ Email alert system for critical cases
✔ Scalable architecture



🧠 System Architecture
Patient Data Generator
        │
        ▼
   Apache Kafka
        │
        ▼
AI Anomaly Detection
(Autoencoder + Isolation Forest)
        │
        ▼
 Severity Classification
        │
   ┌────┴─────┐
   ▼          ▼
Database   Streamlit Dashboard
(Optional)    Monitoring

Patient Data Generator
        │
        ▼
   Apache Kafka
        │
        ▼
AI Anomaly Detection
(Autoencoder + Isolation Forest)
        │
        ▼
 Severity Classification
        │
   ┌────┴─────┐
   ▼          ▼
Database   Streamlit Dashboard
(Optional)    Monitoring



📂 Project Structure
MedSafeAI
│
├── producer.py
├── consumer.py
├── dashboard.py
│

├── models
│   └── autoencoder_model.h5
│

├── database
│   └── db.py
│

├── utils
│   ├── preprocessing.py
│   └── email_alert.py
│

├── requirements.txt
│

└── README.md


⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/BOT9315/MedSafe-AI-Real-Time-Healthcare-Monitoring-System.git
cd MedSafeAI

2️⃣ Create Virtual Environment
python -m venv .venv

Activate it:
Windows
.venv\Scripts\activate

Linux / Mac
source .venv/bin/activate



3️⃣ Install Dependencies
pip install -r requirements.txt
If requirements file does not exist:
pip install kafka-python numpy scikit-learn tensorflow streamlit

🔌 Apache Kafka Setup
Download Kafka Binary
https://kafka.apache.org/community/downloads
Extract Kafka to:
C:\kafka


Start Kafka Server
Open PowerShell:
cd C:\kafka

Start Kafka (KRaft mode)
.\bin\windows\kafka-server-start.bat .\config\server.properties

Create Kafka Topic
.\bin\windows\kafka-topics.bat --create --topic patient_vitals --bootstrap-server localhost:9092

▶ Running the Project
1️⃣ Start Kafka
cd C:\kafka
.\bin\windows\kafka-server-start.bat .\config\server.properties
2️⃣ Run Data Producer
python producer.py

This script generates patient vital signs and sends them to Kafka.
Example Output:
Sent: {'patient_id': 'P3', 'heart_rate': 110, 'temperature': 38.5, 'blood_pressure': 160}

3️⃣ Run AI Consumer
python consumer.py

4️⃣ Run Dashboard
streamlit run dashboard.py

Open in browser:
http://localhost:8501

📊 Example Patient Data
{
 "patient_id": "P4",
 "heart_rate": 125,
 "temperature": 39.1,
 "blood_pressure": 170
}


⚠️ Severity Classification
Anomaly Score	Severity
< 0.3	LOW
0.3 – 0.6	MEDIUM
> 0.6	HIGH


📧 Email Alert System

When the anomaly severity is HIGH, the system sends an alert email to notify healthcare staff.
Example alert:
Patient P4 has abnormal vital signs.
Heart Rate: 125
Temperature: 39.1
Blood Pressure: 170
Severity: HIGH

📈 Future Improvements
1.Integration with IoT medical devices
2.Real hospital patient dataset
3.Advanced deep learning models
4.Mobile app dashboard
5.Doctor notification system


👨‍💻 Author
Ankush Kumar
AI / Machine Learning Developer

📜 License
This project is licensed under the MIT License.
