number_word = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",  # 错写成ninty
    100: "hundred",
    1000: "one thousand",
}

letter_count = 0

for i in range(1, 1001):
    word = ""
    flag = 0
    if i // 1000 == 1:
        word += number_word[1000] + " "
        i = i % 1000
    if i // 100 > 0:
        word += number_word[i // 100] + " " + number_word[100]
        i = i % 100
        if i > 0:
            flag = 1
    if i // 10 > 1:
        if flag == 1:
            word += " and "
        word += number_word[i % 100 // 10 * 10] + "-" + number_word[i % 10]
    else:
        if flag == 1:
            word += " and "
        word += number_word[i % 100]
    # print(word)
    format_word = word.replace(" ", "").replace("-", "")
    letter_count += len(format_word)
print(letter_count)