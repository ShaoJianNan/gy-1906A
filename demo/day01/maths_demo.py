# 小明有20块钱，红双喜10块钱，玉溪25块钱，大前门5块钱   求出小明可以买那种烟
x=20
if(x)>=5:
    print(x,"元能买大前门")
if(x)>=10:
    print(x,"元能买红双喜")
if(x)>=25:
    print(x,"元能买玉溪")

#  成人票(18以上) 200 18岁以下的未成年人票100 60岁以上的老人票 150 小明今年18岁，去买票应该买那种票？
m=18
if(m>=60):
    print(m,"岁要买老人票 150元")
elif(m>=18):
    print(m,"岁要买成人票 200元")
else:
    print(m,"岁要买未成人票 100元")
