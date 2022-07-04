#	병렬로 작업을 처리하려면? ― concurrent.futures
"""
여러 프로세스가 동시에 heavy_work() 함수를 호출하는 코드이다. 
현재 heavy_work() 함수는 result를 계산만 하고 그 값을 반환하지는 않는다. 
계산한 result를 반환하도록 heavy_work() 함수를 수정하고 
호출한 heavy_work() 함수의 반환값을 모두 더해 출력하도록 메인 프로세스를 수정하려면 어떻게 해야 할까?

p.result() 구문에서 BrokenProcessPool 오류 발생
원인 확인 요망
"""
import time


def heavy_work(name):
    result = 0
    for i in range(4000000):
        result += i
    print('%s done' % name)
    return result  # 결과를 반환하도록 변경

if __name__ == '__main__':
    import concurrent.futures

    start = time.time()

    total_result = 0
    pool = concurrent.futures.ProcessPoolExecutor(max_workers=4)

    procs = []
    for i in range(4):
        procs.append(pool.submit(heavy_work, i))

    for p in concurrent.futures.as_completed(procs):
        total_result += p.result()

    end = time.time()

    print("수행시간: %f 초" % (end - start))
    print("총결괏값: %s" % total_result)