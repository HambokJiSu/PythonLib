#	사용자가 보낸 신호를 처리하려면? ― signal
import time
import signal


def handler(signum, frame):
    print("Ctrl+C 신호를 수신했습니다.")


signal.signal(signal.SIGINT, handler)

while True:
    print('대기중...')
    time.sleep(10)