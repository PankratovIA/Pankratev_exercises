def decimal2k(A, k):
    """
    A -- natural number
    k -- base 
    """
    b = []
    while A > 0:
        b.append(A % k)
        A //= k
    return (b[::-1], len(b))
    
if __name__ == "__main__":
    print(decimal2k(7, 2))
    print(decimal2k(8, 2))
        
    