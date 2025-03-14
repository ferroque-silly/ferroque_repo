rivers = {'nile': 'egypt', 'mississippi': 'america', 'volga': 'russia'}

for key, value in rivers.items():
	print(f"The {key.title()} runs through {value.title()}.")

print("The following rivers have been mentioned:")
for river in rivers.keys():
	print(river.title())

print("The following countries have been mentioned:")
for country in rivers.values():
	print(country.title())