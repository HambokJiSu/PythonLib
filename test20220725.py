"""
124 나라가 있습니다. 124 나라에서는 10진법이 아닌 다음과 같은 자신들만의 규칙으로 수를 표현합니다.

124 나라에는 자연수만 존재합니다.
124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.
예를 들어서 124 나라에서 사용하는 숫자는 다음과 같이 변환됩니다.

10진법	124 나라	3진수
1		1			1
2		2			2
3		4			10
4		11			11
5		12			12
6		14			20
7		21			21
8		22			22
9		24			100
10		41			101
11		42			102
12		44			110
13		111			111

실질적으로 3진법의 숫자이며 
0 => 1
1 => 2
2 => 4
바꾼 형태에 불과함.

단, 0이 포함된 경우 재계산이 필요하다.

3진법을 구현해보자.
"""

def solution(n):
    result = []
    while n > 0:
        t = n % 3
        if t == 0:
            t = 3
            n -= 1
        result.append(str(t))
        n = n // 3
    result = list(map(lambda i: '4' if i == '3' else i, result))
    return ''.join(result[::-1])

print(solution(10))

"""
def change124(n):
    num = ['1','2','4']
    answer = ""


    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer
"""