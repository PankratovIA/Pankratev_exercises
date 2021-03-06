from fractions import Fraction

from convertBase import *

def toPeriodic(nom, denom, base):
    """
        convertation from nom / denom to periodic fraction
        http://zftsh.online/articles/683
        return (integer number, fraction, period)
    """
    print(nom, denom)
    intPart = nom // denom
    nom %= denom
    
    if intPart:
        intPart = fromDecimal(intPart, base)[0]
    else:
        intPart = (0,)
    d = {nom: -1}
    idx = 0
    digits = []
    while 1:
        cur = (nom * base) // denom
        # print('cur =', cur)
        # print('d =', d)
        # print('digits =', digits)
        nom = (nom * base) % denom
        if nom in d:
            digits.append(cur)
            period = tuple(digits[d[nom]+1:])
            frac = tuple(digits[:d[nom]+1])
            return (intPart, frac, period)
        digits.append(cur)
        d[nom] = idx
        idx += 1
    return (intPart, tuple(digits), ())
    
def toRational(num, base):
    """
        num = (integer number, fraction, period)
        https://studfiles.net/preview/1700684/page:2/
    """
    intPart = toDecimal(base, num[0])
    ans = Fraction(intPart)
    
    deg, mul  = Fraction(1, base), Fraction(1, base)
    for cur in num[1]:
        ans += cur * deg
        deg *= mul

    frac = toDecimal(base, num[2])
    ans += Fraction(frac, (base ** (len(num[2])) - 1) * (base ** len(num[1])))

    return ans
    
if __name__ == "__main__":
    print("From Rational to periodic and back")
    ans = toPeriodic(3, 8, 10)
    print(ans)
    
    ans = toRational(ans, 10)
    print("Rational =", ans)
    
    ans = toPeriodic(4, 9, 10)
    print(ans)

    ans = toRational(ans, 10)
    print("Rational =", ans)
    
    ans = toPeriodic(5, 6, 10)
    print(ans)
    
    ans = toRational(ans, 10)
    print("Rational =", ans)
    
    ans = toPeriodic(9, 11, 10)
    print(ans)

    ans = toRational(ans, 10)
    print("Rational =", ans)
    
    ans = toPeriodic(123, 1000, 5)
    print(ans)

    ans = toRational(ans, 5)
    print("Rational =", ans)
    
    ans = toPeriodic(3, 8, 2)
    print(ans)
    
    ans = toRational(ans, 2)
    print("Rational =", ans)
        
    ans = toPeriodic(4, 1, 2)
    print(ans)
    
    ans = toRational(ans, 2)
    print("Rational =", ans)
    
    