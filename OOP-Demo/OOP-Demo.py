# Exercise Name:
# 	09-OOP-Demo
# Description:
# 	Create a class and demonstrate how @property decorator is used


class BMI_Calculator:
    def __init__(self, weight, height):
        self._weight = weight
        self._height = height / 100

    @property
    def bmi(self):
        return self._weight / (self._height ** 2)

    @property
    def category(self):
        bmi_value = self.bmi
        if bmi_value < 18.5:
            return "Underweight"
        elif 18.5 <= bmi_value < 24.9:
            return "Normal weight"
        elif 25 <= bmi_value < 29.9:
            return "Overweight"
        else:
            return "Obese"

weight = float(input("\nEnter your weight in kg: "))
height = float(input("Enter your height in cm: "))

bmi_calculator = BMI_Calculator(weight, height)

print("Your BMI is:", bmi_calculator.bmi)
print("BMI Category:", bmi_calculator.category, "\n")