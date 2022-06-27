#	딕셔너리 데이터를 한 눈에 보기 좋게 출력
import pprint

result = {'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
print(result)
pprint.pprint(result)

#	점수에 따른 학점을 구하려면? 	― bisect
#	숫자에 이름을 붙여 사용하려면	― enum
#	수강할 과목의 순서를 구하려면 	― graphlib.TopologicalSorter