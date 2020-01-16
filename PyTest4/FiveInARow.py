#五子棋,剩余问题：超出棋盘，重复落子，电脑出棋，胜利
#1、定义一个棋盘的大小
SIZE = 15
#2、定义嵌套数组
def origin_array():
   array = [['+'] * SIZE]
   for i in range(SIZE -1):
     array += [['+'] * SIZE]
   return array
#定义输入五子棋的位置
def  input_num(array,my_input):
  array[int(my_input[0])][int(my_input[1])] = '●'
  return array
#控制台打印
def  output_num(array):
  for i in range(SIZE):
    for j in range(SIZE):
        print(array[i][j],end=' ')
    print()

#定义输入五子棋的位置
my_input = input('请输入你要下的坐标(x,y)：').split(',')
array = origin_array()
while  my_input != None:
    output_num(input_num(array,my_input))
    my_input = input('请输入你要下的坐标(x,y)：').split(',')
