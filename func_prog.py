#	상담원을 순서대로 배정하려면? ― itertools.cycle
print("###itertools.cycle###")
import itertools
emp_pool = itertools.cycle(['김은경', '이명자', '이성진'])
print(next(emp_pool))
print(next(emp_pool))
print(next(emp_pool))
print(next(emp_pool))
print(next(emp_pool))

#	누적합계 -- itertools.accumulate
print("###itertools.accumulate###")
import itertools

monthly_income = [1161, 1814, 1270, 2256, 1413, 1842, 2221, 2207, 2450, 2823, 2540, 2134]
result = list(itertools.accumulate(monthly_income))

print(result)

#	키 값으로 데이터 묶기 -- itertools.groupby
print("###itertools.groupby###")
import itertools
import operator
import pprint

data = [
    {'name': '이민서', 'blood': 'O'},
    {'name': '이영순', 'blood': 'B'},
    {'name': '이상호', 'blood': 'AB'},
    {'name': '김지민', 'blood': 'B'},
    {'name': '최상현', 'blood': 'AB'},
    {'name': '김지아', 'blood': 'A'},
    {'name': '손우진', 'blood': 'A'},
    {'name': '박은주', 'blood': 'A'}
]

data = sorted(data, key=operator.itemgetter('blood'))  # groupby 전 분류 기준으로 정렬
grouped_data = itertools.groupby(data, key=operator.itemgetter('blood'))

result = {}
for key, group_data in grouped_data:
    result[key] = list(group_data)  # group_data는 이터레이터이므로 리스트로 변경

pprint.pprint(result)


#	부족한 것을 채워 묶으려면? ― itertools.zip_longest
print("###itertools.zip_longest###")
import itertools

students = ['한민서', '황지민', '이영철', '이광수', '김승민']
rewards = ['사탕', '초컬릿', '젤리']

result = itertools.zip_longest(students, rewards, fillvalue='새우깡')
print(list(result))

#	랜덤한 숫자 꺼내기 ― itertools.permutations (순서 포함) itertools.combinations (순서 무관)
print("###itertools.permutations###")
#	1, 2, 3 숫자가 적힌 3장의 카드에서 두 장의 카드를 꺼내 만들 수 있는 2자리 숫자를 모두 구하기 (순서 포함)
import itertools
list1 = list(itertools.permutations(['1', '2', '3'], 2))
print(list1)
list2 = list(itertools.combinations(['1', '2', '3'], 2))
print(list2)

#	itertools.combinations 활용, 로또 경우의 수 구하기
list3 = list(itertools.combinations(range(1, 46), 6))
print(len(list3))

#	순서대로 좌표를 정렬 ― functools.cmp_to_key
print("###functools.cmp_to_key###")
"""
다음과 같이 2차원 평면 위의 점 N개를 (x, y) 좌표로 구성한 리스트가 있다. 
y 좌표가 증가하는 순으로 정렬하되 y 좌표가 같으면 x 좌표가 증가하는 순으로 좌표를 정렬하고 이를 출력하는 프로그램을 만들려면 어떻게 해야 할까
"""
import functools

def xy_compare(n1, n2):
    if n1[1] > n2[1]:         # y 좌표가 크면
        return 1
    elif n1[1] == n2[1]:      # y 좌표가 같으면
        if n1[0] > n2[0]:     # x 좌표가 크면
            return 1
        elif n1[0] == n2[0]:  # x 좌표가 같으면
            return 0
        else:                 # x 좌표가 작으면
            return -1
    else:                     # y 좌표가 작으면
        return -1

src = [(0, 4), (1, 2), (1, -1), (2, 2), (3, 3)]
result = sorted(src, key=functools.cmp_to_key(xy_compare))
print(result)

print("###functools.lru_cache###")
import urllib.request
from functools import lru_cache

@lru_cache(maxsize=32)	#	요놈이 캐싱 처리 여부를 판단
def get_wikidocs(page):
    print("wikidocs page:{}".format(page))  # 페이지 호출시 출력
    resource = 'https://wikidocs.net/{}'.format(page)
    try:
        with urllib.request.urlopen(resource) as s:
            return s.read()
    except urllib.error.HTTPError:
        return 'Not Found'

first_6 = get_wikidocs(6)
first_7 = get_wikidocs(7)

second_6 = get_wikidocs(6)
second_7 = get_wikidocs(7)

assert first_6 == second_6  # 처음 요청한 6페이지와 두 번째 요청한 6페이지의 내용이 같은지 확인
assert first_7 == second_7

#기존 함수로 새로운 함수를 만들려면? ― functools.partial

# 레퍼 함수 -- elapsed, original_func
# 래퍼 함수란 실제 함수(original function)를 감싼 함수(wrapper function)로, 
# 실제 함수 호출 시 특별한 동작을 하도록 기능을 덧붙인 함수를 말한다. 데코레이터를 만들 때 주로 사용한다

import functools
import time

def elapsed(original_func):
    @functools.wraps(original_func)  # 여기에 추가!!
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs)
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))
        return result

    return wrapper


@elapsed
def add(a, b):
    """ 함수 설명문 Print """
    return a + b

#print(add)  # 함수 이름 출력
help(add)  # 함수 독스트링 출력

#	다양한 기준으로 정렬하려면 ― operator.itemgetter
from operator import itemgetter

students = [
    ("jane", 22, 'A'),
    ("dave", 32, 'B'),
    ("sally", 17, 'B'),
]

result = sorted(students, key=itemgetter(0))
print(result)