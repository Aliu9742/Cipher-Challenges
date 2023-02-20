import matplotlib.pyplot as plt
import bs4 as bs
import urllib.request
import numpy as np

n = 26
def normalize_frequency_distribution(distribution):
    """
    divide every single item in array by sum of array
    so that all elements sum up to 1
    """
    normalized = []
    array_sum = sum(distribution)
    for item in distribution:
        normalized.append(item / array_sum)
    return normalized

cipherText = """
BT JPX RMLX PCUV AMLX ICVJP IBTWXVR CI M LMT'R PMTN, MTN YVCJX CDXV MWMBTRJ JPX AMTNGXRJBAH UQCT JPX QGMRJXV CI JPX YMGG CI JPX HBTW'R QMGMAX; MTN JPX HBTW RMY JPX QMVJ CI JPX PMTN JPMJ YVCJX. JPXT JPX HBTW'R ACUTJXTMTAX YMR APMTWXN, MTN PBR JPCUWPJR JVCUFGXN PBL, RC JPMJ JPX SCBTJR CI PBR GCBTR YXVX GCCRXN, MTN PBR HTXXR RLCJX CTX MWMBTRJ MTCJPXV. JPX HBTW AVBXN MGCUN JC FVBTW BT JPX MRJVCGCWXVR, JPX APMGNXMTR, MTN JPX RCCJPRMEXVR. MTN JPX HBTW RQMHX, MTN RMBN JC JPX YBRX LXT CI FMFEGCT, YPCRCXDXV RPMGG VXMN JPBR YVBJBTW, MTN RPCY LX JPX BTJXVQVXJMJBCT JPXVXCI, RPMGG FX AGCJPXN YBJP RAMVGXJ, MTN PMDX M APMBT CI WCGN MFCUJ PBR TXAH, MTN RPMGG FX JPX JPBVN VUGXV BT JPX HBTWNCL. JPXT AMLX BT MGG JPX HBTW'R YBRX LXT; FUJ JPXE ACUGN TCJ VXMN JPX YVBJBTW, TCV LMHX HTCYT JC JPX HBTW JPX BTJXVQVXJMJBCT JPXVXCI. JPXT YMR HBTW FXGRPMOOMV WVXMJGE JVCUFGXN, MTN PBR ACUTJXTMTAX YMR APMTWXN BT PBL, MTN PBR GCVNR YXVX MRJCTBRPXN. TCY JPX KUXXT, FE VXMRCT CI JPX YCVNR CI JPX HBTW MTN PBR GCVNR, AMLX BTJC JPX FMTKUXJ PCURX; MTN JPX KUXXT RQMHX MTN RMBN, C HBTW, GBDX ICVXDXV; GXJ TCJ JPE JPCUWPJR JVCUFGX JPXX, TCV GXJ JPE ACUTJXTMTAX FX APMTWXN; JPXVX BR M LMT BT JPE HBTWNCL, BT YPCL BR JPX RQBVBJ CI JPX PCGE WCNR; MTN BT JPX LAMER CI JPE IMJPXV GBWPJ MTN UTNXVRJMTNBTW MTN YBRNCL, GBHX JPX YBRNCL CI JPX WCNR, YMR ICUTN BT PBL; YPCL JPX HBTW TXFUAPMNTXOOMV JPE IMJPXV, JPX HBTW, B RME, JPE IMJPXV, LMNX LMRJXV CI JPX LMWBABMTR, MRJVCGCWXVR, APMGNXMTR, MTN RCCJPRMEXVR; ICVMRLUAP MR MT XZAXGGXTJ RQBVBJ, MTN HTCYGXNWX, MTN UTNXVRJMTNBTW, BTJXVQVXJBTW CI NVXMLR, MTN RPCYBTW CI PMVN RXTJXTAXR, MTN NBRRCGDBTW CI NCUFJR, YXVX ICUTN BT JPX RMLX NMTBXG, YPCL JPX HBTW TMLXN FXGJXRPMOOMV; TCY GXJ NMTBXG FX AMGGXN, MTN PX YBGG RPCY JPX BTJXVQVXJMJBCT. JPX IBVRJ ACNXYCVN BR CJPXGGC.
"""

"""
count letter frequency in cipher text
"""
# index i correspond to i'th letter of alphabet
cipherLetterFrequency = [0 for i in range(n)]
for char in cipherText:
    if not char.isalpha():
        continue

    index = ord(char) - ord("A")
    cipherLetterFrequency[index] += 1

totalLetterCount = sum(cipherLetterFrequency)
cipherLetterFrequency = normalize_frequency_distribution(cipherLetterFrequency)

"""
scrape plain English letter frequency from 
https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
"""
source = urllib.request.urlopen("https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html")
soup = bs.BeautifulSoup(source, "html.parser")
table = soup.table
plainLetterFrequency = [0 for i in range(n)]
not_header = False
for cell_number, cell in enumerate(table.find_all("td"), 1):
    if not (cell_number + 1) % 5 and not_header:
        letter = cell.get_text()
    if not cell_number % 5 and not_header:
        frequency = cell.get_text()
        plainLetterFrequency[ord(letter) - ord("A")] = float(frequency)
    
    if not cell_number % 5:
        not_header = True

plainLetterFrequency = normalize_frequency_distribution(plainLetterFrequency)

letters = [chr(i) for i in range(ord("A"), ord("Z")+1)]

"""
plotting frequencies of letters


r = np.arange(n)
width = 0.25

plt.xlabel("letter")
plt.ylabel("% occruence")
plt.xticks(r+width/2, letters)


plt.bar(letters, cipherLetterFrequency, color = 'b',
        edgecolor = 'black',
        label = 'cipher text')
plt.bar(letters, plainLetterFrequency, color = 'g',
        edgecolor = 'black',
        label = "plain text")
plt.legend()
plt.show()
"""

def decipher(cipherText, letterReplacements):
    """
    letter replacements is a dictionary, the keys are cipher text (in caps) and values are plain text (lower case)
    given cipher text, replace with plain text
    """
    plain = []
    for char in cipherText:
        if char in letterReplacements:
            plain.append(letterReplacements[char])
        else:
            plain.append(char)
        
    return "".join(plain)

decipherKey = {
    "X" : "e",
    "J" : "t",
    "P" : "h",
    "F" : "b",
    "M" : "a",
    "R" : "s",
    "T" : "n",
    "N" : "d",
    "C" : "o",
    "V" : "r",
    "Y" : "w",
    "U" : "u",
    "G" : "l",
    "A" : "c",
    "I" : "f",
    "B" : "i",
    "Q" : "p",
    "W" : "g",
    "E" : "y",
    "L" : "m",
    "D" : "v",
    "H" : "k",
    "K" : "q",
    "Z" : "x",
    "S" : "j",
    "O" : "z"
}

encryptKey = {decipherKey[char] : char for char in decipherKey}

print(decipher(cipherText, decipherKey))

for letter in letters:
    if letter.lower() in encryptKey:
        print(encryptKey[letter.lower()], end=" ")
    else:
        print(" ", end=" ")
print()
print(" ".join([i.lower() for i in letters]))

        



