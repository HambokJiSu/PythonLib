import textwrap

#	제목 및 내용 미리보기 글자가 많을 때 끊기 (기본값)
txt1 = textwrap.shorten("Life is too short, you need python", width=15)
print(txt1)

#	제목 및 내용 미리보기 글자가 많을 때 끊기 (줄임 기호 직접입력)
txt1 = textwrap.shorten("Life is too short, you need python", width=15, placeholder="...")
print(txt1)