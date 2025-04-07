numbers = [-4, -3, -2, -1, 0, 2, 4, 6]                                                      #1
number = [i for i in numbers if i <= 0]
print(number)

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]                                     #2
flat_list=[i for sub in list_of_lists for sub2 in sub for i in sub2]
print(flat_list)

tpl_lst = [(i, 1, i**1, i**2, i**3, i**4, i**5) for i in range(11)]                          #3
print(tpl_lst)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]    #4
flat_countries = [[country.upper(), country[:3].upper(), capital.upper()] for sublist in countries for country, capital in sublist]
print(flat_countries)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]    #5
dct_countries = [{'country': country.upper(), 'city': city.upper()} for sublist in countries for country, city in sublist]
print(dct_countries)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]] #6
con_str = [f"{first} {last}" for sublist in names for first, last in sublist]
print(con_str)

linear_function = lambda x1, y1, x2, y2, calc: (y2 - y1) / (x2 - x1) if calc == 'slope' else y1 - ((y2 - y1) / (x2 - x1)) * x1  #7
slope = linear_function(1, 2, 3, 6, 'slope')  
y_intercept = linear_function(1, 2, 3, 6, 'y-intercept') 
print("Slope:", slope)
print("Y-Intercept:", y_intercept)