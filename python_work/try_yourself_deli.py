sandwich_orders = ['italian', 'reuben', 'tuna', 'buffalo chicken', 'meatball']
finished_sandwiches = []

while sandwich_orders:
	current_order = sandwich_orders.pop()

	print(f"I am making your delicious {current_order.title()} sandwich.")
	finished_sandwiches.append(current_order)

print("\nThe following sandwiches have been prepared:")
for finished_sandwich in finished_sandwiches:
	print(f"{finished_sandwich.title()} sandwich")