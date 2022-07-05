#	바이너리 파일을 텍스트 파일로 바꾸려면? ― uu
"""
uuencode 인코딩은 바이너리를 텍스트로 변환하기 위한 인코딩 방법으로, 1980년 메리 앤 호튼(Mary Ann Horton)이 만들었다. 
uuencode에서 uu는 Unix-to-Unix를 뜻한다. 
즉, 유닉스 시스템 간에 바이너리 데이터를 안전하게 전송하고자 만든 인코딩 방법이다. 
하지만, 지금은 대부분 uuencode의 단점을 보완한 Base64와 같은 MIME 방식의 인코딩을 사용한다.
"""
import uu

# 이미지를 텍스트로 변환
uu.encode(r'recv_data\gmail.jpg', r'recv_data\result.txt')

# 텍스트를 다시 이미지로 변환
uu.decode(r'recv_data\result.txt', r'recv_data\gmail2.jpg')