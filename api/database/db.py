from flask import Flask, jsonify
from flask_cors import CORS
from database.db import SessionLocal, PatientData

app = Flask(__name__)
CORS(app)
session = SessionLocal()

@app.route("/latest", methods=["GET"])
def latest_vitals():
    data = session.query(PatientData).order_by(PatientData.timestamp.desc()).limit(10).all()
    result = [{c.name: getattr(d, c.name) for c in d.__table__.columns} for d in data]
    return jsonify(result)

@app.route("/history/<patient_id>", methods=["GET"])
def history(patient_id):
    data = session.query(PatientData).filter(PatientData.patient_id==patient_id).all()
    result = [{c.name: getattr(d, c.name) for c in d.__table__.columns} for d in data]
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
