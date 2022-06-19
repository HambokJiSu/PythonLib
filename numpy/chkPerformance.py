import numpy as np
from datetime import datetime as dt

print(dt.now().strftime("%H:%M:%S %f"))
a = np.arange(1000000).reshape(1000, 1000)
print(dt.now().strftime("%H:%M:%S %f"))

print("{0:=^25}".format("Indexing Performance"))
arr = np.arange(4).reshape(2,2)
print(arr)
print(arr[0][1])    #   동일한 인덱스, [행][열] 두 번의 인덱싱이 적용된 상태
print(arr[0, 1])    #   동일한 인덱스, [행,열] 한 번의 인덱싱이 적용된 상태 (약 49% 나은 성능)


print("{0:=^25}".format("List Slice vs Numpy Slice"))
print("{0:=^25}".format("Slice first index By row"))
arrList = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]
resultList = []
for row in arrList:
    resultList.append([row[0]])
print(resultList)

arrNp = np.arange(10).reshape(5, 2)
print(arrNp[:, :1])

print("{0:=^25}".format("Slice ex"))
arr = np.arange(20).reshape(4, 5)
print(arr[1:, 2:])