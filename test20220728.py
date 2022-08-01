"""
answers		return
[1,2,3,4,5]	[1]
[1,3,2,4,2]	[1,2,3]
"""

import math

def solution(answers):
	answer = []
    
	ans1 = [1, 2, 3, 4, 5]
	ans2 = [2, 1, 2, 3, 2, 4, 2, 5]
	ans3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    #   정답 배열의 수에 맞게 배열 길이를 증가처리
	ans1 = ans1 * math.ceil(len(answers) / len(ans1))
	ans2 = ans2 * math.ceil(len(answers) / len(ans2))
	ans3 = ans3 * math.ceil(len(answers) / len(ans3))

	print(ans1)
	print(ans2)
	print(ans3)
	print("="*30)

	rst = [0, 0, 0]
	
	for i, j in zip(ans1, answers):
		if i == j:rst[0]+=1
	
	for i, j in zip(ans2, answers):
		if i == j:rst[1]+=1

	for i, j in zip(ans3, answers):
		if i == j:rst[2]+=1

	maxRst = max(rst)
	for i in range(len(rst)):
		if rst[i] == maxRst:answer.append(i + 1)
	
	return answer

# r = solution([1,2,3,4,5])
# r = solution([1,3,2,4,2])
r = solution([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
print(r)