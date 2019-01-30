import json

from country_codes import get_country_code


#load data into a list
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

#print the population of the every country in 2010
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = pop_dict['Value']
        print(country_name + ": " + population)
        code =  get_country_code(country_name)
        if code:
            print(code + ": " + population)
        else:
            print('ERROR - ' + country_name)