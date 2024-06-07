import imaplib
import email
from email.header import decode_header
import html2text

# Account credentials
username = "your_email@gmail.com"
password = "your_password"

# Connect to the server
mail = imaplib.IMAP4_SSL("imap.gmail.com")

# Login to your account
mail.login(username, password)

# Select the mailbox you want to use
mail.select("inbox")

# Search for all emails in the mailbox
status, messages = mail.search(None, "ALL")

# Convert messages to a list of email IDs
email_ids = messages[0].split()

# Loop through email IDs to fetch and print emails
for email_id in email_ids:
    status, msg_data = mail.fetch(email_id, "(RFC822)")
    
    # msg_data is a list with a tuple with the second element being the message
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding if encoding else "utf-8")
            
            from_ = msg.get("From")
            print("Subject:", subject)
            print("From:", from_)
            
            # Check if the email message is multipart
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))

                    try:
                        body = part.get_payload(decode=True).decode()
                    except:
                        pass
                    
                    if "attachment" not in content_disposition:
                        if content_type == "text/plain":
                            print("Body:", body)
                        elif content_type == "text/html":
                            print("HTML Body:", html2text.html2text(body))
                    else:
                        print("Attachment:", part.get_filename())
            else:
                content_type = msg.get_content_type()
                body = msg.get_payload(decode=True).decode()
                if content_type == "text/plain":
                    print("Body:", body)
                elif content_type == "text/html":
                    print("HTML Body:", html2text.html2text(body))
            print("="*100)

# Logout
mail.logout()
