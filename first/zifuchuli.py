'''
按照扑克牌的规则，现在有6张牌，只要5张
黑桃（S）红桃（H）方块（D）梅花（C）
牌：2.3.4.5.6.7.8.9.10.J.Q.K.A
数据库存的是下面格式的数据，写脚本验证满足3带2的牌型
[''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]
["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]
'''
shuzi  = []
zidian = {}
str = '''["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]'''
str = str.replace("''",'"')
str = str[2:-2]
print(str)
str_li = str.split('" , "')
print(str_li)
b_2 = False
b_3 = False
for i in str_li:
   weiba = i[1:]
   shuzi.append(weiba)
   if(weiba not in zidian):
       zidian[weiba]=1
   else:
       zidian[weiba]+=1
for key in zidian:
    if(zidian[key]==3):
        b_3 = True
    if(zidian[key]==2):
        b_2 = True
if(b_2 and b_3):
    print("可以3带2")
else:
    print("不可以")
print(shuzi)

