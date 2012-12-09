from django.db import models
from djangotoolbox.fields import ListField

MAX_CHAR_LENGTH = 20

class CurrentAccount(models.Model):
    owner = models.CharField(max_length=MAX_CHAR_LENGTH) # for a real system this'd better be a pointer to a user account.
    account_type = models.CharField(max_length=MAX_CHAR_LENGTH)
    balance = models.FloatField(default=0)


# Create your models here.
