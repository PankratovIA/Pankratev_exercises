
def vectorToDecimal(M, K):
    assert (len(K) == len(M) + 1)
    if not M:
        return K[0]
    return K[0] + (M[0] * vectorToDecimal(M[1:], K[1:]))


if __name__ == "__main__":
    print("Vector (mixed) base")
    
    print(vectorToDecimal((2, 3), (1, 1, 1)))
    
    