favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

should_takers = ['jen', 'domingo', 'brimble', 'edward', 'splimby', 'phil']

for name in should_takers:
	if name in favorite_languages.keys():
		print(f"{name.title()}, thank you for taking the poll.")
	else:
		print(f"{name.title()}, you should take the poll.")