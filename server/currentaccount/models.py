from django.db import models
from djangotoolbox.fields import ListField
from django.contrib.auth.models import User
from hashlib import sha512
from time import ctime

MAX_CHAR_LENGTH = 20

class CurrentAccount(models.Model):
    # for a real system this'd better be a pointer to a user account.
    owner = models.ForeignKey(User)
    balance = models.FloatField(default=0)
    ckey = None
    notif_channel = None

    def rstring(self):
        return ' '.join([self.pk, self.owner.username, str(self.balance)])

    def __unicode__(self):
        return self.rstring()

    def get_notif_channel(self):
        # create the channel based on current ctime and the account's balance
        self.notif_channel = sha512(''.join(time.ctime(), self.rstring())).hexdigest()
        # save for usage by publishing mechanism
        self.save()
        return self.notif_channel

    def get_ckey(self):
        # this key encrypts data such that pubnub cannot see it.
        self.ckey = sha512(''.join(time.ctime(), self.username)).hexdigest()
        self.save()
        return self.ckey


# Create your models here.
