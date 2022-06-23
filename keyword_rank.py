"""
축사에서 가장 많이 쓰인 단어 TOP 5를 찾아보자
"""
#from matplotlib.pyplot import arrow
import numpy as np
import pandas as pd
import re
from datetime import datetime as dt

def add_char(x):
	return "[" + x + "]"

def strCut(s):
	p = re.compile(".*을$|.*를$|.*은$|.*는$|.*이$|.*가$")	#	단어 끝에 붙은 조사 확인
	return (s[:-1]) if (p.search(s) != None) else (s)

print(dt.now().strftime("%H:%M:%S %f"))
f = open("txt/문재인_퇴임사.txt", encoding="UTF-8")
data = f.read()
#print(data)

arrWord = data.replace("\n", "").replace(",", " ").replace(".", " ").split(" ")
arrWord = np.array(list(map(strCut, arrWord)))
#print(arrWord)

#	use Series
s = pd.Series(arrWord)
s = s.map(add_char)
#print(s)
s = s.value_counts().iloc[1:6]
print(s)

#	use DataFrame
"""
dfWord = pd.DataFrame({
	'word':arrWord
})

dfCount = dfWord.groupby("word").size().reset_index(name="cnt")
dfCount = dfCount.astype({"word":np.str_, "cnt":np.int16})
#print(dfCount)
dfSort = dfCount.sort_values(by="cnt", ascending=False)
print(dfSort.iloc[0:5, :])
"""
print(dt.now().strftime("%H:%M:%S %f"))