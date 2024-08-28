'''

Write a python program using function to convert Celsius to Fahrenheit.

Formula for Fahrenheit to Calsius is:
f = (c * 9/5) + 32
OR
c = 5 * (f - 32)/9

'''

def C_to_F(Calcius):
    fahreheit = (Calcius * 9/5) + 32
    return fahreheit

# Get temperature in calcius from user
celsius_temp = int(input("Enter temperature in Calcius: "))

fahrenheit_temp = C_to_F(celsius_temp)

print(f"{celsius_temp}°C in Calcius is equal to {fahrenheit_temp}°C in Fahrenheit")
