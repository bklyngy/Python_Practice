first_answer = int(input("Please enter a number:\n"))
second_answer = int(input("Please enter another number:\n"))
choice = input("Enter 'A' for Add  or 'M' for Multiply':\n")
add_total = first_answer + second_answer
mult_total = first_answer * second_answer
if choice == 'A' or choice == 'a':
  print("Your answer is " + str(add_total))
elif choice == 'M' or choice == 'm':
  print("Your answer is " + str(mult_total))
else:
  print("Invalid response")

