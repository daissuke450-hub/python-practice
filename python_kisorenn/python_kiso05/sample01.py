class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name}がワンワン吠えた！")

dog1 = Dog("ポチ", 3)
dog1.bark()
print(dog1.name, "は", dog1.age, "歳です")
