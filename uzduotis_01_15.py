# Create a class that has 2 static methods that
# take in temperature measurements in Kelvins and return
# temperature transformed to Celsius and Fahrenheit.

# class Temperature:
#     def __init__(self, temperature):
#         self.temperature = temperature
#     @staticmethod
#     def celsiush_to_kelvins(temperature):
#         return temperature + 273
#
#     @staticmethod
#     def celsiush_to_fahrenheit(temperature):
#         return (9*temperature)/5 + 32
#
#
# print(Temperature.celsiush_to_fahrenheit(1))
# print(Temperature.celsiush_to_kelvins(1))

# Create a class that would take at least five imperial
# system measurements and would transform with the help
# of static methods to metric system units.
# --------------------------------------------------------------------------------

# class ImperialSystem:
#     def __init__(self, meter, liter, kilometer, kilogram):
#         self.meter = meter
#         self.kilometer = kilometer
#         self.liter = liter
#         self.kilogram = kilogram
#     @staticmethod
#     def metr_to_inch(meter):
#         return meter * 0.62137119
#
#     @staticmethod
#     def kilometer_to_mile(kilometer):
#         return kilometer / 0.0254
#
#     @staticmethod
#     def liter_to_gallone(liter):
#         return liter * 0.2641720524
#
#     @staticmethod
#     def kilogram_to_pound(kilogram):
#         return kilogram * 2.20462262
#
# print(ImperialSystem.metr_to_inch(1))
# print(ImperialSystem.kilometer_to_mile(2))
# print(ImperialSystem.liter_to_gallone(3))
# print(ImperialSystem.kilogram_to_pound(4))
# ------------------------------------------------------------------------------

# class TimeToSecond:
#
#     @staticmethod
#     def calculating_seconds(time):
#         x = ((int(time[:2]) *3600)+(int(time[3:5])*60) + int(time[6:]))
#         return x
#
#
#
# print(TimeToSecond.calculating_seconds("00:01:01"))
# ------------------------------------------------------------------------------

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @staticmethod
    def calculate_payroll(employees):
        sum = 0
        for employee in employees:
            sum += employee.salary
        return sum



employees = [Employee('Petras', 100), Employee('Justas',200)]
print(Employee.calculate_payroll(employees))
