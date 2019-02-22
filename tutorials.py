# prompt = """
#     1. add
#     2. del
#     3. list
#     4. quit

# Enter the number : """

# number = 0
# while number !=4 :
#     print(prompt)
#     number = int(input())

# a=3
# b=4
# c=5

# def change(a, b):
#     a, b=4, 5
#     print(a,b)

# change(a,b)

# print(a,b)

class Fourcal() :

    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def sum(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        if(self.a>=self.b):
            return self.a/self.b
        else:
            return self.b/self.a

num1 = 3
num2 = 8

a = Fourcal(num1, num2)

print(a.sum(), a.sub(), a.mul(), a.div())
