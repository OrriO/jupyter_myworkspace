class Person(object):
	"""人的类"""
	def __init__(self, name):
		super(Person, self).__init__()
		self.name = name

	def anzhuang_zidan(self, dan_jia_temp, zi_dan_temp):
		"""把子弹装到弹夹中"""
		
		#弹夹.保存子弹(子弹)
		dan_jia_temp.baocun_zidan(zi_dan_temp)

	def anzhuang_danjia(self, gun_temp, dan_jia_temp):
		"""把弹夹安装到枪中"""

		#枪.保存弹夹(弹夹)
		gun_temp.baocun_danjia(dan_jia_temp)

class Gun(object):
	"""枪类"""
	def __init__(self, name):
		super(Gun, self).__init__()
		self.name = name#用来记录枪的类型
		self.danjia = None#用来记录弹夹对象的引用

	def baocun_danjia(self, dan_jia_temp):
		"""用一个属性来保存这个弹夹对象的引用"""
		self.danjia = dan_jia_temp

class Danjia(object):
	"""弹夹类"""
	def __init__(self, max_num):
		super(Danjia, self).__init__()
		self.max_num = max_num#用来记录弹夹的最大容量
		self.zidan_list = []#用来记录所有的子弹的引用

	def baocun_zidan(self, zi_dan_temp):
		"""将这颗子弹保存"""
		self.zidan_list.append(zi_dan_temp)

class Zidan(object):
	"""子弹类"""
	def __init__(self, sha_shang_li):
		super(Zidan, self).__init__()
		self.sha_shang_li = sha_shang_li#这颗子弹的威力
		

def main():
	"""用来控制整个程序的流程"""

	#1. 创建老王对象
	laowang = Person("老王")

	#2. 创建一个枪对象
	ak47 = Gun("AK47")

	#3. 创建一个弹夹对象
	dan_jia = Danjia(20)

	#4. 创建一些子弹
	zi_dan = Zidan(10)

	#5. 老王把子弹安装到弹夹中
	#老王.安装子弹到弹夹中(弹夹，子弹)
	laowang.anzhuang_zidan(dan_jia, zi_dan)

	#6. 老王把弹夹安装到枪中
	#老王.安装弹夹到枪中(枪，弹夹)
	laowang.anzhuang_danjia(ak47, dan_jia)

	#7. 老王拿枪

	#8. 创建一个敌人

	#9. 老王开枪打敌人

if __name__ == '__main__':
	main()