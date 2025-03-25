def get_city_name(city, country):
	full_name = f"{city} {country}"
	return full_name.title()

city_country = get_city_name('santiago', 'chile')
print(f""city_country"")