# 题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

# for i in ['x', 'y', 'z']:
#     if i != 'x':
#         for j in ['x', 'y', 'z']:
#             if i != j:
#                 for k in ['x', 'y', 'z']:
#                     if (i != k) and (j != k):
#                         if (k != 'x') and (k != 'z'):
#                             print('order is a -- %s\t b -- %s\tc--%s' % (i, j, k))
#
# a = [1, 2, 3]
# b = 3
# a.remove(b)
# c=a
# print(c)
