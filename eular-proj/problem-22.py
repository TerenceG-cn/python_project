letter_value = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26,
}

name_list = []
with open("eular-proj/p022_names.txt", "r") as f:
    fstr = f.read().replace('"', "")
    name_list = fstr.split(",")
    name_list.sort()
    #print(len(name_list))

values = 0
name_value = 0
for i, name in enumerate(name_list):
    for letter in name:
        name_value += letter_value[letter]
    values += (i+1) * name_value
    name_value = 0

print(values)
