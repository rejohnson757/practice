# 05/04/20

def pay_check():
	your_pay = float(input('How much do you make? '))
	print('Is your pay correct?')
	pay_answer = input()
	if pay_answer == 'Yes' or pay_answer == 'yes':
		your_pay = your_pay
	else:
		your_pay = float(input('How much do you make?'))
	
	your_hours = int(input('How many hours did you work? '))
	print('Is your hours correct?')
	hours_answer = input()
	if hours_answer == 'yes' or hours_answer == 'Yes':
		your_hours = your_hours
	else:
		your_hours = int(input('How many hours did you work?'))

	if your_hours > 40:
		print((your_pay * 1.5) * your_hours)
	elif your_hours <= 40:
		print(your_hours * your_pay)
		

pay_check()
