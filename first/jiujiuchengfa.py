# for a in range(1,10):
#     for b in range(a):
#         print(a,"*",(b+1),"=",a*(b+1),'\t',end = "")
#     print()
# print()
# for i in range(9,0,-1):
#     for j in range(i,0,-1):
#         print(i,"*",j,"=",i*j,'\t',end = "")
#     print()

m=int(input())
a = 0  # a为0的时候是素数，为1的时候是和数
for i in range(2,m):
    if(m%i == 0):
        a=1
if(a==0):
    print(m, "是个素数")
else:
    print(m, "是个和数")