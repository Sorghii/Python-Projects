from time import sleep
from os import system
# Introduction and User Interaction
system('cls')
print('Welcome to the BMI Calculator!')
sleep(1)
print('This tool helps you calculate your Body Mass Index (BMI) based on your weight and height. But, please keep in mind that')
print('The BMI calculation only considers weight and height, but it does not distinguish between muscle mass, body fat, or age.')
print('As a result, people with a lot of muscle mass (like athletes or bodybuilders) can have the same BMI as obese individuals, even though their body compositions are quite different.')
print('Similarly, age influences BMI categories, but it is not considered in this calculation.')
print('BMI is a general reference, but it does not accurately reflect the health of individuals with high muscle mass or varying age.')
sleep(8)
print('Firstly, tell me some infos:')
sleep(1)
weight = int(input('weight(in KG): '))
height = int(input('height (in CM): '))
# BMI calculation
bmi = (weight/((height/100)**2))
# Results
def message(result):
    print(f'BMI: {round(bmi, 1)} - {result}')
if bmi < 18.5:
    message('underweight')
elif bmi >= 18.5 and bmi <= 24.99:
    message('normal weight')
elif bmi >= 25 and bmi <= 29.99:
    message('overweight')
elif bmi >= 30 and bmi <= 34.99:
    message('class 1 (low-risk) obesity')
elif bmi >= 35 and bmi <= 39.99:
    message('class 2 (moderate-risk) obesity')
elif bmi >= 40:
    message('class 3 (high-risk) obesity')
# Acknowledgment
sleep(3)
print('Thanks for using my code. Please, tell me any errors. Bye Bye! ')