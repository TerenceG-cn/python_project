from itertools import combinations

ascii_dict = {
    'a': '01100001',
    'b': '01100010',
    'c': '01100011',
    'd': '01100100',
    'e': '01100101',
    'f': '01100110',
    'g': '01100111',
    'h': '01101000',
    'i': '01101001',
    'j': '01101010',
    'k': '01101011',
    'l': '01101100',
    'm': '01101101',
    'n': '01101110',
    'o': '01101111',
    'p': '01110000',
    'q': '01110001',
    'r': '01110010',
    's': '01110011',
    't': '01110100',
    'u': '01110101',
    'v': '01110110',
    'w': '01110111',
    'x': '01111000',
    'y': '01111001',
    'z': '01111010'
}
for comb in combinations("abcdefghijklmnopqrstuvwsyz", 3):
    encryption_key = ''
    for letter in comb:
        encryption_key+=ascii_dict[letter]
    print(encryption_key)




with open("eular-proj/p059_cipher.txt", "r") as f:
    fstr = f.read().replace('"', "")
    ascii_code_list = fstr.split(",")
    # print(len(ascii_code_list))
    count,tmp_code=1,''
    for ascii_code in ascii_code_list:
        ascii_code_bin = bin(int(ascii_code))[2:].zfill(8)
        # print(ascii_code_bin)
        count+=1
        tmp_code+=ascii_code_bin
        if count==3:
            src_code=tmp_code & encryption_key
            count=0
            tmp_code=''

# todo