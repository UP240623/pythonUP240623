score = float(input("Enter your score: "))                                      #1
if score > 100 or 0 > score:
    print("Please enter a valid score.")
else:
    if 50 > score:
        print("You´ve got a F")
    else:
        if 60 > score:
            print("You´ve got a D")
        else:
            if 70 > score:
                print("You´ve got a C")
            else:
                if 90 > score:
                    print("You´ve got a B")
                else:
                    if 100 >= score:
                        print("You´ve got an A")

spring = ["March", "April", "May"]                                              #2
summer = ["June", "July", "August"]
autumn = ["September", "October", "November"]
winter = ["December", "January", "February"]
month = input("Please enter a month of the year, starting with uppercase: ")
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

fruits = ['banana', 'orange', 'mango', 'lemon']                                 #3
check_fruit = input("Please enter a fruit: ")
if check_fruit in fruits:
    print("The fruit is already on the list.")
else:
    fruits.append(check_fruit)
    print(fruits)