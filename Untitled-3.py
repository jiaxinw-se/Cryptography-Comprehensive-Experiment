from cmath import sqrt


a=3131
b=3.321
c='注意%号的用法'
print('%s :\n a = %d,\n b = %f' % (c,a,b))

#f=int(input("请输入华氏度： "))
#c=(f-32)/1.8
#print(sheshiduw)

'''
x=int(input("请输入x的值：" ))
if x>1:
    print(3*x-5)
elif x>=-1 and x<=1:
    print(x+2)
else:
    print(5*x+3)'''
'''
score=int(input("请输入成绩： "))
if score>=90:
    print("A %d" % score)
elif score<90 and score>=80:
    print("B %d %d" % (score,score)
    )
'''
from math import sqrt
M  =  int(input("请输入一个素数："))
MAX=  int(sqrt(M))
for i in range(2,MAX+1):
    if M%i==0 :
        print("不是素数")
        break
print("素数")

for i in range(2,2):
    print(i)