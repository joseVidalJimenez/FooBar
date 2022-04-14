def solution(M, F):
    count = 0
    m = int(M)
    f = int(F)

    while m != 1 or f != 1:
        if m == 1 or f == 1:
            if m == 1:
                count += f - 1
            if f == 1:
                count += m - 1
            break

        if m < f:
            if m == 0:
                return "impossible"
            count += f / m
            f %= m
        else:
            if f == 0:
                return "impossible"
            count += m / f
            m %= f

    return str(count)
    
def test():
    status = []
    if solution('3', '2') == '1': status.append("1:pass")
    if solution('2', '1') == '1': status.append("2:pass")
    if solution('4', '7')    == '4': status.append("3:pass")
    if solution('2', '4') == 'impossible': status.append("4:pass")
    # s3 = solution('1', '1')
    # print("init=%s" % s3)
    print("#########################") 
    print(*status)


test()
    
"""
2,4: passed
"""