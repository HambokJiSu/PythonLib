#	명령행 옵션을 지정하여 실행하려면? ― argparse
"""
-a 또는 --add 옵션을 지정했을 때는 뒤에 오는 모든 정수의 합을 출력한다.

c:\projects\pylib>python add_mul.py -a 1 2 3 4 5
합은 15입니다.
c:\projects\pylib>python add_mul.py --add 1 2 3 4 5
합은 15입니다.

-m 또는 --mul 옵션을 지정했을 때는 뒤에 오는 모든 정수의 곱을 출력한다.

c:\projects\pylib>python add_mul.py -m 1 2 3 4 5
곱은 120입니다.
c:\projects\pylib>python add_mul.py --mul 1 2 3 4 5
곱은 120입니다.

다음처럼 두 개의 옵션 -a, -m을 함께 사용할 수도 있어야 한다.

c:\projects\pylib>python add_mul.py -a 1 2 3 4 5 -m 1 2 3 4 5
합은 15입니다.
곱은 120입니다.
"""
import argparse
import functools

parser = argparse.ArgumentParser()
#	nargs
# 		*, +: 적어도 1개 이상의 명령행 매개변수가 필요하다. +라면 매개변수가 하나도 없으면 오류가 발생한다.
#	metavar
#		N: N개의 명령행 매개변수가 필요하다. nargs=2와 같이 사용하면 정확히 2개의 명령행 매개변수를 입력해야 한다.
#		?: 1개의 명령행 매개변수 또는 생략할 수 있다. 생략하면 default 매개변수에 설정한 값을 사용한다.
parser.add_argument('-a', '--add', type=int, nargs='+', metavar='N', help='더할 숫자')
parser.add_argument('-m', '--mul', type=int, nargs='+', metavar='N', help='곱할 숫자')

args = parser.parse_args()

if args.add:
    print("합은 %d입니다." % functools.reduce(lambda x, y: x + y, args.add))
if args.mul:
    print("곱은 %d입니다." % functools.reduce(lambda x, y: x * y, args.mul))