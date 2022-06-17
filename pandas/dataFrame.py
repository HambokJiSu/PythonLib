#	pip install pandas
import pandas as pd

data = {
	'year':[2016,2017,2018]
	,'GDP rate':[2.8, 3.1, 3.0]
	,'GDP':['1.654M', '1.774M', '2.654M']
	,'ETC':[None, None, 'test']
}

#	DataFrame : 2차원 배열
print("{0:=^25}".format("DataFrame"))
df = pd.DataFrame(data)
print(df)

#	index 추가 가능
print("{0:=^25}".format("DataFrame Index 추가"))
df = pd.DataFrame(data, index=data['year'])
print(df)

#	index 정보 확인
print("{0:=^25}".format("DataFrame Index 정보"))
print(df.index)

#	column 정보 확인
print("{0:=^25}".format("DataFrame column 정보"))
print(df.index)

#	특정 변수 추출
#df = pd.DataFrame(data)
print("{0:=^25}".format("DataFrame 특정변수 추출1"))
print(df['GDP'])
print("{0:=^25}".format("DataFrame 특정변수 추출2"))
print(df[['ETC', 'GDP']])
print("{0:=^25}".format("DataFrame 특정변수 추출3"))
#	df.loc[n:m, [list]]
#	명시적 index가 없을 경우 rowIndex가 기준이 되며 명시적 index가 있을 경우 해당 값을 기준으로 제어 가능
print("{0:=^25}".format("DataFrame loc"))
print(df.loc[:2017, ['year', 'GDP']])
print("{0:=^25}".format("DataFrame 조건 처리"))
print(df[df['ETC'] == 'test'])

print("{0:=^25}".format("DataFrame 합계"))
print(df['GDP rate'].sum())

print("{0:=^25}".format("DataFrame 카운트"))
print(df.count())
print(df["year"].count())
print(df["ETC"].count())	#	카운트 시 None값은 제외처리