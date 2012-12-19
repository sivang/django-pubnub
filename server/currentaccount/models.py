from django.db import models
from djangotoolbox.fields import ListField
from django.contrib.auth.models import User
from hashlib import sha512
import time

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
        self.notif_channel = sha512(''.join([time.ctime(), self.rstring()])).hexdigest()
        # save for usage by publishing mechanism
        self.save()
        return self.notif_channel

    def get_ckey(self):
        # this key encrypts data such that pubnub cannot see it.
        self.ckey = sha512(''.join([time.ctime(), self.owner.username])).hexdigest()
        self.save()
        return self.ckey

    def push_cbk(self, sender, **kwargs):
        # this functions handles sending push notif to 
        # 3rd party push notification service.
        print 'ckey:', self.ckey
        print 'notif_channel:',self.notif_channel
        print 'account updated!'


