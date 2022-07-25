def solution(s):
    dicNum = {
                0:'zero'
              , 1:'one'
              , 2:'two'
              , 3:'three'
              , 4:'four'
              , 5:'five'
              , 6:'six'
              , 7:'seven'
              , 8:'eight'
              , 9:'nine'
    }

    #   숫자와 문자열을 끊어낼 방안?
    #   dic 루프를 돌아서 존재하면 replace?

    bDigit = s.isdigit()
    while bDigit == False:
        for i in dicNum: 
            strIndex = s.find(dicNum.get(i))
            if(strIndex > -1):
                s = s.replace(dicNum.get(i), str(i))
                print("in Loop:",s)
                bDigit = s.isdigit()
                if bDigit: break
                else: continue
    
    answer = int(s)
    return answer

#rst = solution("1one23one")
rst = solution("one4seveneight")
print(rst)