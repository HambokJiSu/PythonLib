#	아스키 외의 문자만 인코딩하려면? ― quopri
"""
quoted-printable이란?
quoted-printable 인코딩 방식은 인코딩한 메시지를 디코딩하지 않더라도 ASCII 문자는 그대로 볼 수 있도록 하는 방식이다. 
즉, 영문과 숫자 등의 ASCII 7bit 문자는 그대로 두고 한글 등 8bit 문자만 인코딩한다.
"""
import quopri
str1 = quopri.decodestring('Python Library =EA=B3=B5=EB=B6=80').decode('utf-8')
print(str1)

str2 = quopri.encodestring('Python Library 공부'.encode('utf-8'))
print(str2)