import get_credentials as cred
import inbox_conn as inbox
import deleting as dele
import be_seen as seen

def main():
    choice = int(input("Do you want to:\n1 - delete the emails\n2 - mark them as seen\n"))
    credentials = cred.load_credentials('/path/to/credentials.yaml')
    mail = inbox.connect_to_gmail_imap(*credentials)
    if (choice == 1):
        summary = dele.get_emails_to_delete(mail, '/path/to/emails_to_delete.json')
    elif (choice == 2):
        summary = seen.get_emails_to_be_seen(mail, '/path/to/emails_to_mark_as_seen.json')
    print(summary)
    return 0
    
if __name__ == "__main__":
    main()