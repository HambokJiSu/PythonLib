import heapq

data = [
    (12.23, "강보람"),
    (12.31, "김지원"),
    (11.98, "박시우"),
    (11.99, "장준혁"),
    (11.67, "차정웅"),
    (12.02, "박중수"),
    (11.57, "차동현"),
    (12.04, "고미숙"),
    (11.92, "한시우"),
    (12.22, "이민석"),
]

#	힙 활용1 Start
# h = []  # 힙 생성
# for score in data:
#     heapq.heappush(h, score)  # 힙에 데이터 저장

# for i in range(3):
#     print(heapq.heappop(h))  # 최솟값부터 힙 반환
#	힙 활용1 End

#	힙 활용2 Start
# heapq.heapify(data)  # data를 힙 구조에 맞게 변경.

# for i in range(3):
#     print(heapq.heappop(data))  # 최솟값부터 힙 반환
#	힙 활용2 End

#	힙 활용3 Start
#h = heapq.nsmallest(3, data)	#	값이 가장 적은 요소를 우선
h = heapq.nlargest(3, data)		#	값이 가장 큰 요소를 우선 : neapq.nlargest
print(h)
#	힙 활용3 End