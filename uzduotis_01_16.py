class MyClass:
    @classmethod
    def factorial(cls, number):
        if number == 0:
            return 1
        elif number < 0:
            return 'Number must be a non-negative.'
        else:
            return number * cls.factorial(number-1)

print(MyClass.factorial(3))