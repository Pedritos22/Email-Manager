import pandas as pd
import json

def get_emails_to_be_seen(mail, filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
        emails_to_mark = data['emails']
    mail.select("inbox")

    summary_rows = []

    for email in emails_to_mark:
        _, data = mail.search(None, f'FROM "{email}"')
        if data[0]:
            msg_ids = data[0].decode().split()
            if msg_ids:
                mail.store(','.join(msg_ids), '+FLAGS', '\\Seen')
                summary_rows.append({'Email': email, 'Count': len(msg_ids)})
            else:
                summary_rows.append({'Email': email, 'Count': 0})
        else:
            summary_rows.append({'Email': email, 'Count': 0})
    mail.expunge()
    mail.close()
    mail.logout()
    return pd.DataFrame(summary_rows)
