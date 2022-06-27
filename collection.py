#	dequeue 자료형
#	양방향 자료형, 스택처럼 써도 되고 큐처럼 써도 된다.
#	리스트의 연산과 비슷한 부분이 있지만 O(N) 연산을 수행하는 리스트 대비 O(1) 연산을 수행하기 때문에 속도가 더 빠르다
#	O(1) : 입력의 크기와 상관 없이 항상 같은 시간이 걸리는 알고리즘
#	O(N) : 한 번의 반복을 수행하고 완료되는 선형 탐사가 O(N)의 시간 복잡도를 가짐

from collections import deque
a = [1, 2, 3, 4, 5]
q = deque(a)
q.rotate(2)  #시계방향 회전은 양수, 그 반대는 음수
result = list(q)
print(result)	#	[4, 5, 1, 2, 3]

#	자료에 이름을 붙이려면?
#	collections.namedtuple