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
        dd = d.split(" ")   #主要目的是把字符串转成list
        ddd.append(dd)
        print(ddd)                       # DDD双层列表
#########################################################

    biaotou = ddd[0]  ###制作一个表头
    biaotou.insert(0, "名次")
    biaotou.insert(11, "总分数")
    biaotou.insert(12, "平均分")
    print(biaotou)
#########################################################计算出总分和平均分
ii = []
zonfeng=[]
for i in ddd[1:]:
    sc = 0
    for p in i[1:]:
        sc = sc + float(p)
    pj = round(sc / 9, 2)
    i.append(str(sc))
    i.append(str(pj))
    print(sc)
    print(pj)
    print(i)
    ii.append(i)
print(ii)
#############################################################计算每课的汇总及平均分
cd=len(ddd)-1
print(cd)
pj=[]
for kkk in range(1,10):
    pinjun=0
    zonfeng = 0

    for ttt in ii[1:]:
        zonfeng=zonfeng+int(ttt[kkk])
    pinjun=round(zonfeng/cd,2)
    pj.append(str(pinjun))
    zzz = 0
    for xxx in pj:
        zzz=zzz+float(xxx)
        zpj=round(zzz/9,2)
pj.append(str(zzz))
pj.append(str(zpj))
pj.insert(0,0)
pj.insert(1,"平均")
print(pj)
print("****************************************************")



####################################################################排序


ii.sort(key=lambda x: x[10], reverse=True)
print(ii)
####################################添加名次

mc = 1
xinapai=[]
for mm in ii:
    mm.insert(0, mc)
    mc = mc + 1
    print(mm)
    xinapai.append(mm)
xinapai.insert(0, pj)
print(xinapai)
print("****************************************")

###############################################替换不及格
xfenshu=[]
for i in xinapai[0:]:
    dd=["不及格" if float(pp)< 60 else pp for pp in i[2:]]

    dd.insert(0,i[0])
    dd.insert(1,i[1])
    print(dd)
print("**************************")
####################:###############写入文件
with open("C:\\Users\\Administrator\\Desktop\\result.txt", "w") as ff:
    aaa= "  ".join(biaotou)
    print(aaa)
    ff.writelines(str(aaa)+'\n')
    for i in xinapai:
        for k in i:
            xxx="    ".join("%s"% g for g in i)
            print()
            print(xxx)
        ff.writelines(xxx+'\n')
    ff.close()

