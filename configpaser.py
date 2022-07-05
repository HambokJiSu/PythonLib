import configparser

#	특수문자가 포함된 값도 정상적으로 호출하기 위해서는 ConfigParser가 아닌 RawConfigParser를 활용해야함
config = configparser.RawConfigParser()
config.read("ftp.ini", encoding="UTF-8")

ftp1_port = config.get("FTP1", "PORT")
print(ftp1_port)