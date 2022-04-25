import re
import requests
import sys

def fingerprint_web_server(argv):
    headers = ['Server', 'Date','Last-Modified','ETag','Accept-Ranges','Content-Length','Connection','Content-Type','Content-Encoding']
    if(len(argv) == 3 and argv[1] == '-a'):
        req = requests.get('http://'+argv[2])
        print("\nHTTP/%.1f %d \n"%(req.raw.version/10,req.status_code))
        for header in req.headers:
            result = req.headers[header]
            print('%s: %s' % (header, result))
    elif(len(argv) == 4 and argv[1] == '-s'):
        req1 = requests.get('http://'+argv[2])
        req2 = requests.get('http://'+argv[3])
        intersection = dict(req1.headers.items() & req2.headers.items() )
        for header in intersection:
            result = req1.headers[header]
            print("%s : %s" % (header,result))
    else:
        req = requests.get('http://'+argv[1])
        print("\nHTTP/%.1f %d \n"%(req.raw.version/10,req.status_code))
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