import json

#	json 데이터 읽기
with open("recv_data\json_sample.json", encoding="UTF-8") as f:
	data = json.load(f)

print(data)

#	json 데이터 쓰기
data = {'name':'홍길동', 'birth':'0505', 'age':30}
with open("recv_data\json_write.json", mode="w", encoding="UTF-8") as f:
	json.dump(data, f)