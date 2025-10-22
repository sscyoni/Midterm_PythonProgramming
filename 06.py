class Bank () : 
    def __init__ (self,name,number,balance):
        self.name = name
        self.number = number
        self.balance = balance
        
    def deposit (self,aa) :
        self.balance += aa  #여기서 다른 코드 작성 안해도 위에 생성자함수에서도 이 값이 그대로 반영됨
  
        
    def withdraw(self,p):
        if self.balance >= p :
            self.balance -= p  #실제 인출금액 차감하기
            print("인출성공", "인출후 잔고",self.balance - p)
        else :
            print("잔액부족")
                
                
account = Bank("Kim","123456789",1000)
print("초기잔고:",account.balance)

account.deposit(500)
print("저축후 잔고:",account.balance)
account.withdraw(200)
print("인출후 잔고:",account.balance)
account.withdraw(1500)