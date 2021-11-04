import requests
import time
from pprint import pprint
import json

url = "http://127.0.0.1:5000/endpoint"

def main():
    for item in [{"id":1,"vals":"1,2"}, {"id":1,"vals":"b,1"}, {"id":1,"vals":"2,3"}]:
        res = requests.post(url, json.dumps(item))
        print(res)
        pprint(res.content.decode('utf8'))
        time.sleep(2)

if __name__ == "__main__":
    main()