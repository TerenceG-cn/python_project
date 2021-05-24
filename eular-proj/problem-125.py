# https://www.cnpython.com/qa/463900
def is_palindrome(s):
    return s == s[::-1]

def values(n):
    squares = [0]
    i = 1
    while i * i <= n:
        squares.append(squares[-1] + i * i)
        i += 1
    pals = set()
    for i in range(1, len(squares)):
        j = i + 1
        while j < len(squares) and (squares[j] - squares[i - 1]) <= n:
            s = squares[j] - squares[i - 1]
            if is_palindrome(str(s)):
                pals.add(s)
            j += 1
    #return len(pals)
    return sum(pals)
print(values(1000_000_00))
