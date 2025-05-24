# -- coding: utf-8 --
# This script prints out personal information about an individual.


my_name = "John Doe"
my_age = 30
my_height = 175.5  # in centimeters
my_weight = 70.0  # in kilograms
my_eyes = "Brown"
my_hair = "Black"
my_teeth = "White"
my_favorite_color = "Blue"

print("Lets talk about %r." % my_name)
print("He's %d years old." % my_age)
print("He's %.1f centimeters tall." % my_height)
print("He's %.1f kilograms heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)
 
# conveting inches to centimeters and pounds to kilograms
inches_to_cm = 2.54
pounds_to_kg = 0.45359237
i = 70  # height in inches
p = 150  # weight in pounds
print("height in cm = %.1f cm." % (i * inches_to_cm))
print("weight in kg = %.1f kg." % (p * pounds_to_kg))