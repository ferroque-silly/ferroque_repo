age = 32

if age < 2:
	you = 'baby'
elif age < 4:
	you = 'toddler'
elif age < 13:
	you = 'kid'
elif age < 20:
	you = 'teenager'
elif age < 65:
	you = 'adult'
else:
	you = 'elder'

print(f"You are of the age-class {you}.")