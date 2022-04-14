def solution(M, F):
    # print("###### START ############") 
    try:
        m = int(M)
        f = int(F)
        
        # print("mfo:",m, f)
    except:
        return 'impossible'
    
    if m == f:  return 'impossible'
    elif m == 0 or f == 0:  return 'impossible'
    elif m == f+1: return str(f)
    elif f == m+1: return str(m) 
    elif m < 0 or f < 0:  return 'impossible'
    elif m == 1 and f > m:  return str(f-1)
    elif f == 1 and m > f:  return str(m-1)
    
    # print("\tmfi:",m, f)
    
    gen = 0
    while 1:
        cmp = f > m
        if cmp: 
            mult = (f // m)
            # print("mult:",mult)
            f = f-m*mult
        else:
            mult = (m // f)
            m = m -f*mult
        gen +=1
        # print("mult:",mult)
        # print("mfs:",m, f)
        # print("g:",gen)
        
        if m == 0 or f == 0: return 'impossible'
        elif m == 1:
            if f == 1: return str(gen)
            elif f > m:  return str((f-1)+gen)#necessary, not tested
        elif f == 1 and m > f:  return str((m-1)+gen)#necessary, not tested
        elif m == f+1 or f == m+1:  return str(min(m,f)+gen)

def test():
    status = []
   
    if solution('2', '1') == '1': status.append("1:pass")
    if solution('4', '7') == '4': status.append("2:pass")
    if solution('2', '4') == 'impossible': status.append("3:pass")
    if solution('4', '31')  == '4': status.append("4:pass")   
    if solution('0', '0')  == 'impossible': status.append("5:pass")
    if solution('5', '5')  == 'impossible': status.append("6:pass")
    if solution('99999999999999999999999999999999999999999999999999', \
        '100000000000000000000000000000000000000000000000000')  == \
        '99999999999999999999999999999999999999999999999999': \
        status.append("7:pass")
    if solution('40', '41')  == '40': status.append("8:pass") 
    if solution('0','19917')  == 'impossible': status.append("9:pass")
    if solution('100000000000000000000000000000000000000000000000000', '1') == '99999999999999999999999999999999999999999999999999': status.append("10:pass")
    if solution('-9', '5') == 'impossible': status.append("11:pass")
    if solution('fuck', '5') == 'impossible': status.append("12:pass")
    # print(solution('2', '1'))
    # print(solution('63986129451099560133283385270766427353806083067445', '17197069234675055699715946860902099391306494672125'))#error
    # print("###### END ############") 
    print(*status)
    if len(status) == 12: print("All Test Passed")

def rndTest():
    from random import randrange
    import matplotlib.pyplot as plt
    
    plotIt = 0
    rng = 100000
    Xector = []
    Yector = []
    Xfail = []
    Yfail = []
        
    try:
        for x in range(100000000000000000000000000000000000000000000000001):
            x1 = randrange(0,100000000000000000000000000000000000000000000000000)
            y1 = randrange(0,100000000000000000000000000000000000000000000000000)
            result = solution(str(x1), str(y1))
            if plotIt == 1:
                if result != 'impossible':
                    # print("%s\t%s"%(x1, y1))
                    Xector.append(x1)
                    Yector.append(y1)
                else:
                    Xfail.append(x1)
                    Yfail.append(y1)
    except:
        print("Error: \'%d\',\'%d\'"%(x1,y1))
    
    if plotIt == 1:
        plt.plot(Xector, Yector, 'ro', markersize=2)#x, y vectors
        plt.plot(Xfail, Yfail, 'ko', markersize=2)#x, y vectors
        plt.yscale('log')
        plt.xscale('log')
        # plt.axis([0, 6, 0, 20])#range for x,y axis
        plt.show()

def test2():
    fixed = 255
    maxRange = fixed*2
    countNot = 0
    countYes = 0
    
    # x,y = 0,0
    # print("###### IMPOSSIBLE ############") 
    # for y in range(1,fixed):
        # for x in range(1,maxRange):
            # result = solution(y, str(x))
            # if result == 'impossible':
                # if x < y: 
                    # print("%d %d \t%d %f "%(y, x, y//x, y/x))
                # else: 
                    # print("%d %d \t%d %f"%(y, x, x//y, x/y))
                # countNot +=1
        
    x,y = 0,0    
    print("\n\n\n\n\###### POSSIBLE ############") 
    for y in range(2,fixed):    
        for x in range(1,maxRange):
            result = solution(y, str(x))
            if result != 'impossible':
                if x > y: 
                    print("%d %d \t%d %f "%(y, x, x//y, x/y))
                else: 
                    print("%d %d \t%d %f"%(y, x, y//x, y/x))
                countYes +=1
                
    # print("no:%d\tyes:%d"%(countNot, countYes))

    
# test()
rndTest()
# test2()



"""

        if x < fixed: print("%d %d %d %f %s"%(fixed, x, fixed//x, fixed/x, str(solution(fixed, str(x)))))
        else: print("%d %d %d %f \t%s"%(fixed, x, x//fixed, x/fixed, str(solution(fixed, str(x)))))
        
        
    -----------------------------------
    bombs = [m,f]
    prime = []
    
    for n in bombs:
        if n == 3 or n ==2: prime.append('True'); break
        elif (n % 2 == 0) or (n % 3 == 0): prime.append('False'); break

        i = 5

        while (i*i <= n):
            if (n % i == 0) or (n % (i + 2) == 0): prime.append('False'); break
            i = i + 6
        else:
            prime.append('True')
        
    if m>f:
        if prime[1] == 'True' and (m/f).is_integer(): return 'impossible'
    else:
        if prime[0] == 'True' and (f/m).is_integer(): return 'impossible'  

    print(*prime)
"""