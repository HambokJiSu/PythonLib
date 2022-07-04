#	스레드를 이용하여 병렬로 처리하려면? ― threading
import urllib.request

_bThreading = True

def get_wikidocs(page):
    print("wikidocs page:{}".format(page))  # 페이지 호출시 출력
    resource = 'https://wikidocs.net/{}'.format(page)
    try:
        with urllib.request.urlopen(resource) as s:
            with open('wikidocs_%s.html' % page, 'wb') as f:
                f.write(s.read())
    except urllib.error.HTTPError:
        return 'Not Found'

if __name__ == "__main__":
	import time
	import threading

	start = time.time()

	pages = [12, 13, 14, 15, 17, 18, 20, 21, 22, 24]
	threads = []
	for page in pages:
		if _bThreading == True:
			t = threading.Thread(target=get_wikidocs, args=(page, ))
			t.start()
			threads.append(t)
		else:
			get_wikidocs(page)

	if _bThreading == True:
		for t in threads:
			t.join()  # 스레드가 종료될 때까지 대기

	end = time.time()

	print("수행시간: %f 초" % (end - start))