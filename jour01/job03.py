class Operation:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
       print(self.num1 + self.num2)

number = Operation(12, 3)
number.addition()
