# class Person:

#     eyes = 2
#     nose = 1
#     mouth = 1
#     ears = 2
#     arms = 2
#     legs = 2

#     def eat(self):
#         return "먹는다"
    
#     def sleep(self):
#         return "잔다"
    
#     def talk(self):
#         return "말을 한다"
    
# class student(Person):
#     def study(self):
#         return "공부한다"
    
#     def sleep(self):
#         return "학생은 6시간 잔다"
    
# sungwoo = student()

# class teacher(Person):
#     def teach(self):
#         return "가르친다"
    
#     def sleep(self):
#         return "선생님은 12시간 잔다"
    
# sungwoo = teacher()

# class writer(Person):
#     def write(self):
#         return "글을 쓴다"
    
#     def sleep(self):
#         return "작가는 8시간 잔다"
    
# sungwoo = writer()

# print(sungwoo.eyes)
# print(sungwoo.nose)
# print(sungwoo.mouth)
# print(sungwoo.ears)
# print(sungwoo.arms)
# print(sungwoo.legs)
# print(sungwoo.write())
# print(sungwoo.sleep())



# class Animal:
#     def __init__(self, name):
#         self.name = name


# class Dog(Animal):
#     def bark(self):
#         return f"멍멍! 강이지 이름은{self.name}"
    
# class Cat(Animal):
#     def bark(self):
#         return f"야옹! 고양이 이름은{self.name}"

# class tiger(Animal):
#     def bark(self):
#         return f"어흥! 호랑이 이름은{self.name}"
    
# my_dog = Dog("Buddy")

# my_cat = Cat("Miles")

# my_tiger = tiger("Tony")

# def animal_sound(animal):
#     print(animal.bark())

# animal_sound(my_dog)
# animal_sound(my_cat)
# animal_sound(my_tiger)


# 상속 super() 사용하기 : 
#부모클래스의 내용을 가져와서 자식클래스에서 사용할 수 있게 해줌

# class Person:
    
#     def __init__(self):
#         print("Person __init__")
#         self.hello = "안녕하세요"
#         self.contury = "대한민국"

# class Pesron_english(Person):

#     def __init__(self):
#         print("Person_english __init__")
#         super().__init__()
#         self.hello = "Hello"

# class Pesron_japanese(Person):

#     def __init__(self):
#         print("Person_english __init__")
#         super().__init__()
#         self.hello = "곤니찌와"

# class Pesron_chinese(Person):

#     def __init__(self):
#         print("Person_english __init__")
#         super().__init__()
#         self.hello = "니하오마"

# jay = Person()

# john = Pesron_english()

# rai = Pesron_japanese()

# jane = Pesron_chinese()

# print(john.hello)
# print(john.contury)
# print(john.hello)
# print(rai.hello)
# print(jane.hello)


# 클래스 메서드 오버라이딩 오버로딩 개념 이해 
# 오버라이딩 : 부모 클래스의 메서드를 자식 클래스에서 재정의 하는 것
# 오버로딩: 같은 이름의 메서드를 다른 파라메터로 여러개 정의하는 것

# class Person:
#     def greeting(self):
#         print("안녕하세요")

# class Student(Person):
#     def greeting(self):
#         super().greeting()
#         print("안녕하세요. 저는 학생입니다.")


# james = Person()
# james.greeting()

# james = Student()
# james.greeting()

# # 오버로딩 : 같은 이름의 메서드를 다른 파라메터로 여러개 정의하는 것
# class Calculator:
#     def add(self, a, b):
#         return a + b

#     def add(self, a, b, c):
#         return a + b + c
    
#     # def add(self, a, b, c, d):
#     #     return a + b + c + d

#     def add(self,*args):
#         return sum(args)

# # 오버라이딩 : 부모 클래스의 메서드를 자식 클래스에서 재정의 하는 것
# class AdvancedCalculator(Calculator):
#     def add(self, a, b):
#         return a + b + 10

#     def multiply(self, a, b):
#         return a * b

# basic_calc = Calculator()
# # print(basic_calc.add(2, 3))  # Output: 5
# # print(basic_calc.add(2, 3, 4))  # Output: 9
# print(basic_calc.add(2, 3, 4, 5))  # Output: 14

# advanced_calc = AdvancedCalculator()
# print(advanced_calc.add(2, 3))  # Output: 15
# print(advanced_calc.multiply(2, 3))  # Output: 6

# 다중상속 : 여러 부모 클래스로부터 상속을 받는 것

# class person:
#     def greeting(self):
#         print("안녕하세요")

# class university:
#     def manage_credit(self):
#         print("학점 관리")

# class undergraduate(person, university):
#     def study(self):
#         print("공부하기")

# james = undergraduate()
# james.greeting()
# james.manage_credit()
# james.study()

# 추상클래스 : 
# 메서드의 목록만 가진 클래스이며 상속받는 클래스에서 메서드 구현을 강제하기 위해 사용

# from abc import *

# class StudentBase(metaclass=ABCMeta):
#     @abstractclassmethod
#     def study(self):
#         pass

#     @abstractclassmethod
#     def go_to_school(self):
#         pass

# class Student(StudentBase):
#     def study(self):
#         print("공부하기")

#     def go_to_school(self):
#         print("학교가기")


# james = Student()
# james.study()




