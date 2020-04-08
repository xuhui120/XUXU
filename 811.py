def load_word():    #     读取屏蔽词列表
    with open('words.txt') as f:
        global  bkword#定义全局变量
        bkword=[]
        line=f.readlines()
        for l in line:
            if l != " ":   #不等于空行，说明有内容，接着删除空格
                l=l.strip()
                bkword.append(l)




def wordfilter(text,symb="*"):
    for w in bkword:
        text=text.replace(w,symb*len(w))    #遍历屏蔽列表，把输入的这名话中的屏蔽词给他用*号替换了
    return text


load_word()
while True:
    t=input("输入文字（直接回车退出）：\n")
    if not t:   #如果T为空就跳出，表示没有输入字符串
        break
    print(wordfilter(t))    #T为输入的新的一句话，传给TEXT