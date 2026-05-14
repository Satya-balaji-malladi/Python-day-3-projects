import random
guessing_number=random.randint(1,100)
attempt=0
num=int(input("Guess the number which i am imagining: "))
while(num!=guessing_number):
    if(num>guessing_number):
        print("your Number is high")
        attempt +=1
        num=int(input("Inko chance tisuko: "))
    elif(num<guessing_number):
        print("your number is low")
        attempt +=1
        num=int(input("Inko chance tisuko: "))
print("wahhh anna kanipetesav")
print("mothaniki ",attempt,"chances lo kanipettesav")
