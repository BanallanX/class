#!/usr/bin/python

import httplib
import base64
import string

host = "3.17.10.219"
user = "student" 
password = "P@ssw0rd"

authToken = base64.encodestring('%s:%s' % (user, password)).replace('\n', '')
print(authToken)

request = httplib.HTTP(host)
request.putrequest("Get", "/")
request.putheader("host", host)
request.putheader("Authorization", "Basic %s" % authToken)
request.endheaders()
request.send("")

print(request)
statusCode, statusMsg, headers = request.getreply()
print("Response: ", statusCode, statusMsg, headers)