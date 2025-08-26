'''
You will build a class to manage personal health information.

Some data must be protected (not directly accessible).

Users should only interact with the object through public methods.

This demonstrates the concept of Encapsulation: hiding details and providing controlled access.

🚀 Requirements

Create a class HealthProfile with:

__weight (in kg) → private

__height (in meters) → private

name → public

Add safe setter/getter methods:

set_weight(new_weight) → only allow values > 0

set_height(new_height) → only allow values > 0

get_weight(), get_height()

Add a method calculate_bmi()

Formula: BMI = weight / (height ** 2)

Return a string category:

<18.5: “Underweight”

18.5–24.9: “Normal”

25–29.9: “Overweight”

>=30: “Obese”

Override __repr__ so that printing the object shows something like:
HealthProfile(name='Alice', weight=55kg, height=1.65m, BMI=20.2 Normal)
'''