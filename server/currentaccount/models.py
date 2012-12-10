from django.db import models
from djangotoolbox.fields import ListField
from django.contrib.auth.models import User

MAX_CHAR_LENGTH = 20

class CurrentAccount(models.Model):
    # for a real system this'd better be a pointer to a user account.
    user = models.ForeignKey(User)
    balance = models.FloatField(default=0)

    def __unicode__(self):
        return user, ' ', balance


# Create your models here.
