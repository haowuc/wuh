# 小明有20块钱，红双喜10块钱，玉溪25块钱，大前门5块钱   求出小明可以买那种烟
print("请输入您的姓名：")
name = input()
print("请输入您的年龄：")
age=input()
print("请交钱：")
money = input()

if(int(money) >5 and int(money) < 25):
    print(name,"您有",money,"元可以买红双喜")
elif(int(money)==5):
    print(name,"您有",money, "元可以买红大前门")
elif(int(money)>=25):
    print(name,"您有",money,money, "元可以买玉溪")
else:
    print(name,"你就",money,"块钱，想啥好事儿呢，捡烟头去吧")

