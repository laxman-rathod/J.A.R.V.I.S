import smtplib
import os
from dotenv import load_dotenv
from jarvis_speech_recognizer import speak
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

# Email credentials and details
sender_email = os.getenv('user_name')
sender_password = os.getenv('user_pass')
receiver_email = "dummyac10000@gmail.com"
subject = 'Test Email from Python'
body = 'Hello, this is a test email sent from a Python script.'

# Create message container - MIME multipart
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach body to the email
msg.attach(MIMEText(body, 'plain'))

# Establish SMTP connection
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print('Email sent successfully!')
except Exception as e:
    print(f'Error: {e}')
finally:
    server.quit()


# # Configure the SMTP server details
# smtp_server = "smtp.gmail.com"
# smtp_port = 587  # For starttls
# smtp_username = os.getenv('user_name')
# smtp_password = os.getenv('user_pass')

# # Create a secure SSL context
# import ssl
# context = ssl.create_default_context()

# # Create the SMTP server connection
# server = smtplib.SMTP(smtp_server, smtp_port)

# # Start the TLS encryption
# server.starttls(context=context)

# # Login to the SMTP server
# server.login(smtp_username, smtp_password)

# # Define the email message
# from_address = smtp_username
# to_address = "dummyac10000@gmail.com"
# subject = "Test Email from Python"
# body = "This is a test email sent from a Python script."

# # Construct the message
# msg = f"Subject: {subject}\n\n{body}"

# # Send the email
# try:
#     server.sendmail(from_address, to_address, msg)
#     print("Sir Email sent successfully!")
#     speak("Sir Email sent successfully!")
# except Exception as e:
#     print(f"Error: {e}")

# # Close the SMTP server connection
# server.quit()