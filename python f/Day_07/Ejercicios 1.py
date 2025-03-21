#sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))                                                                #1

it_companies.add("Twitter")                                                             #2

it_companies.update(["Intel", "Windows", "Samsung"])                                    #3

it_companies.remove("Apple")                                                            #4

#it_companies.remove("Lenovo") Will return error                                        #5
it_companies.discard("Lenovo") #Won´t