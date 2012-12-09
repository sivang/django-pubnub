from django.db import models
from djangotoolbox.fields import ListField

MAX_CHAR_LENGTH = 20

class CurrentAccount(models.Model):
    # for a real system this'd better be a pointer to a user account.
    owner = models.CharField(max_length=MAX_CHAR_LENGTH) 
    account_type = models.CharField(max_length=MAX_CHAR_LENGTH)
    balance = models.FloatField(default=0)


# Create your models here.
