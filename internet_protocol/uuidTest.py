#	고유한 식별자를 만들려면? ― uuid
"""
UUID 버전에는 1, 3, 4, 5 등 총 4가지가 있다. 
이 중 많이 쓰이는 것은 버전 1과 4이다. 
버전 1은 타임스탬프를 기준으로 생성하는 방식이고 버전 4는 랜덤 생성 방식이다. 
버전 3과 5는 각각 MD5, SHA-1 해시를 이용해 생성하는 방식이다.
"""
import uuid

a = uuid.uuid1()
print(a)
print(a.bytes)
print(a.hex)
print(a.int)
print(a.version)
print("-"*10)
b = uuid.uuid4()
print(b)
print(b.bytes)
print(b.hex)
print(b.int)
print(b.version)