#
NUM = int(input("请输入你要输入字符穿的数量："))
my_list = []
for  i  in range(NUM):
    my_list.append(input("请输入你要输入第"+repr(i+1)+"个字符串："))
print(list(set(my_list)))