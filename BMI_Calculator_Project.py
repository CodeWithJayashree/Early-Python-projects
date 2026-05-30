# Write code below 💖 This is a BMI calculator I made using Gemini to debug my code! 1/27/26
def BMI_calculator():
  print('Hello user! Please enter the following information as integers.')
  print('Once you have entered an integer, press enter to continue!')
  while True:
    try:
        mass:float = float(input('Mass (kg): '))
        height: float = float(input('Height (m): '))
        bmi = mass/(height**2)
        print (f"Your BMI is: {bmi}")
        if bmi < 18.5:
          print('Weight category: Underweight')
        elif 18.5 <= bmi <= 24.9:
          print("Weight category: Normal")
        elif 25 <= bmi <= 29.9:
          print("Weight category: Overweight")
        else:
          print('Weight category: Obese')
        break
    except ValueError:
      print("Please enter numbers only.")
  print('Have a good day!')

BMI_calculator()
