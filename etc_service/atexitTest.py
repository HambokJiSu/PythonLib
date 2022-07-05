#	프로그램 종료 시 특정 작업을 실행하려면? ― atexit
import time
import atexit


def handle_exit():
    print("프로그램 종료시 반드시 호출되어야 합니다.")


atexit.register(handle_exit)  # handle_exit() 함수를 프로그램 종료 시 호출하도록 등록
while True:
    print("작업중..")
    time.sleep(1)