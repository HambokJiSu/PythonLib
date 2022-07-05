#	문장을 분석하려면? ― shlex
"""
다음과 같은 문자열이 있다고 하자. 여기에는 "a test"와 같이 큰따옴표로 강조한 부분이 있다.

this is "a test"
이 문장을 단순히 공백을 기준으로 나누면(split()) 다음과 같은 결과가 나온다.

a = 'this is "a test"'
a.split()
['this', 'is', '"a', 'test"']
>>>
하지만, 이는 원하는 결과가 아니다. 큰따옴표로 묶은 부분을 하나로 취급하여 다음과 같은 결과가 나오기를 바란다.

['this', 'is', 'a test']
또는 큰따옴표를 포함하여 다음과 같은 결과가 나왔으면 한다.

['this', 'is', '"a test"']
큰따옴표 부분을 한 묶음으로 다루어 문장 요소를 나누는 프로그램은 어떻게 만들어야 할까?
"""
import shlex
r = shlex.split('this is "a test"')
print(r)

r2 = shlex.split('this is "a test"', posix=False)	#	큰따옴표 포함
print(r2)