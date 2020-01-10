#列表推导式的循环控制不是循环，而是前面的表达式
#循环几次，前面的表达式就执行几次，表达式的结果将作为列表的元素
#对于列表推导式而言，for循环执行几次，那么列表就有几个元素


r = [(i,i ** i)   for  i  in  range(20)]
print(r)

for i  in  range(100):
    print(i)
    #break 提前跳出循环,continue忽略本次
    if i >  20:
       continue
    print('循环第%d次：' % i)
else:
 print("循环结束")