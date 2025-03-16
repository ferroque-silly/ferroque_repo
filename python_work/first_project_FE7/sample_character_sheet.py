units = {
	'eliwood': {
		'hp': 18,
		's/m': 5,
		'skl': 5,
		'spd': 7,
		'lck': 7,
		'def': 5,
		'res': 0,
		'con': 7,
		'affin': 'anima',
		'ranks': {
			'swords': 'C'
		},
	},
	'matthew': {
		'hp': 18,
		's/m': 4,
		'skl': 4,
		'spd': 11,
		'lck': 2,
		'def': 3,
		'res': 0,
		'con': 7,
		'affin': 'wind',
		'ranks': {
			'swords': 'D'
		},
	},
}

for unit, stat in units.items():
	print(f"\nHere are {unit.title()}'s base stats:")
	print(f"HP: {stat['hp']}")
	print(f"S/M: {stat['s/m']}")
	print(f"Skl: {stat['skl']}")
	print(f"Spd: {stat['spd']}")
	print(f"Lck: {stat['lck']}")
	print(f"Def: {stat['def']}")
	print(f"Res: {stat['res']}")
	print(f"Con: {stat['con']}")
	print(f"Affinity: {stat['affin'].title()}")
	print(f"Weapon Ranks: {stat['ranks']}")