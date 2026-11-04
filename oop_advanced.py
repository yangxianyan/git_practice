# 1.定义一个父类（基类）：动物
class Animal:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def eat(self):
		print(f"{self.name}正在吧唧吧唧吃东西...")

	def speak(self):
		print("动物发出来某种叫声")

# 2.定义子类：狗（继承至Animal）
class Dog(Animal):
	# 重写父类的speak
	def speak(self):
		print(f"{self.name}汪汪叫！")

# 3.定义子类：猫（继承至Animal）
class Cat(Animal):
	#重写父类的speak
	def speak(self):
		print(f"{self.name}喵喵叫！")

# 4.定义子类：鸟（继承至Animal）
class Bird(Animal):
	def speak(self):
		print(f"{self.name}叽叽喳喳！")


#==============测试区域=================
if __name__ == "__main__":
	#创建三个不同子类的实例（对象）
	dog = Dog("旺财", 3)
	cat = Cat("巾巾", 2)
	bird = Bird("皮皮", 1)

	#验证继承：子类没有定义eat的方法，但是可以直接用父类的
	print("---测试继承（代码复用）---")
	dog.eat()
	cat.eat()
	bird.eat()

	#验证多态
	print("\n---测试多态（同一个指令，不同表现）---")
	pets = [dog, cat, bird]

	for pet in pets:
		pet.speak()
