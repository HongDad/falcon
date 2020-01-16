#超市控制系统
#1、添加 2、修改 3、删除 4、结算 5、超市商品列表 6、购物车列表
#定义仓库
responisty = dict()
#定义购物车列表
shop_list = []
#定义超市商品列表方法
def  show_goods():
   goods1 = ('1001', '炫迈',12)
   goods2 = ('1002', '显示器', 1134)
   goods3 = ('1003', '程序化广告', 134)
   goods4 = ('1004', '橙子', 6)
   goods5 = ('1005', '鼠标', 45)
   goods6 = ('1006', '键盘', 89)
   goods7 = ('1007', '椅子', 189)
   goods8 = ('1008', '抱枕', 334)
   goods9 = ('1009', '花盆', 34)
   #商品入库
   responisty[goods1[0]] = goods1
   responisty[goods2[0]] = goods2
   responisty[goods3[0]] = goods3
   responisty[goods4[0]] = goods4
   responisty[goods5[0]] = goods5
   responisty[goods6[0]] = goods6
   responisty[goods7[0]] = goods7
   responisty[goods8[0]] = goods8
   responisty[goods9[0]] = goods9
   return responisty
#购物车添加
def   add(key):
   shop_list.append(responisty[key])
   return shop_list


print(show_goods())
