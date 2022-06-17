import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.array([4,5,6,7])

s = a + b	#	[5,7,9]		배열의 항목 자체가 늘어나는 Python List와는 다르다
print("{0:=^25}".format("배열 항목간 덧셈"))
print(s)

print("{0:=^25}".format("배열 항목간 뺄셈"))
s = a - b
print(s)

#s = a + c	#	배열 간 개수가 다르면 오류 발생
#print(s)

arr1 = [[1,2],[3,4]]
arr2 = [[5,6],[7,8]]
# arr1 = [1,3]
# arr2 = [5,7]
a = np.array(arr1)
b = np.array(arr2)

c= np.dot(a, b)	#	행열의 곱
print("{0:=^25}".format("행열의 곱"))
print(c)

print("{0:=^25}".format("모든 원소의 합"))
a = np.array([[-1,2,3],[3,4,5]])
s = np.sum(a)	#	모든 원소의 합
print(s)
s = a.sum(axis=0)	#	행별 합
print(s)
s = a.sum(axis=1)	#	열별 합
print(s)

print("{0:=^25}".format("모든 원소의 곱"))
a = np.array([[1,2,3],[3,4,5]])
s = np.prod(a)	#	모든 원소의 곱
print(s)
s = a.prod(axis=0)	#	행별 곱
print(s)
s = a.prod(axis=1)	#	열별 곱
print(s)

print("{0:=^25}".format("모든 원소의 개수"))
s = np.array([[1,2,3],[3,4,5]])
print(s.size)
s = np.array([[1,2,3,4,5]])
print(s.size)

s = np.random.normal(0, 1, 1000)

#	linspace(a:시작 값, b:종료 값, c:분배할 개수)
print("{0:=^25}".format("linspace"))
a = np.linspace(0, 1, 5)
print(a)
a = np.linspace(0, 1, 11)
print(a)

#	r_	배열 요소 더하기 (배열 요소별 덧셈과 다름!)
print("{0:=^25}".format("r_"))
a = np.array([1,2,3])
b = np.array([3,4,5,6])
s = np.r_[a, b]
print(s)
s = np.r_[a, 9, 10, 11, b]
print(s)

#	c_	동일한 인덱스 배열간 요소 더하기 (배열 요소별 덧셈과 다름!)
print("{0:=^25}".format("c_"))
a = np.array([1,2,3,4])
b = np.array([3,4,5,6])
#b = np.array([3,4,5])	#요소의 인덱스 개수가 다르면 오류
s = np.c_[a, b]
print(s)

#	amin / amax	: 모든 배열 요소 중 최소 / 최대값
print("{0:=^25}".format("c_"))
a = np.array([1,2,3,4])
b = np.array([3,4,5,6])
#b = np.array([3,4,5])	#요소의 인덱스 개수가 다르면 오류
print(np.amax(a))
print(np.amax(b))
s = np.r_[a,b]
print(np.amin(s))


#	pip install matplotlib
#	pyplot 차트나 플롯으로 그려주는 라이브러리
import matplotlib.pyplot as plt
plt.hist(s)
plt.show()