from Roman import *

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
    #print("compress >>> ")
    tmp = [('DD', 'M'), ('CCCC', 'CD'), ('LL', 'C'), ('LXL', 'XC'),\
     ('XLX', 'L'),\
     ('XXXX', 'XL'), ('VV', 'X'), ('VIV','IX'), ('IIIII', 'V'), ('IIII', 'IV')]
    
    f = True
    while f:
        f = False
        for cur in tmp:
            while cur[0] in num:
                f = True
                #print('cur = ', cur)
                #print('num = ', num)
                num = num.replace(cur[0], cur[1])
                #print(num)
                #break
    #print("compress <<< ")
    
    return num
    
    
def sumRoman(r1, r2):
    #print(r1, r2)
    r1 = parseRoman(r1)
    r2 = parseRoman(r2)
    
    
    plus = r1[0] + r2[0]
    minus = r1[1] + r2[1]
    
    if not minus:
        plus = sorted(plus, key=lambda x: DIGITS[x], reverse=True)
    
    while minus:
        #print('plus =', plus)
        #print('minus =', minus)
        
        plus = sorted(plus, key=lambda x: DIGITS[x], reverse=True)
        minus = sorted(minus, key=lambda x: DIGITS[x], reverse=True)
    
        #print('plus =', plus)
        #print('minus =', minus)
    
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
        
        #print('plus =', plus)
        #print('minus =', minus)
        
        if not minus:
            break
            
        #print('minus = ', minus)
        x = minus.pop()
        
        #print('x = ', x)
        
        idx = len(plus) - 1
        
        while (DIGITS[plus[idx]] < DIGITS[x]):
            idx-=1
        
        #print('plus[idx] = ', plus[idx])
        
        plus = plus[:idx] + list(tmp[plus[idx]][x]) + plus[idx+1:]
        
        #print(plus)
        
        #plus = compressRoman(''.join(plus))
        
        #plus = parseRoman(plus)
        #minus += plus[1]
        #plus = plus[0]

        #print('plus =', plus)
        #print('minus =', minus)
    #print(plus)
    ans = compressRoman(''.join(plus))
    
    return ans

if __name__ == "__main__":
    roman = ['XIX', 'IX', 'VIII']
    
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
    
    MX = 49
    for x in range(1, MX):
        for y in range(1, MX):
            a, b = list(map(DecimalToRoman, [x, y]))
            c = sumRoman(a, b)
            print(a + ' + ' + b + ' = ' + c)
    
            s = list(map(RomanToDecimal, [a, b, c]))
            print(s)
            f = (s[0] + s[1] == s[2])
            print(f)
            assert f
