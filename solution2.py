def solution(s):
    #calculate salutes
    counter = 0;
    nChar = len(s)
    for i in range(0, nChar-1):
        if s[i] =='>':
            # print(i)
            for j in range(i+1, nChar):
                if (s[i]=='>' and s[j]=='<'):
                    counter += 2
                    # print(j)

    # print(counter)
    return counter

def test():
    if solution(">----<")==2: print("1:Pass")
    if solution("<<>><")==4: print("2:Pass")
    if solution("<<>><<>>")==8: print("3:Pass")
    if solution(">><>><")==12: print("4:Pass")

# solution(">----<")
test()


"""
<<>><
    >><

<<>><<>>
    >><<

>><>><
    >>< >><


import sys: get rid of new line on every print
    print(i),end=""
    .rstrip()
"""