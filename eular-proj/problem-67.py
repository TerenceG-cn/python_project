# 路径选择算法

# -*-coding:utf-8-*-
# 用散列表实现图的关系
# 创建节点的开销表，开销是指从"起点"到该节点的权重

nums=[]
g={}
for line in open("eular-proj/p067_triangle.txt"):
    nums.append(line)
ln=i=0
for line in nums:
    ln+=1
    line=line[:-1].split(" ")
    #print(line)
    for num in line:
        i+=1
        g[str(ln)+"_"+str(i)]={}
        if str(ln-1)+"_"+str(i-1) in g.keys():
            g[str(ln-1)+"_"+str(i-1)][str(ln)+"_"+str(i)]=-num
        if str(ln-1)+"_"+str(i) in g.keys():
            g[str(ln-1)+"_"+str(i)][str(ln)+"_"+str(i)]=-num
        if str(ln-1)+"_"+str(i+1) in g.keys():
            g[str(ln-1)+"_"+str(i+1)][str(ln)+"_"+str(i)]=-num
    i=0

graph = {}

#todo

