import numpy as np

#	단건
print("{0:=^25}".format("단건"))
print(np.random.rand())

#	배열 형태
print("{0:=^25}".format("배열 1차원"))
print(np.random.rand(3))
print("{0:=^25}".format("배열 2차원"))
print(np.random.rand(2,3))

#	음수, 양수 모두
print("{0:=^25}".format("음수/양수 모두"))
print(np.random.randn())

#	배열 형태
print("{0:=^25}".format("배열 1차원"))
print(np.random.randn(3))
print("{0:=^25}".format("배열 2차원"))
print(np.random.randn(2,3))

#	randint 정수형
#	random.randint(low, high=None, size=None, dtype=int)
#	범위 지정
print("{0:=^25}".format("정수형"))
print(np.random.randint(90, 100))

#	uniform 2개의 숫자 사이의 실수를 리턴
x = range(1000)
y = np.random.uniform(5, 9, size=1000)

import matplotlib.pyplot as plt
plt.scatter(x, y, s=1, c='k')
plt.show()