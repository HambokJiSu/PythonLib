#	최대 공약수 구하기
import math
math.gcd(60, 100, 80)

#	최소 공배수 구하기
import math
math.lcm(15, 25)

#	2진수 연산 기반의 파이썬에서 아래 식들은 True이지만 False를 반환
print("===실수 연산===")
print(0.1 * 3 == 0.3)
print(1.2 - 0.1 == 1.1)
print(0.1 * 0.1 == 0.01)

#	정확한 비교를 위해 Decimal 활용 가능. 단, Decimal함수 파라미터는 문자열 이어야 함
#	단, 메모리 사용이 많으니 재무/회계 프로그램에서 사용하자.
from decimal import Decimal
print("===실수 연산 (with Decimal)===")
print(Decimal("0.1") * Decimal("3") == Decimal("0.3"))
print(Decimal("1.2") - Decimal("0.1") == Decimal("1.1"))
print(Decimal("0.1") * Decimal("0.1") == Decimal("0.01"))

#	분수계산
print("===분수 연산===")
#	아래 식에서 원하는 3/5를 얻어내려면?
print(1/5 + 2/5)
from fractions import Fraction
result = Fraction("1/5") + Fraction("2/5")
print(result)			# Fraction 타입
print(float(result))	# float 변환
print(result.numerator)		# Fraction 분자 추출
print(result.denominator)	# Fraction 분모 추출

#	로또 번호 뽑기
print("===로또===")
import random

result = []
while len(result) < 6:
    num = random.randint(1, 45)  # 1~45 사이의 숫자중 임의의 숫자 생성
    if num not in result:  # 중복 숫자 뽑기 방지
        result.append(num)

print(result)  # 무작위 생성된 6개의 숫자 출력


#	평균값과 중앙값 알기
print("===평균값과 중앙값===")
import statistics
marks = [78, 93, 99, 95, 51, 71, 52, 43, 81, 78]
print(statistics.mean(marks))	#	평균값
print(statistics.median(marks))	#	중앙값