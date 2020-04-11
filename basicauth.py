#!/usr/bin/python

import httplib
import base64
import string

host = "3.17.10.219"
user = "student" 
password = P@ssw0rd

authToken = base64.encodestring('%$:%$' % (user, password)).replace('\n', '')
print(authtoken)

request = httplib(host)
request.putrequest("Get", "/")
request.putheader("host", host)
request.putheader("Authorization", "Basic %$" % authToken)
request.endheaders()
request.send("")

print(request)
statusCode, statusMsg, headers = request.getreply()
print("Response: ", statusCode, statusMsg, headers)
