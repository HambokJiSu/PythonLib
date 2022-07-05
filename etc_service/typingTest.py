#	데이터의 타입을 확인하려면? ― typing
from typing import List

def sum_list(numbers: List[int]) -> int:
    return sum(n for n in numbers)

def sum_list_normal(numbers) -> int:
    return sum(n for n in numbers)

result2 = sum_list_normal([1, 2, '3', 4])
print(result2)

result = sum_list([1, 2, '3', 4])
print(result)


#	재할당할 수 없는 변수에는 Final을 사용한다.
from typing import Final
PORT: Final[int] = 8080