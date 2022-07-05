#	pip install Faker

#	테스트용 데이터를 생성하려면? ― faker
from faker import Faker
fake = Faker()
n = fake.name()
a = fake.address()
print(n)
print(a)
print("-"*30)
fake = Faker('ko-KR')
n = fake.name()
a = fake.address()
print(n)
print(a)
print("-"*30)
test_data = [(fake.name(), fake.address()) for i in range(30)]
print(test_data)
"""
fake.name()	이름
fake.address()	주소
fake.postcode()	우편 번호
fake.country()	국가명
fake.company()	회사명
fake.job()	직업명
fake.phone_number()	휴대 전화 번호
fake.email()	이메일 주소
fake.user_name()	사용자명
fake.pyint(min_value=0, max_value=100)	0부터 100 사이의 임의의 숫자
fake.ipv4_private()	IP 주소
fake.text()	임의의 문장 (※ 한글 임의의 문장은 fake.catch_phrase() 사용)
fake.color_name()	색상명
"""