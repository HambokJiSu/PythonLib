#	C로 만든 라이브러리를 사용하려면? ― ctypes
"""
$ gcc -c mylib.c 
$ gcc -shared mylib.o -o mylib.so
"""
import ctypes
mylib = ctypes.cdll.LoadLibrary('./mylib.so')  # 파이썬 셸을 실행한 위치에 mylib.so가 있어야 함
mylib.add(3, 4)