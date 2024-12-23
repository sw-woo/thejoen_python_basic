#파이썬 데코레이터(decorator) 개념 이해하기
#데코레이터는 함수를 수정하지 않고 기능을 추가하거나 수정할 때 사용하는 기법이다.
#데코레이터는 함수를 인자로 받아 다른 함수를 반환하는 함수이다.
#데코레이터는 @데코레이터 함수명으로 사용한다.

# def hello():
#     print("hello 함수 시작")
#     print("hello")
#     print("hello 함수 끝")

# def world():
#     print("world 함수 시작")
#     print("world")
#     print("world 함수 끝")


# hello()
# world()


# def trace(func):
#     def wrapper():
#         print(func.__name__, "함수 시작")
#         func() #인자로 받은 함수를 호출 hello or world
#         print(func.__name__,"함수 끝")
#     return wrapper

# @trace
# def hello():
#     print("hello")

# @trace
# def world():
#     print("world")

# hello()
# world()

# trace_hello = trace(hello)
# trace_hello()

# trace_world = trace(world)
# trace_world()

# 클래스 메서드와 정적 메서드 사용해보기
#클래스 메서드는 클래스 변수를 사용할 때 사용한다.
#클래스 메서드는 @classmethod 데코레이터를 사용한다.
#클래스 메서드는 첫 번째 인자로 cls를 사용한다.
#정적 메서드는 클래스 변수를 사용하지 않을 때 사용한다.
#정적 메서드는 @staticmethod 데코레이터를 사용한다.
#정적 메서드는 첫 번째 인자로 cls를 사용하지 않는다.

# class Dog: 
#     species = "말티즈" #클래스 변수 

#     @classmethod
#     def get_species(cls):
#         return cls.species
    
#     @staticmethod
#     def make_sound():
#         return "멍멍"
    
# my_dog = Dog()

# print(my_dog.get_species())
# print(my_dog.make_sound())
# print(Dog.get_species())
# print(Dog.make_sound())



#클래스 프로퍼티 사용해보기
#클래스 프로퍼티는 클래스 속성에 대해 
#getter와 setter를 사용하여 접근할 수 있게 해준다.

# class Dog:
#     def __init__(self,name):
#         self.__name = name # 비공식 속성 (private)
    
#     @property
#     def name(self):
#         return self.__name
    
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name

# my_dog = Dog("Jindo")
# print(my_dog.name)
# my_dog.name = "Max"
# print(my_dog.name)



# @dataclass 데코레이터 사용해보기 
# 기본적인 메서드를 자동으로 제공받습니다. 데이터 클래스는 많은 양의 데이터를 다룰 때 유용하며, 
# 코드의 간결함과 가독성을 높이는 데 기여합니다.

from dataclasses import dataclass 

@dataclass
class Dog:
    name: str
    age: int
    breed: str

@dataclass
class Person:
    name: str
    age: int

# Create instances of Dog and Person
my_dog = Dog("Max", 3, "Labrador")
my_person = Person("John", 30)

# Access and modify attributes
print(my_dog.name)  # Output: Max
print(my_person.age)  # Output: 30

my_dog.age = 4
my_person.name = "Jane"

print(my_dog.age)  # Output: 4
print(my_person.name)  # Output: Jane






