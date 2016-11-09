import requests
import argparse

parser = argparse.ArgumentParser(description="Elasticsearch")
parser.add_argument('--url', help='Target url', dest='url', metavar='')
parser.add_argument('--host', help='Target host (default localhost)', dest='host', default='localhost', metavar='')
parser.add_argument('--port', help='Target port (default 9200)', dest='port', default='9200', metavar='')
parser.add_argument('--method', help='HTTP Method (default GET)', dest='method', default='get', metavar='')

args = parser.parse_args()

req_url = 'http://' + args.host + ':' + str(args.port) + args.url

res = requests.request(method=args.method, url=req_url)
print(res.text)
