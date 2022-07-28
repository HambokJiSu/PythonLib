# from time import time

# list1 = [1, 3, 5, 6, 7, 9, 11, 13, 15, 17]
# start = time()
# for i in range(999999):
#     list1.reverse()
# print(list1)
# end = time()
# print('time elapsed:', end - start)

# list2 = [1, 3, 5, 6, 7, 9, 11, 13, 15, 17]
# list3 = []
# start = time()
# for i in range(999999):
#     list2[::-1]
# print(list2[::-1])
# end = time()
# print('time elapsed:', end - start)

list1 = ["1", "3", "5", "6", "7", "9"]
print("".join(list1))
print("-".join(list1))  #   공백 이외의 문자 입력 시 리스트 사이에 해당 문자 출력

list2 = [1, 3, 5, 6, 7, 9]
#   리스트 내용이 문자열이 아니면 오류 발생!!!!
#   map 활용하여 문자열로 변환 후 처리하자
list2 = list(map(lambda i:str(i), list2))
print("".join(list2))