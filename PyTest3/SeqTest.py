#生成10个随机大写字符写入列表
import null as null

my_list = []

import  random
for  i  in  range(10):
  n = random.randint(65,91)
  my_list.append(chr(n))
print(my_list)

#2
my_list = [chr(random.randint(65,91))  for  i  in  range(10)]
print(my_list)

from  numpy  import *
for  i  in  random.randint(65, 90, [10,1]):
   print(type(i))
print(my_list)

#列表去重
my_list = [random.randint(20,30) for  i  in range(15)]
print(my_list)
#普通遍历、判断
new_list = []
for  y   in  my_list:
   if  y not  in  new_list:
      new_list.append(y)
print(new_list)
#使用set集合
new_set_list = list(set(my_list))
print(new_set_list)

#使用itertools
import  itertools
my_list.sort()
new_my_list = []
key_value = itertools.groupby(my_list)
for  k,v  in  key_value:
 new_my_list.append(k)
print(new_my_list)





