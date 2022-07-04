#	디버깅용 로그를 남기려면? ― logging
"""
로그 레벨은 다음과 같이 5단계로 구성된다. 각 단계는 logging.debug(), logging.info(), logging.warning(), logging.error(), logging.critical() 함수로 출력할 수 있다.

1단계 DEBUG: 디버깅 목적으로 사용
2단계 INFO: 일반 정보를 출력할 목적으로 사용
3단계 WARNING: 경고 정보를 출력할 목적으로(작은 문제) 사용
4단계 ERROR: 오류 정보를 출력할 목적으로(큰 문제) 사용
5단계 CRITICAL: 아주 심각한 문제를 출력할 목적으로 사용
"""
from logging.config import dictConfig
import logging

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['file']
    }
})


def myfunc():
    logging.debug("함수가 시작되었습니다.")


myfunc()