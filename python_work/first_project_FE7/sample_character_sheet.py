units = {
	'eliwood': {
		'HP': 18,
		'S/M': 5,
		'Skl': 5,
		'Spd': 7,
		'Lck': 7,
		'Def': 5,
		'Res': 0,
		'Con': 7,
		'Affin': 'anima',
		'ranks': {
			'swords': 'C'
		},
	},
	'matthew': {
		'HP': 18,
		'S/M': 4,
		'Skl': 4,
		'Spd': 11,
		'Lck': 2,
		'Def': 3,
		'Res': 0,
		'Con': 7,
		'Affin': 'wind',
		'ranks': {
			'swords': 'D'
		},
	},
}

for unit, stat in units.items():
	print(f"\nHere are {unit.title()}'s base stats:")
	