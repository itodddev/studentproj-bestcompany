import smtplib, ssl
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(message):
    host = os.getenv("HOST")
    print(host)
    port = int(os.getenv("PORT"))
    print(port)
    username = os.getenv("FROM_EMAIL")
    print(username)
    password = os.getenv("PASSWORD")
    print(password)
    receiver = os.getenv("RECEIVER")
    print(receiver)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
        server.quit()


if __name__ == "__main__":
    send_email("Test Message")
