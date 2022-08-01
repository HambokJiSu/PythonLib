"""
n		전체 학생수
lost	잃어버린 학생 배열
reserve	여벌옷이 있는 학생 배열

잃어버린 학생에겐 바로 앞 혹은 바로 뒤 번호의 체육복만 빌려 줄 수 있음

여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 
이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

체육복을 입고 수업을 들을 수 있는 학생의 수 리턴

n	lost	reserve		return
5	[2, 4]	[1, 3, 5]	5
5	[2, 4]	[3]			4
3	[3]		[1]			2
3	[3]		[3]			3
"""

def solution(n, lost, reserve):
	answer = 0

	arrSt = range(1, n + 1)

	#	reserve 배열에 있지만 lost에 포함되는 경우 resver 배열에서 제거처리
	for i in arrSt:
		if reserve.count(i) > 0 and lost.count(i) > 0:
			reserve.remove(i)
			lost.remove(i)

	for i in arrSt:
		if lost.count(i) == 0:
			answer+=1
		else:
			if reserve.count(i - 1):
				reserve.remove(i - 1)
				answer+=1
			elif reserve.count(i + 1):
				reserve.remove(i + 1)
				answer+=1

	return answer

rst = solution(30
				, [1, 2, 				7, 		9, 10, 11, 12, 		14, 15, 16, 	18, 20, 21, 		24, 25, 	27]
				, [1, 2, 3, 4, 5, 6, 	7, 8, 	9, 10, 11, 12, 13, 	14, 15, 16, 17, 	20, 	22, 23, 24, 25, 26, 27, 28])
print(rst)