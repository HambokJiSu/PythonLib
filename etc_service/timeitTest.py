#	함수의 실행 시간을 비교하려면? ― timeit
import functools
import time


def elapsed(original_func):
    @functools.wraps(original_func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs)
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))
        return result

    return wrapper


@elapsed
def a():
    result = []
    for i in range(10000):
        result.append(i)
    return result


@elapsed
def b():
    return [i for i in range(10000)]


if __name__ == '__main__':
	#	단건 테스트
	a()
	b()

	#	반복 테스트
	import timeit
	print(timeit.timeit("a()", number=100, globals=globals()))
	print(timeit.timeit("b()", number=100, globals=globals()))