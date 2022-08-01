from heapq import heappop, heappush

def solution(scoville, K):
	answer = 0

	last1 = 0
	last2 = 0
    
	scoville.sort()

	while scoville[0] < K:
		
		if len(scoville) <= 1:
			return -1
		
		last1 = heappop(scoville)
		last2 = heappop(scoville)
		
		heappush(scoville, last1 + (last2 * 2))
		
		answer += 1
		
	return answer