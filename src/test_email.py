import os
import smtplib
from email.mime.text import MIMEText


def send_email(subject, body, to_email):
    """Send email"""
    from_email = os.getenv("EMAIL_USER")
    from_password = os.getenv("EMAIL_PASSWORD")

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(from_email, from_password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()


if __name__ == "__main__":
    send_email("Book Notification Test", "This is test email", os.getenv("EMAIL_USER"))
