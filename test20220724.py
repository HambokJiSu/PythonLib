"""
participant	completion	return
["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"

동명 이인 있을 수 있음

정렬한 다음 값이 달라지는 첫번째 내용
"""

def solution(participant, completion):
	participant.sort()
	completion.sort()
	completion.append("")

	for i, j in zip(participant, completion):
		# print("i,j:", i, j)
		if i != j:
			return i

rst = solution(["leo", "kiki", "eden"],["eden", "kiki"])
print(rst)