prompt = "\nTell me what toppings you want for your delicious pizza:"
prompt += "\nEnter 'quit' to end the program. "

while True:
	topping = input(prompt)

	if topping == 'quit':
		break
	else:
		print(f"Adding {topping.title()} to your delicious pizza.")