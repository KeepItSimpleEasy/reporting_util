import smtplib
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class MailUtil:

    @staticmethod
    def send_mail(send_from, send_to, cc="", subject="", text="", files=[], server="localhost"):
        # assert type(send_to) == list
        # assert type(files) == list
        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = send_from
        message["To"] = send_to
        message["Subject"] = subject
        message["Cc"] = cc
        message["Bcc"] = send_to  # Recommended for mass emails
        # Add body to email
        message.attach(MIMEText(text, "html"))
        for f in files:
            part = MIMEBase('application', "octet-stream")
            part.set_payload(open(f, "rb").read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
            message.attach(part)

        text = message.as_string()
        # Log in to server using secure context and send email
        with smtplib.SMTP(server) as email_server:
            email_server.sendmail(send_from, send_to.split(",") + cc.split(","), text)
            email_server.quit()
