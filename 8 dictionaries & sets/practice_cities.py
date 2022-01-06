# Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
# Create a dictionary of information about each city and include the country that the city is in, 
# it's approximate population, and one fact about that city. 
# The keys for each citys dictionary should be something like country, population, and fact. 
# Print the name of each city and all of the information you have stored about it.
# city1 = {"country": "Austria", "population": 1000000, "fact": "The first postcards used were in Austria"}
# cities = {"Tokio": city1, "Rio": city2, "Nairobi": city3}

country = ""
population = 0
fact = ""

cities = {'berlin': {
    'country': 'germany', 'population': 1, 'fact': 'capital of Germany'
    },
    'rome': {
    'country': 'italy', 'population': 2, 'fact': 'capital of Italy'
    },
    'paris' :{
    'country': 'france', 'population': 3, 'fact': 'capital of France'
    },
}
for city, city_info in cities.items():
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

    print(city.title() + " is in " + country.title() + ".")
    print("It has population of " + str(population) + ".")
    print("The " + fact + ".\n")