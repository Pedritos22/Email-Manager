import imaplib
import logging

def connect_to_gmail_imap(user, password):
    imap_url = 'imap.gmail.com'
    try:
        mail = imaplib.IMAP4_SSL(imap_url)
        mail.login(user, password)
        mail.select('inbox')
        return mail
    except Exception as e:
        logging.error(f"Connection failed: {e}")
        raise
