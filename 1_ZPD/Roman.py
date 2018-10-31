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
    
def sumRoman(r1, r2):
    print(r1, r2)
    r1 = parseRoman(r1)
    r2 = parseRoman(r2)
    
    plus = sorted(r1[0] + r2[0], key=lambda x: DIGITS[x], reverse=True)
    minus = sorted(r1[1] + r2[1], key=lambda x: DIGITS[x], reverse=True)
    
    print('plus =', plus)
    print('minus =', minus)
    
    ans = ''.join(plus)
    return ans
    

if __name__ == "__main__":
    print("Conversion between Roman and decimal numbers")
    
    roman = ['MCMXLVIII', 'XXXI', 'CXXIV', 'VIII', 'L', 'DCCXLVIII']
    
    for r in roman:
        d = RomanToDecimal(r)
        back_r = DecimalToRoman(d)
        #print(r, d, back_r, r == back_r)
        print(r, parseRoman(r))
        
    cnt = 0
    for i in range(1, 4000):
        r = DecimalToRoman(i)
        d = RomanToDecimal(r)
        #print(i, r, d, i==d)
        cnt += (i == d)
    print("Good double conversions = ", cnt)
    
    print(sumRoman('MCMXLVIII', 'CXXIV'))
