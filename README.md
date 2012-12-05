Reaindg here: http://blog.pubnub.com/pubnub-adds-cross-platform-aes-symmetric-key-encryption/ 

I decided to come up with a real word working example of how to do this from Django.
(- but the proceedings should be quite similar with any other framework)

(My original use case is to be able to do pub/sub push notifs without introducing more programming
language technologies to an existing Python stack).

PubNub gives you a *lot* , indeed. But these you need to take care yourself for secured per user
notifications:

* Creating *unique* private channel ID per user, make that known only to the user and the Python server to
  make sure encryption attacks are harder.
* Create a cipher key per user that will be used to encrypt communications to and from the user.
* This demo simulates a points' account, where points are earned from an external source:
  - Everytime points are being deposited into his account he'll get real time notification.
  - Same goes if his account is being deducted for points he uses (hypothetically).

