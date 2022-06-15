import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.array([4,5,6,7])

s = a + b	#	[5,7,9]		배열의 요소가 더해지는 Python List와는 다르다
print(s)

s = a - b
print(s)

#s = a + c	#	배열의 개수가 다르면 오류 발생
#print(s)