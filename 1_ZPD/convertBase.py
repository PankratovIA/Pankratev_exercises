def fromDecimal(A, k):
    """
        A -- natural number
        k -- base 
    """
    assert A>0, "A should be natural number"
    assert k>1, "base should be greater than 1"
    b = []
    while A > 0:
        b.append(A % k)
        A //= k
    return (tuple(b[::-1]), len(b))
    
if __name__ == "__main__":
    print(decimal2k(7, 2))
    print(decimal2k(8, 2))
        
    