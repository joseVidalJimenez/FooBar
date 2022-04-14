

def solution(xs):
    import numpy as np
    arr = np.array(xs)  #creating np array
    result = np.where(arr == 0)
    
    # for i in result:
        # print(i)
    
    arrMod = np.delete(arr, result)
    power = np.prod(arrMod)
    print(power)
    return str(power)   
    
def test():
    if solution([2, 0, 2, 2, 0]) == "8": print("1:passed")
    if solution([-2, -3, 4, -5]) == "60": print("2:passed")
    if solution([2, -3, 1, 0, -5]) == "30": print("3:passed")


test()