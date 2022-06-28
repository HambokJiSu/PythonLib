"""
주어진 로또 번호 기준으로 최고 순위 및 최저 순위를 반환하라.
단, 배열 파라미터 0은 알 수 없는 번호로 인지한다.

lottos		6개 내 번호
win_nums	6개 1등 번호

1등			6개 번호 모두 일치
2등			5개 번호 일치
3등			4개 번호 일치
4등			3개 번호 일치
5등			2개 번호 일치
6등			1개 이하 번호
"""

def solution(lottos, win_nums):
	equalCnt = 0	#	일치 횟수
	for i in lottos:
		if i == 0:continue

		if i in win_nums:
			win_nums.remove(i)
			equalCnt+=1

	bottomRank = 6 if 7 - equalCnt == 7 else 7 - equalCnt	#	최저 순위
	equalCnt+=lottos.count(0)
	topRank = 6 if 7 - equalCnt == 7 else 7 - equalCnt		#	최고 순위

	answer = []
	answer.append(topRank)
	answer.append(bottomRank)
	
	return answer

list1 = solution([44,1,0,0,31,25], [31, 10, 45, 1, 6, 19])
# list1 = solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])
# list1 = solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])
print(list1)