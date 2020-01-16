#数字转人民币读法
'''
将浮点数进行分解，把整数部分和小数部分进行分解
'''
def  divid(num):
    int_num = int(num)
    float_num = (num-int_num)*100
    return (int_num,float_num)
han_list = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
unit_list = ['', '拾', '佰', '千']

def  int_num_str(num):
    str = ""
    len_num = len(repr(num))
    for  i in range(len_num):
      int_num_char = repr(num)[i]
      if (len_num <5 ):
          str += han_list[int(int_num_char)]
          if int(int_num_char) != 0:
            str += unit_list[len_num-1-i]
      elif (len_num < 9):
        if ((len_num-i) < 5 ):
            str += han_list[int(int_num_char)]
            if int(int_num_char) != 0:
                str += unit_list[len_num - 1 - i]
        else :
            str += han_list[int(int_num_char)]
            if int(int_num_char) != 0:
              str += unit_list[len_num-i-5]
        if len_num-i==5:
            str += "万"
    if int(repr(num)[-1]) == 0:
      str = str.replace(str[-1],"")
    return str
print(int_num_str(100000))




