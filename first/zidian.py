# a = {}
# a.update(name="wuhao")
# a['age']= 18
#
# a.update(phone=133888811111,email='wuhao@126.com')
# print(a)
# b = a.pop('email')
# print(b)
# del a['phone']
# print(a)

'''
按照扑克牌的规则，现在有6张牌，只要5张
黑桃（S）红桃（H）方块（D）梅花（C）
牌：2.3.4.5.6.7.8.9.10.J.Q.K.A
数据库存的是下面格式的数据，写脚本验证满足3带2的牌型
[''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]
["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]
'''

def juge_3_2(str):# 外部传入
    # 拿到数据
    # str = '''[''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']''' #(代码写死)
    # str = input("请输入牌型：")  #控制台输入
    # 处理数据
    print(str)
    str = str.replace("''",'"')
    # print(str)
    str = str[2:-2]
    # print(str)
    str_li = str.split('" , "')
    # print(str_li)
    dict_str={}
    for i in str_li:
        i_v = i[1:]
        if(i_v not in dict_str):
            dict_str[i_v] = 1
        else:
            dict_str[i_v]+=1
    # print(dict_str)
    b_2 = False
    b_3 = False
    for key in dict_str:
        if(dict_str[key] == 3):
            b_3 = True
        if(dict_str[key]==2):
            b_2 = True
    if(b_2 and b_3):
        print("可以三带二")
    else:
        print("不可以")
i = ''
with open("D:\\softwareData\\study_wh\\first\\data_pai") as f:
    data_li = f.readlines()
for line in data_li:
    line = line.replace("\n","")
    juge_3_2(line)