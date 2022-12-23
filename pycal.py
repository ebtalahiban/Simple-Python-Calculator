
class PyCal:
    def __init__(self, name, num1, num2):
        self.name = name
        self.num1 = num1
        self.num2 = num2
        print(f"Welcome to PyCal, {self.name}! \nA mini calculator using Python")
        
    def getUserInput(self):
        try:
            self.num1 = int(input("Enter first value: "))
            self.num2 = int(input("Enter second value: "))
        except ValueError:
            print("Invalid input. Must be int\n")
    
    def add(self): 
        if not calc.getUserInput():
            result = int(self.num1)+int(self.num2)  
            print(f"Addition result: {result}") 
    def sub(self):
        if not calc.getUserInput():
            result = int(self.num1)-int(self.num2) 
            print(f"Subtraction result: {result}") 
    def mul(self):
        if not calc.getUserInput():
            result = int(self.num1)*int(self.num2) 
            print(f"Multiplication result: {result}") 
    def div(self):
        if not calc.getUserInput():
            try:
                result = int(self.num1)/int(self.num2)  
                print(f"Division result: {result}")  
            except ZeroDivisionError:
                print("Cannot be zero\n")    

name = input("Enter you name: ")
choice = ""
calc = PyCal(name, 0, 0)

while True:
    menu = " Menu \n a. Addition\n b. Subtraction\n c. Multiplication\n d. Division\n e. Quit"
    print(menu)
    choice = input("Choice: ")

    if not any(map(str.isdigit, choice)):
        if choice == "a" or choice == "A":
            calc.add()

        elif choice == "b" or choice == "B":
            calc.sub() 

        elif choice == "c" or choice == "C":
            calc.mul()

        elif choice == "d" or choice == "D":
            calc.div()

        elif choice == "e" or choice == "E":
            exit()

        else:
            print(f"{choice} is an invalid input\n")
            continue
    else:
        print(f"{choice} is an invalid input\n")
        continue
