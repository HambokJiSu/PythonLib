import numpy as np

print("{0:=^25}".format("반복문 없이 전체 내용에 반영"))
a = np.array([1,2,3,4])
b = np.array([2,3,4,5])
print(a + 3)	#	스칼라 연산 확장 적용
print(a + b)	#	ndarray간 연산

a = np.array([1,2,3,4])
b = np.array([1,2,3])
#s = a + b #오류 발생

print("{0:=^25}".format("BroadCast 가능 조건"))
print("{0:=^25}".format("1) 배열의 마지막 축 사이즈가 동일 (추가적인 Case Study 요망)"))
a = np.array([[1, 2],[3, 4]])
b = np.array([[1,1,1,1], [2,2,2,2]])
print(a.shape)	#	(2, 2)
print(b.shape)	#	(2, 4)
#print(a + b)

print("{0:=^25}".format("2) 어느 한축의 길이가 1이면 BroadCast 가능"))
a = np.array([[1],[3],[5],[7]])
b = np.array([[1,1,1,1], [2,2,2,2], [3,3,3,3], [4,4,4,4]])
print(a.shape)	#	(4,)	실제 (1, 4)
print(b.shape)	#	(4, 4)
print(a + b)

print("{0:=^25}".format("최고 / 최저값 BroadCast 연산 활용"))
arrMax = np.array([200, 300, 400, 500, 600])
arrMin = np.array([101, 201, 150, 250, 101])

totAvg =  (arrMax - arrMin).sum() / len(arrMax - arrMin)
print(totAvg)