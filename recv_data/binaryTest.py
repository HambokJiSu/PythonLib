#	바이너리 데이터를 문자열로 바꾸려면? ― base64
#	base64는 바이너리 데이터를 문자열로 인코딩할 때 사용하는 모듈이다. 이때 인코딩한 문자열은 64개의 아스키 문자로 구성된다(64진법 사용).
"""
A 씨는 test.jpg라는 이미지 파일을 텍스트로 첨부하여 B 씨에게 전송하려 한다. 
그러려면 이미지 파일을 Base64 형식으로 인코딩한 문자열로 바꾸는 img_to_string() 함수가 필요하다. 
이와 함께 데이터를 수신한 B 씨는 Base64로 인코딩한 문자열을 원래 이미지로 바꾸는 string_to_img() 함수가 필요하다.
A 씨와 B 씨가 이미지를 문자열 형식으로 주고받는 데 필요한 다음과 같은 형식의 img_to_string() 함수와 string_to_img() 함수를 만들려면 어떻게 해야 할까?
"""
import base64

def img_to_string(filename):
    ''' 파일명(filename)을 입력으로 받아 base64로 인코딩한 문자열을 리턴한다 '''
    with open(filename, 'rb') as f:
        return base64.b64encode(f.read())

def string_to_img(s, filename):
    ''' base64로 인코딩된 문자열(s)과 파일명(filename)을 입력으로 받아 문자열을 파일로 저장한다. '''
    with open(filename, 'wb') as f:
        f.write(base64.b64decode(s))

img_string = img_to_string(r'recv_data\gmail.jpg')  	# gmail.jpg 파일을 base64 문자열로 반환
string_to_img(img_string, r'recv_data\result.jpg')  	# base64 문자열을 result.jpg 파일로 저장