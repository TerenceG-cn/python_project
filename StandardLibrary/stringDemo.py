import string

# ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
# ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# ascii_letters = ascii_lowercase + ascii_uppercase
# print(ascii_letters)


# # 1-1
# s = 'Prerelease users should be aware that this document is currently in draft form. ' \
#     'It will be updated substantially as Python 3.8 moves towards release, ' \
#     'so it’s worth checking back even after reading earlier versions.'
# # capwords()首字母大写
# print(string.capwords(s))
# print(s.title())
# # capitalize()将字符串的第一个字母变成大写,其他字母变小写
# print(s.capitalize())
#
#
# # capwords src
# def capwords_src(s, sep='连接序列,默认None'):
#     return (sep or ' ').join(word.capitalize() for word in s.split())
#
#
# print(capwords_src(s))

# 1-2
values = {'var': 'foo'}
t = string.Template("""
Variable    : $var
Escape      : $$
Variable in text: ${var}iable
""")
print('Template:', t.substitute(values))
