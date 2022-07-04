#	멀티 프로세스를 이용하여 병렬로 처리하려면? ― multiprocessing
#	_bMultiProcessing True 수행시 오류 발생 원인은?
import time

_bMultiProcessing = True

def heavy_work(name):
    result = 0
    for i in range(4000000):
        result += i
    print('%s done' % name)


if __name__ == "__main__":

	import multiprocessing

	start = time.time()
	procs = []
	for i in range(4):
		if _bMultiProcessing == True:
			p = multiprocessing.Process(target=heavy_work, args=(i,))
			p.start()
			procs.append(p)
		else:
			heavy_work(i)

	if _bMultiProcessing == True:
		for p in procs:
			p.join()	#	프로세스가 모두 종료될 때까지 대기

	end = time.time()

	print("수행시간: %f 초" % (end - start))