import pandas as pd
import numpy as np

"""
시리즈
"""
print("{0:=^25}".format("list to Series"))
data = [10, 20, 30]
s = pd.Series(data)
print(s)

print("{0:=^25}".format("ndarray to Series"))
data = np.arange(10, 31, 10)
s = pd.Series(data)
print(s)

print("{0:=^25}".format("string to Series"))
data = ["시가", "고가"]
s = pd.Series(data)
print(s)	#	dtype이 object로 표기되는 경우 브로드캐스팅 기능을 이용한 수치 연산 사용 불가

"""
시리즈 인덱스
인덱스를 따로 설정하지 않아도 0부터 시작하는 숫자값을 RangeIndex 타입으로 자동 생성
"""
print("{0:=^25}".format("confirm index"))
data = [10, 20, 30]
s = pd.Series(data)
print(s.index)

print("{0:=^25}".format("explicit index"))
data = [10, 20, 30]
s = pd.Series(data)
s.index = ["와", "비비빅", "옥동자"]	# 시리즈 생성 후 인덱스를 명시적으로 적용
print(s)
print("")
data = [10, 20, 30]
idx = ["와", "비비빅", "옥동자"]		# 시리즈 생성 시 인덱스를 명시적으로 적용
s = pd.Series(data, idx)
print(s)

"""
시리즈 인덱싱
iloc : 행번호 인덱스 사용
loc : 인덱스 사용
"""
print("{0:=^25}".format("iloc / loc"))
data = [10, 20, 30]
s = pd.Series(data)
print(s.iloc[0])
print(s.iloc[1])
print(s.iloc[2])
print(s.iloc[-1])