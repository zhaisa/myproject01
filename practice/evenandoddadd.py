#编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
def even(n):
    s=0.0
    for i in range(2,n+1,2):
        s +=1.0/i
    return s
def odd(n):
    s=0.0
    for i in  range(1,n+1,2):
        s +=1.0/i
    return s
def dcall(fp,n):
    s = fp(n)
    return s

if __name__=='__main__':
    aa=int(input("请输入数字："))
    if aa % 2==0:
        sum=dcall(even,aa)
    else:
        sum=dcall(odd,aa)
    print(sum)