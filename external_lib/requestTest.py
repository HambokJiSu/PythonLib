#	pip install requests

#	게시물 1건 조회(GET)
import requests
from pprint import pprint

#url = 'https://jsonplaceholder.typicode.com/posts/1'	#	단건
url = 'https://jsonplaceholder.typicode.com/posts'	#	리스트형 게시물
res = requests.get(url)
pprint(res.json())

"""
조회(GET)
사용자 번호(userId)가 1인 게시물만 조회하려면 다음과 같이 서비스를 호출해야 한다.

항목	설명
URL	https://jsonplaceholder.typicode.com/posts?userId=1
HTTP METHOD	GET
"""
import requests
import pprint

url = 'https://jsonplaceholder.typicode.com/posts'
params = {'userId': 1}
res = requests.get(url, params=params)
pprint.pprint(res.json())

#	게시물 저장(POST)
import requests
import pprint
import json

url = 'https://jsonplaceholder.typicode.com/posts'
headers = {'Content-type': 'application/json; charset=utf-8'}
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1,
}

res = requests.post(url, headers=headers, data=json.dumps(data))
pprint.pprint(res.json())

#	게시물 수정(PUT)
import requests
import pprint
import json

url = 'https://jsonplaceholder.typicode.com/posts/1'
headers = {'Content-type': 'application/json; charset=utf-8'}
data = {
    'id': 1,
    'title': '제목을 수정',
    'body': '내용을 수정',
    'userId': 1,
}
res = requests.put(url, headers=headers, data=json.dumps(data))
pprint.pprint(res.json())

#	게시물 일부 속성 수정(PATCH)
import requests
import pprint
import json

url = 'https://jsonplaceholder.typicode.com/posts/1'
headers = {'Content-type': 'application/json; charset=utf-8'}
data = {
    'title': 'foo',
}
res = requests.patch(url, headers=headers, data=json.dumps(data))
pprint.pprint(res.json())

#	게시물 삭제(DELETE)
import requests
import pprint

url = 'https://jsonplaceholder.typicode.com/posts/1'
res = requests.delete(url)
pprint.pprint(res.json())