dog = {}                                                            #1

dog["name"], dog["color"], dog["breed"], dog["legs"], dog["age"] = "Billy", "Black", "Dachshund", 4, 5   #2
print(dog)

student = {                                                         #3
    "first_name":"Fernando",
    "last_name":"Bautista,
    "gender":"male",
    "age":18,
    "marital_status":"single",
    "skills":["python", "sleeping", "math"],
    "country":"Mexico",
    "city":"Aguascalientes",
    "address":"Calzada Navarra 456"
}

print(len(student))                                                 #4

print(student["skills"])                                            #5
print(type(student["skills"]))

student['skills'].append('drawing')                                 #6

print(list(student.keys()))                                         #7

print(list(student.values()))                                       #8

print(student.items())                                              #9

del student["marital_status"]                                       #10

del student                                                         #11