
DAY2NUM = {'понедельник': 0, 'вторник': 1, 'среда': 2, 'четверг': 3,\
          'пятница': 4, 'суббота': 5, 'воскресенье': 6}
NUM2DAY = {0: 'понедельник', 1: 'вторник', 2: 'среда', 3: 'четверг',\
           4: 'пятница', 5: 'суббота', 6: 'воскресенье'}

def vectorToDecimal(M, K):
    assert (len(K) == len(M) + 1)
    if not M:
        return K[0]
    return K[0] + (M[0] * vectorToDecimal(M[1:], K[1:]))

def decimalToVector(M, k):
    if not M:
        return (k, )
    return (k % M[0],) + decimalToVector(M[1:], k // M[0])

if __name__ == "__main__":
    print("Vector (mixed) base")
    
    print(vectorToDecimal((2, 3), (1, 1, 1)))
    
    M = (60, 60, 24)
    
    dates = [('среда', 5, 7, 6), ('понедельник', 5, 7, 6), \
    ('понедельник', 0, 1, 0), ('понедельник', 1, 0, 0), ('понедельник', 0, 0, 1)]
    for date in dates:
        K = date[-1:0:-1] + (DAY2NUM[date[0]], )
        sec = vectorToDecimal(M, K)
        print(sec, "second(s) passed")
    
        f = (sec == (DAY2NUM[date[0]] * 86400 + date[1] * 3600 +\
            date[2] * 60 + date[3]))
        if not f:
            print('date -> sec', date, sec)
        assert f
        
        d = decimalToVector(M, sec)
        d = (NUM2DAY[d[-1]], ) + d[-2::-1]
        print(d)
        f = (d == date)
        if not f:
            print('sec -> date', date, sec)
        assert f
        
        
    