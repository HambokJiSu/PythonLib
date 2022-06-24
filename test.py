id_list = ["muzi", "frodo", "apeach", "neo"]
id_list = ["con", "ryan"]
#	ex) muzi frodo => 유저 muzi가 frodo를 신고했다
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3	#	차단 기준

#print(set(report))

arrReportCnt	= []
arrBanUser 		= []
answer			= []

for i in set(report): 
	arrReportCnt.append(i.split(" ")[1])

#print(arrReportCnt)
for i in id_list: 
	if arrReportCnt.count(i) >= k :
		arrBanUser.append(i)

mailCnt = 0
for i in id_list:
	for j in arrBanUser:
		# print(i + " " + j)
		# print(i + " " + j in set(report))
		if (i + " " + j) in set(report):
			mailCnt = mailCnt + 1

	answer.append(mailCnt)
	mailCnt = 0

print(answer)