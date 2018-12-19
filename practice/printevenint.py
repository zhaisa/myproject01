#打印列表中重复的数据，并删除
a=[1,2,4,2,4,5,6,5,7,8,9,0]
b=[]
for i in a:
    if i not in b:
        b.append(i)
    else:
        print("重复的数据：{}".format(i))
print(b)