def solution(x,y):
    m=int(x)
    f=int(y)
    cnt=0
    while((m>1 or f>1) and (m!=0 and f!=0)):
        if(m>f):
            if(m>1000*f):
                cnt+=int(m/f)
                m-=int(m/f)*f                       
            else:
                m-=f
                cnt+=1
        elif(f>m):
            if(f>1000*m):           
                cnt+=int(f/m)
                f-=int(f/m)*m           
            else:
                f-=m
                cnt+=1
        else:
            return "impossible"

    return str(cnt)
    
    
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
    # print("###### END ############") 
    print(*status)
    

test()