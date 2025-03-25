def describe_city(city_name, country='united states'):
	print(f"\n{city_name.title()} is in {country.title()}.")

describe_city('boston')
describe_city('san francisco')
describe_city('beijing', 'china')