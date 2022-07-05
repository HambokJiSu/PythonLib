#	문자열을 16진수로 변환하려면? ― binascii
"""
다음은 어떤 문자열을 16진수로 표현한 것이다.
507974686f6e204c696272617279
이 문자열의 원래 값을 구하려면 어떻게 해야 할까?
"""
import binascii
str1 = binascii.unhexlify(b'507974686f6e204c696272617279')
print(str1)

#	한글 문자열이 포함된 경우 encode 필요
result1 = binascii.hexlify('Python 라이브러리'.encode('utf-8'))
print(result1)
result2 = binascii.unhexlify(result1).decode('utf-8')
print(result2)