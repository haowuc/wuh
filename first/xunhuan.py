# count = 0
# li = []
# for i in range(100):
#     if(i%2==1):
#         count = count+1
#         li.append(i)
#         print("第",count,"个奇数是",i)
# print(li)
#
#
# for a in range(100):
#     b=2
#     for c in range(2,a+1):
#         if(a%b==0):
#             break
#         b = b +1
#     if(b==a):
#         print(a)
# "01010010001110001001001010101010010101" 计算下几个0 几个1
# a = "01010010001110001001001010101010010101"
# x = 0
# y = 0
# for i in a:
#     if(i=="0"):
#         x+=1
#     else:
#         y+=1
# print("有",x,"个0，有",y,"个1")

#求和1+2+3.....+99+100
# sum=0
# for i in range(1,101):
#     sum = sum +i
# print(sum)

a=1
sum=0
while a<=100:
    sum=sum+a
    a=a+1
print(sum)