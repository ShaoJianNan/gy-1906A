for a in range(52):
    print("爱你",a+1,"千遍")
#打印出100以内的奇数 取余为1的数
for b in range(100):
    if(b % 2)==1:
        print(b)
#九九乘法口诀表
#空格"\t"
#打印放在一行end=""


for c in range(1,10):
    for d in range(1,c+1):
        print(d,"X",c,"=",c*d,"\t",end="")
    print()

#100以内的质数
#break 中断循环.
for f in range(2,101):
    n = 2
    for e in range(2,f+1):
        if(f%n == 0):
            break
        n =n+1
    if(n==f):
        print(f)
# 输入一个年份，判断其是否为闰年 能被4整除而不能被100整除 能被400整除。


