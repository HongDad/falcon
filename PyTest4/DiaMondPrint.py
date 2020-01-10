#控制台打印菱形
'''
    *
   * *             中间空格1、3、5
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
'''

N = int(input("请输入你要打印的菱形大小，请输入一个整数："))
for i in  range(2*N-1):
   if i < N :
     if i == 0:
         print((N - 1 - i) * ' ' + '*')
     else:
         print((N-1-i)*' '+'*',end='')
         print((2*i - 1) * ' '+'*')
   else:
      if i == 2*(N-1):
          print(((i + 1) - N) * ' ' + '*', end='')
      else:
         print(((i+1) - N) * ' ' + '*',end='')
         print((4*N-2*i-5) * ' ' + '*')




