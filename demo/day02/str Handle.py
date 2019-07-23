#字符串切片splist

# a="亲成我上马"
# print(a[0:1])
# print(a[0:1])
# print(a[2:3])
# print(a[::-1])

# 按照扑克牌的规则，现在有6张牌，只要5张
# 黑桃（S）红桃（H）方块（D）梅花（C）
# 牌：2.3.4.5.6.7.8.9.10.J.Q.K.A
# 数据库存的是下面格式的数据，写脚本验证满足3带2的牌型
# [''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
# ["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]
# ["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]

# replace    替换
# print(len(str))查询字符串长度
#def是方法关键字,juge_3_2是方法名,,可以自定义,不能以数字开头:()参数列表:
def juge_3_2():
    # 第一步：统一符号  对字符串的处理，用replace（）
    b=input("请在下方输入手中的牌型")
    b=b.replace("''",'"')
    # print(b)
    # 第二步：去掉中括号 字符串截取  [::]
    b=b[2:-2]
    # print(b)
    # 第三步：变成list  字符串切片  .split（） 新建一个list变量
    b_li=b.split('" , "')
    # print(b_li)
    # 第四步：取出后面的数字  循环遍历取出list里面的每个值，对这个值进行截取
    c_dict={}
    for d in b_li:
        d_key=d[1:]
        # print(d_key)
    # 第五步：统计相同的数字个数  用字典去统计
        if (d_key in c_dict):
            c_dict[d_key]+=1
        else:
            c_dict[d_key] =1
    # print(c_dict)
    # 第六步：判断数据中有没有同时存在三个相同数字和两个相同数字  if判断
    v1=0# 如果key对应的数值有3的 v1 = 1，如果没有则为0
    v2=0# 如果key对应的数值有2的 v2 = 1，如果没有则为0
    for key in c_dict:
        if(c_dict[key]==3):
            v1=1
        if(c_dict[key]==2):
            v2=1
    if (v1==1 and v2==1):
        print("这把牌可以出三带二")
    else:
        print("这把牌凉凉")

#open 是 python提供的一个内置函数:作用就是打开一个文件.参数一:文件路径;参数二:文件的打开模式 r只读,W可写入,a可读可写
#with open() as f 类似于 f = open ()他可以在with 的代码执行出问题的时候,做一些资源释放的工作
with open("E:\\softwaredate\\daydayupup\\gy-1906A\\demo\\day04\\cards.txt",'r') as f:
    #读文件.readlines()作用就是把文件中整个内容按行读取出来,存到一个list中;read()把整个文件的内容读取出来,存到一个字符串中
    lines = f.readlines()
    #for循环遍历这个列表
    for lines in lines:
         lines=lines.replace()
