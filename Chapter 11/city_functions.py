def get_formatted_city(city, country, population=""):
    if population:
        formatted_location = f"{city}, {country} Population: {population}"
    else:
        formatted_location = f"{city}, {country}"    
    return formatted_location.title()
