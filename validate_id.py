s=input("Please type your ID number here:")
s=str(s)
table={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':34,
        'J':18,'K':19,'L':20,'M':21,'N':22,'O':35,'P':23,'Q':24,'R':25,
        'S':26,'T':27,'U':28,'V':29,'W':32,'X':30,'Y':31,'Z':33}#建立身分證首位字母數字轉換表，以利檢查碼的計算
def IDvalidation(s):
    if len(s)!=10:#檢查是否為10碼
        return "Invalid ID"
    else:
        if not s[-9:].isdigit():#檢查後9碼格式是否為0-9。isdigit是內建的自動檢驗數字是否在0-9之間。不能寫成not in ['1','2']的原因是因為python會把後九碼去對陣列中的每個數字
            return "Invalid ID"
        else:
            if s[0] not in table:#檢查第一碼是否為table中的英文字母
                return "Invalid ID"
            else:
                if s[1] not in ['1', '2']:#檢查第二碼是否為1或2,不能用or語法，因為if的邏輯，是其中一個條件符合就會回傳true值，所以不管帶誰都是回傳true值
                    return "Invalid ID "
                else:
                    tendigit=table[s[0]] // 10 #取字母對應數字的10位數
                    digit=table[s[0]] % 10 #取字母對應數字的個位數
                    weighted_average=(tendigit*1+digit*9+int(s[1])*8+int(s[2])*7+int(s[3])*6+int(s[4])*5+int(s[5])*4+int(s[6])*3+int(s[7])*2+int(s[8])*1)#計算加權數
                    remain=weighted_average%10#取餘數
                    inspectnum = 10-remain#計算檢查碼
                    if str(inspectnum) == s[-1:]:#檢查計算的檢查碼是否和輸入的檢查碼相符,要記得把inspectnum轉成字串才能比較
                         return "Valid ID"
                    else:
                        return "Invalid ID"
print(IDvalidation(s))
while True:#重複顯示輸入ID的字串
    s = input("Please type your ID number here: ")
    print(IDvalidation(s))
