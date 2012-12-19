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

$ curl --basic -u "test:957431cbfaa05551a59bb087ad4de5370a9e521c4c455b27ba6b06d5cf4068a3" -v -H "Content-type: application/json" -X PATCH http://localhost:8000/api/v1/account/50d1a999da907a142711dea0/ -d '{"balance" : 2500}'
* About to connect() to localhost port 8000 (#0)
*   Trying ::1... Connection refused
*   Trying 127.0.0.1... connected
* Server auth using Basic with user 'test'
> PATCH /api/v1/account/50d1a999da907a142711dea0/ HTTP/1.1
> Authorization: Basic dGVzdDo5NTc0MzFjYmZhYTA1NTUxYTU5YmIwODdhZDRkZTUzNzBhOWU1MjFjNGM0NTViMjdiYTZiMDZkNWNmNDA2OGEz
> User-Agent: curl/7.22.0 (x86_64-pc-linux-gnu) libcurl/7.22.0 OpenSSL/1.0.1 zlib/1.2.3.4 libidn/1.23 librtmp/2.3
> Host: localhost:8000
> Accept: */*
> Content-type: application/json
> Content-Length: 18
> 
* upload completely sent off: 18out of 18 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 202 ACCEPTED
< Date: Wed, 19 Dec 2012 12:11:18 GMT
< Server: WSGIServer/0.1 Python/2.7.3
< Content-Type: text/html; charset=utf-8
< 
* Closing connection #0

