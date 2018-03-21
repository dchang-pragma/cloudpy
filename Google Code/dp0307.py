import operator
# citizen = {'Ben': [1900, 2000]}
# citizen = {'Ben': [1900, 2000]}
year_population = {}
citizen = {}
citizen['Ben'] = [1900, 2000]
citizen['Benny'] = [1973, 2073]
citizen['Alex'] = [1956, 2023]
citizen['Mary'] = [1928, 2033]
citizen['Alan'] = [1917, 1992]
citizen['Andrew'] = [2000, 2088]
citizen['Tony'] = [1988, 2035]

#print(citizen['Ben'][0])


# population = []
# population[1988] = 


class 


def population(citizen, year):
	count = 0
	for k, v in citizen.items():
		#print(1)
		#print(v[0], v[1])
		if v[0] <= year and v[1] >= year:
			count = count + 1
	return count



year_population[2001] = (population(citizen, 2001))
year_population[2000] = (population(citizen, 2000))
print(year_population)


#sorted_population = sorted(year_population.items(), key = operator.itemgetter(0))

print(year_population.get(2000))
sorted_population = [(k, year_population[k]) for k in sorted(year_population, key=year_population.get, reverse = True)]


print(sorted_population)

# calculate lowest birth year and highest birth year


