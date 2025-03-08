#Level 2
first_name, last_name, age = "Fernando", "Bautista Vicke", 18
full_name = first_name + " " + last_name
country, city, year = "México", "Aguascalientes", 2025
is_married, is_true, is_light_on = False, False, True
print(type(first_name), type(last_name), type(age))                                     
print(type(full_name))                                                                  
print(type(country), type(city), type(year))                                            
print(type(is_married), type(is_true), type(is_light_on))                               
print("Length of first and last names: ", len(first_name), "and", len(last_name))      
num_one, num_two = 5, 4                                                                 
total = num_one + num_two                                                               
diff = num_one - num_two                                                                
product = num_one * num_two                                                             
division = num_one / num_two                                                            
remainder = num_one % num_two                                                           
exp = num_one ** num_two                                                                
floor_division = num_one // num_two                                                     

r=30                                                                                    
area_of_circle = (r**2)*3.14159                                                         
circum_of_circle = 2*r*3.14159                                                          

r = float(input("Enter the value of the radius: "))                                     
print ("The area of your circle is", area_of_circle)

first_name, last_name, country, age = input("Please enter your first and last names, your country, and your age, separated by a coma and a space: ").split(", ")
print(first_name, last_name, country, age)                                             

              