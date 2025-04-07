def add_two_numbers(num1, num2):                                                #1
    sum = num1 + num2
    print(sum)

def area_of_a_circle(radius):                                                   #2
    area = radius*radius*3.14159
    print(area)

def add_all_nums(*args):                                                        #3
    total = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            total += arg
        else:
            print(f"'{arg}' is not a number, and for that it´ll be skipped.")
    return total

def convert_celsius_to_fahrenheit(celcius):                                     #4
    farenheit = celcius * 9/5 + 32
    print(farenheit)
convert_celsius_to_fahrenheit(35)

spring = ["March", "April", "May"]                                              #5
summer = ["June", "July", "August"]
autumn = ["September", "October", "November"]
winter = ["December", "January", "February"]
def check_season(month):
    if month in spring:
        print("This month belongs to spring.")
    elif month in summer:
        print("This month belongs to summer.")
    elif month in autumn:
        print("This month belongs to autumn.")
    elif month in winter:
        print("This month belongs to winter.")
    else:
        print("This isn´t a valid input.")

def calculate_slope(coeff_x, coeff_y):                                          #6
    slope = -1*coeff_x/coeff_y
    print(slope)

def solve_quadratic_eqn(a, b, c):                                               #7
    x1 = ((b*-1) + ((b**2) - (4*a*c))**(1/2))/(2*a)
    x2 = ((b*-1) - ((b**2) - (4*a*c))**(1/2))/(2*a)
    print(x1, x2)

def print_list(list):                                                           #8
    for i in list:
        print(i)
print(print_list)

def reverse_list(arr):                                                          #9
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    print(reversed_arr)

def capitalize_list_items(list_items):                                          #10
    capitalized = []
    for item in list_items:
        if isinstance(item, str):
            capitalized.append(item.capitalize())
        else:
            capitalized.append(item)
            print("Please enter a string value.")
    print(capitalized)

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']                              #11
def add_item (lst,item):
    lst.append(item)
    print(lst)
add_item(food_staff, 'Meat')

def remove_item (lst,item):                                                     #12
    lst.remove(item)
    print(lst)
print(remove_item(food_staff, 'Mango'))

def sum_of_numbers(number):                                                     #13
     sum_of_numbers = 0
     for i in range (number + 1):
        sum_of_numbers += i
     print(sum_of_numbers)

def sum_of_odds (odd):                                                          #14
     sum_of_odd_nums = 0
     for i in range(odd + 1):
        if i % 2 == 1:
            sum_of_odd_nums += i
     print(sum_of_odd_nums)

def sum_of_even(even):                                                          #15
     sum_of_even_nums = 0
     for i in range(even + 1):
        if i % 2 == 1:
            sum_of_even_nums += i
     print(sum_of_even_nums)