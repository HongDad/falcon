#将n个随机数放入列表
NUM = int(input("请输入一个整数："))
import  random
my_list = []
for i in range(NUM):
    my_list.append(random.randint(0,100*NUM))
print(my_list)


#将n个随机奇数放入列表
my_list = []
for i in range(NUM):
   a =  random.randint(0, 100 * NUM)
   if a % 2 == 1:
       my_list.append(a)
   else:
       my_list.append(a+1)
print(my_list)


#将n个随机大写字母放入列表
my_list =[]
for i in range(NUM):
   my_list.append(chr(random.randint(65, 90)))
print(my_list)