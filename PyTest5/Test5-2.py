#定义一个函数，该函数可就收一个集合，用冒泡排序对该集合排序
def  dirct_choose_sort(list):
    for i in range(len(list)):
        for j in range(i,len(list)):
            if list[i]>list[j]:
                a=list[i]
                list[i]=list[j]
                list[j]=a
    return list
print(dirct_choose_sort([100,5,3,8,6,4,5,6,5,9,7,64,45,3]))