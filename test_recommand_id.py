import re

def solution(new_id):
    #  1단계 : 모든 대문자는 소문자로 치환
    answer = new_id.lower()

    #  2단계 : 허용 문자 (소문자, -, _, .)
    p2 = re.compile("[^a-z0-9-_.]")
    answer = p2.sub("", answer)

    #  3단계 : 2회 이상 연속된 마침표는 1회 마침표로 치환
    p3 = re.compile("[.]{2,}")
    answer = p3.sub(".", answer)
    print("p3 after:", answer)

    #  4단계 : 마침표가 처음이나 끝에 있으면 제거
    p4 = re.compile("^[.]|[.]$")
    answer = p4.sub("", answer)

    #  5단계 : 빈 문자열이라면 a 대입
    answer = "a" if answer == "" else answer

    #  6단계 : 16자 이상이면 좌측 15문자만 남김, 제거 후 마지막이 마침표면 다시 제거
    answer = answer[:15] if len(answer) >= 16 else answer
    answer = answer[:14] if answer[-1:] == "." else answer

    #  7단계 : 길이가 2자 이하라면 new_id 마지막 문자를 new_id 길이가 3이 될 때 까지 반복해서 붙입니다.
    #answer = "ab"
    if len(answer) <= 2:
        firstChar = "" if len(answer) == 1 else answer[0:1]
        lastChar = answer[-1:]
        answer = firstChar + (lastChar * (3 - len(answer) + 1))
    
    return "정답:" + answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
#print(solution("!@#$-_."))