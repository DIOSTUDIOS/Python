import time
from uuid import uuid4
import requests

def test():
    url = r'http://116.182.12.53:8001/gateway/api/1/ee48fe4f3ab049f394fd153d7bc3731a?AppKey=7d795dc894ef40f7a12e989b74f0f821'
    xClientId = 'cd9ea0ea10f9473d8ddec6d8c78a65a0'
    xTimeStamp = time.time()
    xNonce = uuid4()
    xSecret = ''
    xAppKey = '7d795dc894ef40f7a12e989b74f0f821'
    xSignature = ''

    print(xTimeStamp)
    print(xNonce)

    response = requests.get(url=url, timeout=500).text

    print(response)


if __name__ == '__main__':
    test()
