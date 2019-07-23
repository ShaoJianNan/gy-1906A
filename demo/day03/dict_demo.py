
# 字典的特性:
# 1,字典中key是唯一的 ,同一个key只显示最后赋值的值
#  2,key是不可变得
# 元祖(1,2,3,4)可以作为key,但是(1,[23])不可以作为一个key
#访问value只能通过key

##增
#创建
a={}
#新增
a["姓名"]="邵建南"
a["性别"]="男"
a["手机号"]=1896521520
a[1,2,3]=356
print(a)
#改
a["姓名"]="大宝剑"
print(a)


#删pop的参数只能为key
# a.pop((1,2,3))
# print(a)
#清空字典
# a.clear()
# print(a)

#查
#根据key查看value
print(a["姓名"])
#遍历字典   借助循环
for key in a:
    print(a[key])
##字典合并
#把一个字典,合并到另一个字典中
c={"大鸡巨":"大蜘蛛"}
d={"小脑斧":"小老虎"}
c.update(d)
print(c)
#把两个字典合并成一个新的字典
print(dict(c,**d))
#成员判断(key)
if("大鸡巨" in c):
    print("存在字典中")
else:
    print("不存在字典中")
print(len(c))
