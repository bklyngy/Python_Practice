first_answer = int(input("Please enter a number:\n"))
second_answer = int(input("Please enter another number:\n"))
choice = input("Enter 'A' for Add  or 'M' for Multiply':\n")
choice = choice.upper()
add_total = first_answer + second_answer
mult_total = first_answer * second_answer
if choice == 'A':
  print("Your answer is " + str(add_total))
elif choice == 'M':
  print("Your answer is " + str(mult_total))
else:
  print("Invalid response")

