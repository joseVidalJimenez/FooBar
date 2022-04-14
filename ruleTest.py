def rule(M, F):
    import math as math
    m = int(M)
    f = int(F)
    
    primeM = is_prime(m)
    primeF = is_prime(f)
    
    if m>f:
        if primeF == 'True' and (m/f).is_integer(): return 'impossible'
    else:
        if primeM == 'True' and (f/m).is_integer(): return 'impossible'

#check logbase is prime
def base23(M):
    import math
    
    number = int(M)
    
    for base in range(2, 4):
        c1 = math.log(number,base).is_integer()
        if c1:
            return base
            
 
#Primality  optimized wikipedia
def is_prime(n):
    if n <= 3: return str(n > 1)
    elif (n % 2 == 0) or (n % 3 == 0): return 'False'
   
    i = 5

    while (i*i <= n):
        if (n % i == 0) or (n % (i + 2) == 0): return 'False'
        i = i + 6
        
    return 'True'
    
    
#-----------------------------------------------------------
#base23
# for x in range(1,100):
    # print("number:%d \tbase:%s" % (x, str(rule2(x))))


#-----------------------------------------------------------
#tes if prime 
# for x in range(1,50):
    # if is_prime(x) == 'True':
        # print("\t",x, end="")

# if is_prime(2) != 'false':
    # print("2")
    
# print(is_prime(1))
#-----------------------------------------------------------

rule(13, 26)