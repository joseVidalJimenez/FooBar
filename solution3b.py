def solution(xs):
    
    #trivial cases
    nCeros = list(filter(lambda x: (x == 0), xs))  #grab ceros
    if len(xs) == len(nCeros) : return '0'
    
    nOnes = list(filter(lambda x: (x == 1), xs))  #grab ceros
    if len(xs) == len(nCeros) : return '1'    
    
    if len(xs) == 1 : return("%d" % xs[0])
    
    negArr = list(filter(lambda x: (x < 0), xs))   #grab negatives
    posgArr = list(filter(lambda x: (x > 0), xs)) #grab positives
    
    #Massaging negatives
    negCount = len(negArr) # number of negative numbers
    mod = negCount % 2
    #If it is an odd number of negatives
    if mod > 0:
        negArr.sort()
        negArr.pop()    #getting rid of the highest


    # print(negArr)
    # print(posgArr)
    # print("") 

    xsNew = negArr + posgArr
    
    if not xsNew: return '0'
    
    power = 1;
    for i in xsNew:
        power *= i
    
    return str(power)   
    
def test():
    status = []
    if solution([2, 0, 2, 2, 0]) == "8": status.append("1:passed")
    if solution([-2, -3, 4, -5]) == "60": status.append("2:passed")
    if solution([2, -3, 1, 0, -5]) == "30": status.append("3:passed")
    if solution([0, 0, 0, 0, 0]) == "0": status.append("4:passed")
    if solution([1, 1, 1, 1, 1]) == "1": status.append("5:passed")
    if solution([-2]) == "-2": status.append("6:passed")
    if solution([-2, 1]) == "1": status.append("7:passed")
    if solution([-2, 0]) == "0": status.append("8:passed")
    
    print(*status)

test()

"""

Keep track:
    nNeg: even or odd
    minNeg: lowest negative number
"""