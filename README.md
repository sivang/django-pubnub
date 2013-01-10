Django Example Application-- use PubNub to Deliver Real Time Notifications
===========================================================================

Reaindg here: http://blog.pubnub.com/pubnub-adds-cross-platform-aes-symmetric-key-encryption/ 

I was lacking a real word working example of how to do this from Django, so I decided to write one myself.
(- but the proceedings should be quite similar with any other framework)

Rationale
=========

Having an existing Python stack, I did not want to introduce more technologies. 

This simulates a bank account that has a status page for the balance, where balance can be changed out of band by either administrator on the Django admin, or via the REST call (as shown below) by an app or so.

PubNub gives you a *lot* , indeed. However, for this you'd have to care yourself for secured per user
notifications:

* Creating *unique* private channel ID per user, make that known only to the user and the Python server to
  make encryption attacks are harder.
* Save that ID as per the user in your db, and make it available to code parts that need it.
* Refresh that ID everytime a user lands on his status page, making attacks even harder.

How To Use
==========

Point your browser at: `http://django-pubnub.herokuapp.com/current_account/my`

(login if required, the creds are the same as used in the below REST call)

Leave this screen in your browser, then to create an update event for the balance of an account:

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

And watch the notification received in the browser view!
