from celery import shared_task
from app.models import EmailReader
from app.helpers import read_unread_emails


@shared_task
def email_reader():
    unread_emails = read_unread_emails()
    keyword = ["Hello", "My", "Name"]

    for email_data in unread_emails:
        print(f"From: {email_data['mail_from'][1]}")
        email_reader = EmailReader(
            from_email=email_data["mail_from"][1],
            to_email=email_data["mail_to"],
            email_subject=email_data["mail_subject"],
            email_body=email_data["body"],
        )
        email_reader.save()
        print(f"To: {email_data['mail_to']}")
        print(f"Subject: {email_data['mail_subject']}")
        print(f"Body:\n{email_data['body']}\n{'=' * 40}\n")

        for kw in keyword:
            if kw.lower() in email_data["body"].lower():
                print(f"'{kw}' is available in the message body")
            else:
                print(f"'{kw}' is not found in the message body")
