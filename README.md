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


To create an update event for the balance of an account:

<pre>
sivan@future:~/django-pubnub/django-pubnub$ curl --basic -u "test:957431cbfaa05551a59bb087ad4de5370a9e521c4c455b27ba6b06d5cf4068a3" -v -H "Content-type: application/json" -X PUT http://django-pubnub.herokuapp.com/api/v1/account/50d1a999da907a142711dea0/ -d '{"balance" : 2531.5}'
* About to connect() to django-pubnub.herokuapp.com port 80 (#0)
*   Trying 23.23.113.171... connected
* Server auth using Basic with user 'test'
> PUT /api/v1/account/50d1a999da907a142711dea0/ HTTP/1.1
> Authorization: Basic dGVzdDo5NTc0MzFjYmZhYTA1NTUxYTU5YmIwODdhZDRkZTUzNzBhOWU1MjFjNGM0NTViMjdiYTZiMDZkNWNmNDA2OGEz
> User-Agent: curl/7.22.0 (x86_64-pc-linux-gnu) libcurl/7.22.0 OpenSSL/1.0.1 zlib/1.2.3.4 libidn/1.23 librtmp/2.3
> Host: django-pubnub.herokuapp.com
> Accept: */*
> Content-type: application/json
> Content-Length: 20
> 
* upload completely sent off: 20out of 20 bytes
< HTTP/1.1 204 NO CONTENT
< Content-length: 0
< Content-Type: text/html; charset=utf-8
< Date: Thu, 10 Jan 2013 18:07:33 GMT
< Server: WSGIServer/0.1 Python/2.7.2
< Connection: keep-alive
< 
* Connection #0 to host django-pubnub.herokuapp.com left intact
* Closing connection #0
</pre>