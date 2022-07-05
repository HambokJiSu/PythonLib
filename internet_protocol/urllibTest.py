#	웹 페이지를 저장하려면? ― urllib
import urllib.request

def get_wikidocs(page):
    print("wikidocs page:{}".format(page))  # 페이지 호출시 출력
    resource = 'https://wikidocs.net/{}'.format(page)
    with urllib.request.urlopen(resource) as s:
        with open('wikidocs_%s.html' % page, 'wb') as f:
            f.write(s.read())

if __name__ == "__main__":
	get_wikidocs(11)