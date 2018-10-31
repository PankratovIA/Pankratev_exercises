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

if __name__ == "__main__":
    print("Conversion between Roman and decimal numbers")
    
    roman = ['MCMXLVIII', 'XXXI', 'CXXIV', 'VIII', 'L', 'DCCXLVIII']
    
    for r in roman:
        d = RomanToDecimal(r)
        back_r = DecimalToRoman(d)
        print(r, d, back_r, r == back_r)
        
    cnt = 0
    for i in range(1, 4000):
        r = DecimalToRoman(i)
        d = RomanToDecimal(r)
        #print(i, r, d, i==d)
        cnt += (i == d)
    print("Good double conversions = ", cnt)