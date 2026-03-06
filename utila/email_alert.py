import smtplib
from email.mime.text import MIMEText

def send_email_alert(vitals):
    sender = "your_email@gmail.com"
    receiver = "doctor_email@example.com"
    msg = MIMEText(f"High-severity alert for patient {vitals['patient_id']}: {vitals}")
    msg['Subject'] = "MEDSAFE AI ALERT"
    msg['From'] = sender
    msg['To'] = receiver

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, "YOUR_PASSWORD")
        server.sendmail(sender, receiver, msg.as_string())
