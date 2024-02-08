import email
import imaplib
from django.conf import settings

username = settings.USERNAME
password = settings.PASSWORD
sender_of_interest = None


def read_unread_emails():
    try:
        # Login to the IMAP server (e.g., Gmail)
        imap = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        imap.login(username, password)
        imap.select("INBOX")

        # Retrieve unread messages
        if sender_of_interest:
            status, response = imap.uid(
                "search", None, "UNSEEN", "FROM {0}".format(sender_of_interest)
            )
        else:
            status, response = imap.uid("search", None, "UNSEEN")

        if status == "OK":
            unread_msg_nums = response[0].split()
        else:
            unread_msg_nums = []

        email_data_list = []

        for e_id in unread_msg_nums:
            _, response = imap.uid("fetch", e_id, "(RFC822)")
            html = response[0][1].decode("utf-8")
            email_message = email.message_from_string(html)

            for part in email_message.walk():
                if part.get_content_type() == "text/plain":
                    email_body = part.get_payload(decode=True).decode("utf-8")
                    break

            # Extract relevant information
            data_dict = {
                "mail_to": email_message["To"],
                "mail_subject": email_message["Subject"],
                "mail_from": email.utils.parseaddr(email_message["From"]),
                "body": email_body,
            }
            email_data_list.append(data_dict)

        # Mark messages as read
        for e_id in unread_msg_nums:
            imap.uid("store", e_id, "+FLAGS", "\\Seen")

        return email_data_list

    except Exception as e:
        print(f"Error: {e}")
    finally:
        imap.logout()


unread_emails = read_unread_emails()

# Keyword which is you want to search in the body
