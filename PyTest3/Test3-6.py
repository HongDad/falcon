
#
my_dict = {}
for  i  in  range(5):
    key = input("请输入一个大写字母：")
    value = my_dict.get(key)
    if value == None:
        my_dict.update({key:1})
    else:
        my_dict.update({key:value+1})
print(my_dict)