##增
#新增
#创建
a=[]
#列表最后新增单个值
a.append(1)
a.append("hasasf")
print(a)
#合并#print(a+b)打印出一个新的列表 = a.extend(b)
b=[1,2,3,4,5]
c=a+b
print(c)

print(a+b)
a.extend(b)
print(a)
##删
#根据下标删除某个元素
a.pop(2)
print(a)
#默认删除最后一个元素
a.pop()
print(a)
#清空一个列表 方法一a = [] 利用赋值 , 方法二a.clear() 直接将数据清空
# a = []
# print(a)
# a.clear()
# print(a)
##改
#根据下标修改某个元素的值
a[0]=8
a[1]="你好"
print(a)
#等价
# a[0],a[1] = 8,4
# print(a)
##查
#根据下标查某个元素
print(a[0])
print(a[1])
#遍历()借助循环
for b in a:
    print(b)
#截取
#截取部分数据
print(a[1:3])
#截取倒叙
print(a[::-1])
#隔一个取一个
print(a[::2])
print(len(a))
#成员判断
if("你好" in a):
    print("存在列表中")
else:
    print("不存在列表中")
