#两个数相加
def sum(a,b):
    print(a,"+",b,"=",a+b)
    return a+b
sum(5,6)
sum(sum(5,6),7)

#两个数相减
def cha(a,b):
    print(a,"-",b,"=",a-b)
    return a-b
cha(-1,-6)
cha(cha(-1,-6),7)

#两个数相乘
def ji (a,b):
    print(a,"X",b,"=",a*b)
    return a*b
ji(5,6)
ji(ji(5,6),7)
#两个数相除

def shang (a,b):
    if (b!=0):
        print(a,"÷",b,"=",a/b)
        return a/b
    else:
        print("除数无意义")

shang(5,1)
shang(shang(5,1),5)

def meili(a,b,c):
    return "{na}独自{vt}着{sth}" .format(na=a,vt=b,sth=c)
print(meili("富婆","吃","大龙虾"))

def buy_coffees(cash=100,cups=1):
    #去咖啡店
    print("富婆去买肾")
    #告诉服务员要几杯咖啡
    cup_num = cups
    print("告诉服务员要",cup_num,"个肾")
    #服务员告诉你要多少钱
    print("服务员告诉你要",cup_num*30,"万元")
    #你给服务员多少钱
    money = cash
    print("富婆给服务员",money,"万元")
    #服务员找零，给你咖啡
    print("服务员找零",money-cup_num*30,"万元，给你",cup_num,"个肾")
buy_coffees()
buy_coffees(1500,50)


#args接收单个数据的形式,kwargs接收成对的数据

def div(a,b):
        f=None
        try:
            f=open("E:\\softwaredate\\daydayupup\\gy-1906A\\demo\\day04\\two number")
            print("文件打开成功")
        except:
            print("文件打开失败")
        finally:
            print("不管任何情况,都会执行")