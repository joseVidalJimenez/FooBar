
def solution(encoding):
    eString = []
    for x in encoding:
        # print(">"+x)
        if x.isupper(): eString.append('000001'); x = x.lower()
        if x == "a":    eString.append('100000')
        elif x == "b":  eString.append('110000')
        elif x == "c":  eString.append('100100')
        elif x == "d":  eString.append('100110')
        elif x == "e":  eString.append('100010')
        elif x == "f":  eString.append('110100')
        elif x == "g":  eString.append('110110')
        elif x == "h":  eString.append('110010')
        elif x == "i":  eString.append('010100')
        elif x == "j":  eString.append('010110')
        elif x == "k":  eString.append('101000')
        elif x == "l":  eString.append('111000')
        elif x == "m":  eString.append('101100')
        elif x == "n":  eString.append('101110')
        elif x == "o":  eString.append('101010')
        elif x == "p":  eString.append('111100')
        elif x == "q":  eString.append('111110')
        elif x == "r":  eString.append('111010')
        elif x == "s":  eString.append('011100')
        elif x == "t":  eString.append('011110')
        elif x == "u":  eString.append('101001')
        elif x == "v":  eString.append('111001')
        elif x == "w":  eString.append('010111')
        elif x == "x":  eString.append('101101')
        elif x == "y":  eString.append('101111')
        elif x == "z":  eString.append('101011')
        elif x == " ":  eString.append('000000')
        
    together = ""
    for i in eString:
        together += i
    return together

def test():
    if solution("code")=="100100101010100110100010": print("1:Pass")
    if solution("Braille")=="000001110000111010100000010100111000111000100010": print("2:Pass")
    if solution("The quick brown fox jumps over the lazy dog")=="000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110": print("3:Pass")


# text = "code"
# text = "Braille"
text = "The quick brown fox jumps over the lazy dog"
slv = solution(text)
print(slv)

# test()


"""
x: has one char at the time


code: works
    100100101010100110100010

Braille:
000001 110000 111010100000010100111000111000100010              example
000001 110000 111010100000010100111000111000100010              mine

The quick brown fox jumps over the lazy dog:
000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110

Note:
    in the example mentions: solution(plaintext)
        so make sure that the name variable is the same
"""