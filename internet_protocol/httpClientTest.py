#	웹 페이지를 저장하는 또 다른 방법은? ― http.client
import http.client

def get_wikidocs_GetMethod(page):
	
	conn = http.client.HTTPSConnection("wikidocs.net")
	conn.request("GET", "/12")
	r = conn.getresponse()
	with open('wikidocs_%s.html' % page, 'wb') as f:
		f.write(r.read())
	conn.close()

def get_wikidocs_PostMethod(page):
	import urllib

	conn = http.client.HTTPSConnection("wikidocs.net")
	params = urllib.parse.urlencode({'@name': '홍길동', '@age': 55})
	headers = {"Content-type": "application/x-www-form-urlencoded"}
	conn.request("POST", "/12", params, headers)
	r = conn.getresponse()
	with open('wikidocs_%s.html' % page, 'wb') as f:
		f.write(r.read())
	conn.close()

if __name__ == "__main__":
	get_wikidocs_GetMethod(12)
	get_wikidocs_PostMethod(32)