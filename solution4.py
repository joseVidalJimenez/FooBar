def solution(M, F):
    print("#########   NEW   ###########")
    S = []
    true = 1
    gen = 1
    sumX = 0
    sumY = 0
    difSum = 0
    #we will remember only next values, not past
    while true == 1 and gen<4:
        temp = []
        if not S:
            # init S0
            m = int(M)
            f = int(F)
            Mt = Ft = m + f
            #adding initial branch
            S.append([Mt, f])
            S.append([m, Ft])
            temp = list(S)  #helps verification after g1
            print("\nmf:  (%d,%d)"%(m,f))
            print("s%d :"%gen+"",*S)
        else:
            gen += 1
            for i in S:
                m,f = i
                Mt = Ft = m + f
                temp.append([Mt, f])
                temp.append([m, Ft])
            # print("temp:",temp[0])    
            print("s%d :"%gen+"",*temp)
        
        #getting a slice (p1,p2)
        p = (temp[::2],temp[1::2])
        print("\n\tp1", p[0])
        print("\n\tp2", p[1])
        #calculating sum for p1 and p2
        tSum = []
        rn = len(p)
        for i in range(rn):
            sumX,sumY = 0,0
            for j in p[i]:
                x,y = j
                sumX += x
                sumY += y
                # print("x:",x)
            tSum.append([sumX,sumY])
            print("tSum",tSum[i])
            # print("i:",i)
        
        #exit plan
        x1,y1 = tSum[0]
        x2,y2 = tSum[1]
        print("%d %d %d %d:"%(x1,y2,x2,y1))
        t1 = (y1+x2)==x1
        print("t1:",t1)
        # if t1:  
        if difSum == 1:
            print ("exitgen %d"% gen)
            return str(gen)
            true = 0
        else:
            #deleting and cloning
            del S[:]
            S = list(temp)
            print("")
    

def test():
    status = []
    # if solution('3', '2') == '1': status.append("1:pass")
    # if solution('2', '1') == '1': status.append("2:pass")
    if solution('4', '7')    == '4': status.append("3:pass")
    # if solution('2', '4') == 'impossible': status.append("4:pass")
    # s3 = solution('1', '1')
    # print("init=%s" % s3)
    print("#########################") 
    print(*status)


test()




"""

if difSum == 1:

case1: (Ft) + M
case2: (Mt) + F
    
        gen = 0
        for i in X:
            # print(i)
            for j in Y:
                if i == j: 
                    print(i, j)
                    gen = count+1
                    # return ("%d" % gen)
                    # print(gen)
                # print(j)
            print("")
        # print(S[count])
        print(S[count+1])
"""