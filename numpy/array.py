#	numpy	C기반으로 빠른 속도가 장점
import numpy as np

a = np.array(0)
print(a)
print(type(a))

a = np.array([1,2,3])
print(a)
print(type(a))	#	<class 'numpy.ndarray'>와 같이 상세하게 나오지 않음

a = np.array([[1,2,3], [4,5,6], ["가능?", "진짜?", "레알?"]])
print(a)
print(a.dtype)	#	<U11

a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(a)
print(a.dtype)	#	int32
a = a.astype(np.float32)	#	형변환
print(a.dtype)	#	float32

a = np.arange(1, 10)	# 1부터 10미만
print(a)
a = np.arange(1, 10, 2)	# 1부터 10미만 2간격
print(a)
#	reshape : 차원 전환
a = np.arange(1, 10).reshape(3, 3)		# 1부터 10미만 3행 3열 2차원 배열
print(a)
a = np.arange(1, 21).reshape(4, 5)		# 1부터 21미만 4행 5열 2차원 배열
print(a)
a = np.arange(1, 13).reshape(3, 2, 2)	# 1부터 12미만 3*2*2 3차원 배열
print(a)

#	슬라이싱 / 인덱싱
a = np.arange(1, 10).reshape(3, 3)		# 1부터 10미만 3행 3열 2차원 배열
arr = np.array(a)
a = arr[0:2, 0:2]	# [[1 2][4 5]]	0:2 0부터 2인덱스까지
print(a)
a = arr[1:, 1:]		#	1인덱스부터 끝까지
print(a)