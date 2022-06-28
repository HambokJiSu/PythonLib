#	데이터 크기를 줄여 전송하려면? ― zlib
import zlib


data = "Life is too short, You need python." * 10000
compress_data = zlib.compress(data.encode(encoding='utf-8'))	# 압축
print(len(compress_data))  # 1077 출력
print(compress_data)

org_data = zlib.decompress(compress_data).decode('utf-8')		# 복구
print(len(org_data))  # 350000 출력
print(org_data)

#	데이터 압축 저장, 해제 호출

#	use gzip
import gzip
import bz2
import lzma

data = "Life is too short, you need python." * 10000

with gzip.open('data.txt.gz', 'wb') as f:	#	gzip
# with bz2.open('data.txt.bz2', 'wb') as f:	#	bz2
    f.write(data.encode('utf-8'))  # 저장한 파일의 크기는 1097바이트

with gzip.open('data.txt.gz', 'rb') as f:	#	gzip
#with bz2.open('data.txt.gz', 'rb') as f:	#	bz2
    read_data = f.read().decode('utf-8')

assert data == read_data

#	use lzma
compress_data = lzma.compress(data.encode(encoding='utf-8'))
print(len(compress_data))  # 220 출력

org_data = lzma.decompress(compress_data).decode('utf-8')
print(len(org_data))  # 350000 출력

#	여러파일 tar로 합치기	--	tarfile
import tarfile

# 여러파일 합치기
with tarfile.open('mytext.tar', 'w') as mytar:
    mytar.add('a.txt')
    mytar.add('b.txt')
    mytar.add('c.txt')

# 여러파일 해제하기
with tarfile.open('mytext.tar') as mytar:
    mytar.extractall()