# for i in [1,60,30,90,100,20,70,59,69,71,80,84]:
#     score = 0 # 0为不及格、1为及格、2为良好、3为优秀
#     if(i<60):
#        print(i,"是不及格")
#     elif(i>=60 and i<70):
#         print(i, "是及格")
#     elif (i >= 70 and i < 80):
#         print(i, "是良好")
#     else:
#         score = 1
#         print(i, "是优秀")
# 成绩0-59不及格，60-70及格 70-80 良好 80以上是优秀    [90,100,81,84]判断下改组成绩是否全部都是优秀
li=[90,54,100,81,84,170,154,77]
count=0
count1=0
for i in li:
    if(i >= 80):
        count=count+1
    else:
        count1 = count1 + 1
if(count==len(li)):
    print("都为优秀")
else:
    print("有",count1,"个人拖后腿了！")