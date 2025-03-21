family_members = ("Faus", "Are", "Sara", "Paula", "David", "Rosa")           #1
siblings = family_members[0:2]
parents = family_members[2:]

fruits = ("Apple", "Orange", "Banana")                                              #2
vegetables = ("Lettuce", "Tomato", "Onion")
animals = ("Chicken", "Fish", "Beef")
food_stuff_tp = fruits + vegetables + animals

food_stuff_lt = list(food_stuff_tp)                                                 #3

middle_item = food_stuff_tp[4]                                                      #4

first_three = food_stuff_tp[0:3]                                                    #5
last_three = food_stuff_tp[-3:]

del food_stuff_tp                                                                   #6

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')             #7
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)