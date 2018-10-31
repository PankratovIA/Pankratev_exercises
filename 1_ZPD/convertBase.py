def fromDecimal(A, k):
    """
        A -- natural number
        k -- base 
    """
    assert A>0, "A should be natural number"
    assert k>1, "Base should be greater than 1"
    b = []
    while A > 0:
        b.append(A % k)
        A //= k
    return (tuple(b[::-1]), len(b))
    
    
def toDecimal(k, num):
    """
        num -- tuple for number in k-based system
        k -- base 
    """
    assert num, "There should be at least one digit in number"
    A = 0
    for b in num[::-1]:
        assert 0<=b<k, "All digits should be in [0; k)."
        A = A * k + b
        
    return A
    
if __name__ == "__main__":
    print(fromDecimal(7, 2))
    print(fromDecimal(8, 2))
    
    print(toDecimal(2, (1, 1, 0)))
    print(toDecimal(2, (1, )))
    
    