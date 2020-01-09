#提示用户输入n个字符串，封装成元组，输入该元组乘以3的结果，输出该元组加上'fkjava','crazyit'

#提示用户输入n个字符串
NUM = 5
my_list=[]
for i in  range(NUM):
    my_list.append(input("请输入一个字符串："))
my_tuple=tuple(my_list)*3
my_tuple2=('fkjava','crazyit')
print(my_tuple+my_tuple2)
