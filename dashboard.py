import streamlit as st
import time
import random
import pandas as pd

st.title("MedSafe AI - Patient Monitoring Dashboard")

data = []

placeholder = st.empty()

while True:
    new_data = {
        "patient_id": f"P{random.randint(1,10)}",
        "heart_rate": random.randint(60,130),
        "temperature": round(random.uniform(36,40),1),
        "blood_pressure": random.randint(110,180)
    }

    data.append(new_data)

    df = pd.DataFrame(data)

    with placeholder.container():
        st.write("Live Patient Vitals")
        st.dataframe(df)

    time.sleep(2)