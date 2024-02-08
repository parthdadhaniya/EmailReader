from django.db import models

# Create your models here.


class EmailReader(models.Model):
    from_email = models.EmailField(verbose_name="From Email")
    to_email = models.EmailField(verbose_name="To Email")
    email_subject = models.CharField(max_length=255, verbose_name="Email Subject")
    email_body = models.TextField(verbose_name="Email Body")

    def __str__(self):
        return str(self.from_email)
