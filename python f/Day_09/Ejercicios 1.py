age = int(input("Enter your age: "))                                                #1
if age >= 18:
    print("You´re old enough to learn to drive.")
else:
    gap = 18 - age
    if gap == 1:
        print("You need one more year to learn to drive")
    else:
        print(f"You need {gap} more years to learn to drive.")

my_age = int(input("Enter my age: "))                                               #2
your_age = int(input("Enter your age: "))
gap_ages = abs(my_age - your_age)
if my_age == your_age:
    print("We´re both the same age.")
elif my_age > your_age:
    if gap_ages == 1:
        print("I´m one year older than you")
    else:
        print(f"I´m {gap_ages} years older than you.")
else:
    if gap_ages == 1:
        print("You´re one year older than me")
    else:
        print(f"You´re {gap_ages} years older than me.")

num_A = input("Enter number A: ")                                                     #3
num_B = input("Enter number B: ")
if num_A == num_B:
    print("A is equal to B")
elif num_A > num_B:
    print("A is bigger than B")
else:
    print("B is bigger than A")