class Dog ():
    def __init__ (self,name,age,tricks) :
        self.name = name
        self.age = age
        self.tricks = tricks
    
    def bark (self) :
        print(f"{self.name}가 짖고 있습니다.")
    
    def show_tricks (self) :
        tricks = ",".join(self.tricks)
        print(f"{self.name}의 장기는 {tricks}")  
         
dog1 = Dog("바둑이",3,["뒹굴기","달리기"])
dog2 = Dog("멍멍이",5,["먹기"])

dog1.bark()
dog1.show_tricks()
dog2.bark()
dog2.show_tricks()