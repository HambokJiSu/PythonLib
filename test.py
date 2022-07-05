id_list = ["muzi", "frodo", "apeach", "neo"]
#id_list = ["con", "ryan"]
#	ex) muzi frodo => 유저 muzi가 frodo를 신고했다
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
#report = ["ryan con", "ryan con", "ryan con", "ryan con"]

k = 2	#	차단 기준
#k = 3	#	차단 기준

#print(set(report))

arrUniReport	= list(set(report))
arrReportCnt	= []
arrBanUser 		= []
answer			= []

arrReportCnt 	= list(map(lambda i: i.split(" ")[1], arrUniReport))
arrBanUser		= list(filter(lambda i: arrReportCnt.count(i) >= k, id_list))

arrReportUser	= list(filter(lambda i: i.split(" ")[1] in arrBanUser, arrUniReport))
arrReportUser	= list(map(lambda i: i.split(" ")[0], arrReportUser))

#print(arrReportUser)
#	Ban 사용자는 확보, 신고한 사용자의 메일 카운팅 이슈

for i in id_list:
	answer.append(arrReportUser.count(i))

print(answer)