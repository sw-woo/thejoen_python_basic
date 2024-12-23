#파이썬 클래스 사용하기 : 객체지향 프로그래밍 


# class Dog:
#     pass

# class Dog:
#     species = "Canis familiaris" # 클래스 변수
#     #클래스 변수: 객체의 속성을 공유하는데 사용한다. 
#     #객체를 생성할 때마다 같은 값을 가진다. 
#     def __init__ (self, name, age):
#         self.name = name
#         self.age = age
    
#     def bark(self):
#         return f"{self.name}"

# my_dog = Dog("Buddy",3)
# my_dog2 = Dog("Miles", 4)

# print(my_dog.bark())
# print(my_dog.species)

# print(my_dog2.bark())
# print(my_dog.species)

# print(my_dog2.name)
# print(my_dog2.age)
# print(type(my_dog2))



class warrior:
    strength =  30
    agility = 20
    intellect = 10
    energy = 30

    level = 1
    
    def __init__(self, name):
        self.name = name

    def attack(self):
        return "공격!"
    
    def level_up(self):
        self.level += 1
        self.strength +=2
        self.agility +=3
        self.intellect +=1
        self.energy +=5
    
sungwoo = warrior("sungwoo-전사1")
sungwoo2 = warrior("sungwoo-전사2")

print(sungwoo.name)
print(sungwoo.strength)
print(sungwoo.agility)
print(sungwoo.intellect)
print(sungwoo.energy)

print(sungwoo.attack())
sungwoo.level_up()

print(sungwoo.name)
print(sungwoo.strength)
print(sungwoo.agility)
print(sungwoo.intellect)
print(sungwoo.energy)

print(sungwoo2.name)
print(sungwoo2.strength)
print(sungwoo2.agility)
print(sungwoo2.intellect)
print(sungwoo2.energy)

print(warrior.__dict__)


