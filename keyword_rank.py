"""
축사에서 가장 많이 쓰인 단어 TOP 5를 찾아보자
"""
#from matplotlib.pyplot import arrow
import numpy as np
import pandas as pd
from datetime import datetime as dt

print(dt.now().strftime("%H:%M:%S %f"))
f = open("txt/문재인_퇴임사.txt", encoding="UTF-8")
data = f.read()
#print(data)

arrWord = np.array(data.replace("\n", "").replace(",", " ").replace(".", " ").split(" "))

def add_char(x):
	return "[" + x + "]"

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