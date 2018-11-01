DIGITS = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X':10, 'V': 5, 'I': 1}

NUMBERS = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', \
50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5:'V', 4: 'IV', 1: 'I'}

def RomanToDecimal(num):
    assert num, "Roman number should not be a blank string"
    assert all(d in DIGITS for d in num), "All digits should be Roman"

    if len(num) == 1:
        return DIGITS[num[0]]

    ans = 0
    cnt = 0
    for prev, cur in zip(num, num[1:]):
        if cur == prev:
            if (cnt == 0):
                cnt += 1
            cnt += 1
        else:
            cnt = 1
        assert cnt < 4, "There can be no more than 3 equal digits in succession"
        if DIGITS[cur] <= DIGITS[prev]:
            ans += DIGITS[prev]
        else:
            ans -= DIGITS[prev]
    ans += DIGITS[num[-1]]
    return ans
    
def DecimalToRoman(num):
    ans = '';
    for cur in sorted(NUMBERS, reverse=True):
        while num >= cur:
            num -= cur
            ans += NUMBERS[cur]
    return ans
    
    
def parseRoman(num):
    """
        From roman number to 2 lists of digits (+ and -) 
    """
    ans = ([], [])
    for cur in sorted(NUMBERS.items(), reverse=True):
        while num.startswith(cur[1]):
            ans[0].append(cur[1][-1]) # plus
            if (len(cur[1]) == 2):
                ans[1].append(cur[1][0]) # minus
            num = num[len(cur[1]):]
                
    return ans
    
def compressRoman(num):
    tmp = [('DD', 'M'), ('CCCC', 'CD'), ('LL', 'C'), ('LXL', 'XC'), ('XXXX', 'XL'), \
    ('VV', 'X'), ('VIV','IX'), ('IIIII', 'V'), ('IIII', 'IV')]
    
    f = True
    while f:
        f = False
        for cur in tmp:
            while cur[0] in num:
                f = True
                #print(cur)
                print(num)
                num = num.replace(cur[0], cur[1])
                print(num)
                #break
    return num
    
    
def sumRoman(r1, r2):
    print(r1, r2)
    r1 = parseRoman(r1)
    r2 = parseRoman(r2)
    
    plus = r1[0] + r2[0]
    minus = r1[1] + r2[1]
    
    while minus:
        print('plus =', plus)
        print('minus =', minus)
        
        plus = sorted(plus, key=lambda x: DIGITS[x], reverse=True)
        minus = sorted(minus, key=lambda x: DIGITS[x], reverse=True)
    
        print('plus =', plus)
        print('minus =', minus)
    
        delList = []
        for m in minus:
            if m in plus:
                plus.remove(m)
                delList.append(m)
    
        for x in delList:
            minus.remove(x)
            
        tmp= {'V':{'I': 'IIII'}, 'X':{'I':'VIIII'}, 'L':{'I':'XXXXVIIII',\
         'V':'XXXXV', 'X': 'XXXX'}, 'C':{'I': 'LXXXXVIIII',\
         'V':'XXXXXXXXXV', 'X':'LXXXX'}}
        
        print('plus =', plus)
        print('minus =', minus)
        
        if not minus:
            break
            
        print('minus = ', minus)
        x = minus.pop()
        
        print('x = ', x)
        
        idx = len(plus) - 1
        
        while (DIGITS[plus[idx]] < DIGITS[x]):
            idx-=1
        
        print('plus[idx] = ', plus[idx])
        
        plus = plus[:idx] + list(tmp[x][plus[idx]]) + plus[idx+1:]
        plus = compressRoman(''.join(plus))
        
        plus = parseRoman(plus)
        minus += plus[1]
        plus = plus[0]

        print('plus =', plus)
        print('minus =', minus)
    
    ans = compressRoman(''.join(plus))
    
    return ans
    

if __name__ == "__main__":
    print("Conversion between Roman and decimal numbers")
    
    roman = ['MCMXLVIII', 'XXXI', 'CXXIV', 'VIII', 'L', 'DCCXLVIII']
    
    # for r in roman:
    #     d = RomanToDecimal(r)
    #     back_r = DecimalToRoman(d)
    #     #print(r, d, back_r, r == back_r)
    #     print(r, parseRoman(r))
    #     
    # cnt = 0
    # for i in range(1, 4000):
    #     r = DecimalToRoman(i)
    #     d = RomanToDecimal(r)
    #     #print(i, r, d, i==d)
    #     cnt += (i == d)
    # print("Good double conversions = ", cnt)
    
    
    for a in roman:
        for b in roman:
            if a != b:
                c = sumRoman(a, b)
                print(a + ' + ' + b + ' = ' + c)
    
                s = list(map(RomanToDecimal, [a, b, c]))
                print(s)
                f = (s[0] + s[1] == s[2])
                print(f)
                assert f
    