import re
from urllib import response
import requests
import httplib2
req = requests.get('http://www.cloudflare.com')
headers = ['Server', 'Date','Last-Modified','ETag','Content-Length','Accept-Ranges','Connection','Content-Type']
print(req.raw.version/10)
print(req.status_code)
for header in headers:
    try:
        result = req.headers[header]
        print('%s: %s' % (header, result))
    except Exception as error:
        continue

print("\nCustom headers used by the website: \n")

for header in req.headers:
    result = req.headers[header]
    if(header.startswith('X-')):
        print('%s: %s' % (header, result))
