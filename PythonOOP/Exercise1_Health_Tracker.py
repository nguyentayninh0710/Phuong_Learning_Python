'''
You will build a class to manage personal health information.

Some data must be protected (not directly accessible).

Users should only interact with the object through public methods.

This demonstrates the concept of Encapsulation: hiding details and providing controlled access.

🚀 Requirements

Create a class HealthProfile with:

__weight (in kg) → private              x

__height (in meters) → private          x

name → public                           x

Add safe setter/getter methods:

set_weight(new_weight) → only allow values > 0      x

set_height(new_height) → only allow values > 0      x

get_weight(), get_height()              x

Add a method calculate_bmi()        x

Formula: BMI = weight / (height ** 2)       x

Return a string category:   

<18.5: “Underweight”        x

18.5–24.9: “Normal”         x

25–29.9: “Overweight”       x

>=30: “Obese”               x

Override __repr__ so that printing the object shows something like:
HealthProfile(name='Alice', weight=55kg, height=1.65m, BMI=20.2 Normal)
'''
from __future__ import annotations

class HealthProfile: 
    def __init__(self, name: str, weight: float = 0.0, height: float = 0.0):
        self.__weight = float(weight)
        self.__height = float(height)
        self.name = name

    def set_weight(self, new_weight):
        if new_weight > 0:
            self.__weight = new_weight
        else:
            raise ValueError("Weight must be positive!")
        
    def get_weight(self):
        return self.__weight

    def set_height(self, new_height):
        if new_height > 0:
            self.__height = new_height
        else:
            raise ValueError("Height must be positive!")
        
    def get_height(self):
        return self.__height

    def calculate_bmi(self):
        bmi =  self.__weight / (self.__height ** 2)

        if bmi < 18.5:
            return (bmi, "Underweight")
        elif 18.5 <= bmi <= 24.9:
            return (bmi, "Normal")
        elif 25 <= bmi <= 29.9:
            return (bmi, "Overweight")
        else:
            return (bmi, "Obese")
        
    def __repr__(self):
        bmi, status =  self.calculate_bmi()
        return f"HealthProfile(name = {self.name}, weight = {self.__weight}kg, height = {self.__height}m, BMI = {bmi}, {status})"
    
hp = HealthProfile("Phuong", 100, 1.89)
print(hp)


