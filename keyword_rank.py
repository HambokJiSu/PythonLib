"""
축사에서 가장 많이 쓰인 단어 TOP 5를 찾아보자
"""
from matplotlib.pyplot import arrow
import numpy as np
import pandas as pd

f = open("txt/문재인_삼일절_기념축사.txt", encoding="UTF-8")
data = f.read()
#print(data)

arrWord = np.array(data.replace("\n", "").replace(",", " ").replace(".", " ").split(" "))

dfWord = pd.DataFrame({
	'word':arrWord
})

dfCount = dfWord.groupby("word").size().reset_index(name="cnt")
dfCount = dfCount.astype({"word":np.str_, "cnt":np.int16})
#print(dfCount)
dfSort = dfCount.sort_values(by="cnt", ascending=False)
print(dfSort.iloc[0:5, :])