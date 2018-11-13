
def toPeriodic(nom, denom, base):
    """
        convertation from nom / denom to periodic fraction
        nom < denom for simplicity
        http://zftsh.online/articles/683
    """
    print(nom, denom)
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
            period = digits[d[nom]+1:]
            frac = digits[:d[nom]+1]
            return (frac, period)
        digits.append(cur)
        d[nom] = idx
        idx += 1
    return (digits, [])
    
if __name__ == "__main__":
    print("From Rational to periodic")
    ans = toPeriodic(3, 8, 10)
    print(ans)
    
    ans = toPeriodic(4, 9, 10)
    print(ans)
    
    ans = toPeriodic(5, 6, 10)
    print(ans)
    
    # Take a look on last 3 tests. One or two are wrong.
    # 10 : 0.375 = 2 : 0.011
    # 10 : 9/11 = 10 : 0.(81)
    # 10: 0.123 = 5 : 0.030(14)
    ans = toPeriodic(9, 11, 10)
    print(ans)
    
    ans = toPeriodic(123, 1000, 5)
    print(ans)
    
    ans = toPeriodic(3, 8, 2)
    print(ans)