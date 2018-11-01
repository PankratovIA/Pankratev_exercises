
DAYNUM = {'понедельник': 0, 'вторник': 1, 'среда': 2, 'четверг': 3,\
          'пятница': 4, 'суббота': 5, 'воскресенье': 6}

def vectorToDecimal(M, K):
    assert (len(K) == len(M) + 1)
    if not M:
        return K[0]
    return K[0] + (M[0] * vectorToDecimal(M[1:], K[1:]))


if __name__ == "__main__":
    print("Vector (mixed) base")
    
    print(vectorToDecimal((2, 3), (1, 1, 1)))
    
    M = (60, 60, 24)
    
    dates = [('среда', 5, 7, 6), ('понедельник', 5, 7, 6), \
    ('понедельник', 0, 1, 0), ('понедельник', 1, 0, 0), ('понедельник', 0, 0, 1)]
    for date in dates:
        K = date[-1:0:-1] + (DAYNUM[date[0]], )
        sec = vectorToDecimal(M, K)
        print(sec, "second(s) passed")
    
        f = (sec == (DAYNUM[date[0]] * 86400 + date[1] * 3600 +\
            date[2] * 60 + date[3]))
        if not f:
            print(date, sec)
        assert f
        
    