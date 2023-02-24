cipherText = "MHILY LZA ZBHL XBPZXBL MVYABUHL HWWPBZ JSHBKPBZ JHLJBZ KPJABT HYJHUBT LZA ULBAYVU"

def ceasarShift(cipherLetter, plainLetter):
    cipherLetterNum = ord(cipherLetter.upper())
    plainLetterNum = ord(plainLetter.upper()) 
    shift = plainLetterNum - cipherLetterNum

    decrypt = {}
    for i in range(ord("A"), ord("Z")+1):
        if shift + i <= ord("Z") and shift + i >= ord("A"):
            decrypt[chr(i)] = chr(shift+i).lower()
        
        elif shift + i > ord("Z"):
            decrypt[chr(i)] = chr(shift+i-ord("Z")+ord("A")-1).lower()
        
        elif shift + i < ord("A"):
            decrypt[chr(i)] = chr(shift+i-ord("A")+ord("Z")+1).lower()

    return decrypt

def decipher(cipherLetter, plainLetter):
    key = ceasarShift(cipherLetter, plainLetter)
    print(key)
    plainText = []
    for char in cipherText:
        if char in key:
            plainText.append(key[char])
        else:
            plainText.append(char)
    print("".join(plainText))

"""
# brute force solution, try all 26 possible ceasar shifts
letters = [chr(i) for i in range(ord("a"), ord("z")+1)]
for letter in letters:
    decipher("L", letter)
"""

# solution:
decipher("A", "t")




    



