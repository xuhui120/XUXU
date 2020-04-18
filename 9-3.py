import os
import re

with open("C:\\Users\\Administrator\\Desktop\\report.txt") as f:
    lines = f.readlines()
    print(lines)
    print(type(lines))
    ##########################################
    c = []  ####生成一个列表中的列表
    for l in lines:
        b = l.strip("\n")
        c.append(b)
    print(type(c), c)
    ddd = []
    for d in c:
        dd = d.split(" ")
        ddd.append(dd)
        print(ddd)  # DDD双层列表
#########################################################

    biaotou = ddd[0]  ###制作一个表头
    biaotou.insert(0, "名次")
    biaotou.insert(11, "总分数")
    biaotou.insert(12, "平均分")
    print(biaotou)
#########################################################计算出总分和平均分
ii = []
for i in ddd[1:]:
    sc = 0
    for p in i[1:]:
        sc = sc + float(p)
    pj = round(sc / 9, 2)
    i.append(sc)
    i.append(pj)
    print(sc)
    print(pj)
    print(i)
    ii.append(i)
print(ii)
####################################################################排序

ii.sort(key=lambda x: x[10], reverse=True)
print(ii)
####################################添加名次
mc = 0
xinapai=[]
for mm in ii:
    mm.insert(0, mc)
    mc = mc + 1
    print(mm)
    xinapai.append(mm)
###################################写入文件
with open("C:\\Users\\Administrator\\Desktop\\repASDFt.txt", "w") as ff:
    ff.writelines(str(biaotou)+'\n')
    for ppp in xinapai:
        ff.writelines(str(ppp)+'\n')
    ff.close()

