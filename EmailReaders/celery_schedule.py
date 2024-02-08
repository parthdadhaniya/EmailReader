CELERY_BEAT_SCHEDULE = {
    "email_reader": {
        "task": "EmailReaders.app.tasks.email_reader",
        "schedule": 900.0,  # 900 seconds = 15 minutes
    },
}
