#
num = input("请输入多个整数，中间用空格分开：")
num2 = num.split(" ")
num3 = []
for i in num2:
   if i != '':
     num3.append((i,hash(i)))
print(tuple(num3))
