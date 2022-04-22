import re
import requests
import sys

def fingerprint_web_server(argv):
    req = requests.get('http://'+argv[1])
    headers = ['Server', 'Date','Last-Modified','ETag','Accept-Ranges','Content-Length','Connection','Content-Type','Content-Encoding']
    print("\nHTTP/%.1f %d \n"%(req.raw.version/10,req.status_code))
    if(len(argv) == 3 and argv[2] == '-a'):
        for header in req.headers:
            result = req.headers[header]
            print('%s: %s' % (header, result))
    else:
        for header in headers:
            try:
                result = req.headers[header]
                print('%s: %s' % (header, result))
            except Exception as error:
                print("%s : Not found"%(header))
        for header in req.headers:
            result = req.headers[header]
            if(header.startswith('X-') or header.startswith('x-')):
                print('%s: %s' % (header, result))

if __name__ == "__main__":
    try:
        fingerprint_web_server(sys.argv)
    except:
        print("An error occured... Try a different URL")