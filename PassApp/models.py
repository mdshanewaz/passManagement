from django.db import models
from datetime import timedelta
from django.utils.timezone import now

# Create your models here.

class CredentialModel(models.Model):
    # user = models.ForeignKey
    platform_name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    credential = models.CharField(max_length=100, null=True, blank=True)
    login_link = models.CharField(max_length=1000, null=True, blank=True)
    backup_mail_num = models.CharField(max_length=100, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.platform_name