


text = input('What would you like to cipher?')
print(text)


def split(word):
    return [char for char in word]


def intoCipher(otext, p, k):
    arrLow = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    arrCap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    indexA = 0
    lowOrUp = '0'
    b = 0
    x = len(otext)
    index = 0
    while index < x:
        while indexA < 25 and lowOrUp == '0':
            if otext[index] == arrLow[indexA]:
                lowOrUp = '1'
                p = indexA
                b = 1
            elif otext[index] == arrCap[indexA] and lowOrUp == '0':
                lowOrUp = '1'
                p = indexA
                b = 2
            indexA += 1
        k = shift(p)
        if b == 1:
            otext[index] = arrLow[k]
        elif b == 2:
            otext[index] = arrCap[k]
        b = 0
        lowOrUp = '0'
        index += 1
        indexA = 0
    return otext


def shift(indexes):

    if indexes < 25 - 8:
        indexes += 8
    else:
        indexes -= 17
    return indexes

text = split(text)

text = intoCipher(text, 0, 0)

text = ''.join(text)

print('The ciphered text is')
print(text)
