evens = []                                                                                  #1
odds = []
def evens_and_odds(parameter):
    for i in range(parameter + 1):
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    print(f"There are {len(evens)} even numbers in the desired range.")
    print(f"There are {len(odds)} odd numbers in the desired range.")
evens_and_odds(100)

def factorial(factorial):                                                                   #1
     fact = 1
     for i in range(1, factorial + 1):
        fact = fact * i
     return fact
print(factorial(5))

fruit = ["apple", "orange"]                                                                 #2
fruit_e = []
def is_empty(parameter):
    if bool(parameter) == True:
        print("It´s not empty")
    else:
        print("It´s empty")
is_empty(fruit)
is_empty(fruit_e)

numbers = [1, 2, 7, 2, 3, 3, 5, 7, 6, 1, 2, 4]                                              #3
def calculate_mean(lst):
    total = 0
    for i in lst:
        total += i
    mean = total/len(lst)
    return(round(mean, 3))
    
def calculate_median(lst):
    if len(lst) % 2 == 0:
        median = (lst[len(lst)//2] + lst[(len(lst)//2)-1])/2
        return(median)
    else:
        median = lst[len(lst)//2]
        return(median)

def calculate_mode(lst):
    mode = {lst[0]:lst.count(lst[0])}
    for i in lst:
        mode_i = lst.count(i)
        if mode_i > mode[list(mode)[0]]:
            mode = {i:lst.count(i)}
        elif mode_i == mode[list(mode)[0]]:
            mode[i] = lst.count(i)
    return(mode)

def calculate_range(lst):
    highest = 0
    for i in lst:
        if i > highest:
            highest = i
    lowest = highest
    for i in lst:
        if lowest > i:
            lowest = i
    range = highest - lowest
    return(range)

def calculate_variance(lst):
    total_variance = 0
    mean = calculate_mean(lst)
    for i in lst:
        total_variance += (i - mean)**2
    variance = total_variance/len(lst)
    return(round(variance, 3))

def calculate_std(lst):
    total_std = 0
    mean = calculate_mean(lst)
    for i in lst:
        total_std += (i - mean)**2
    std = (total_std/(len(lst)-1))**(1/2)
    return(round(std, 3))

print(f"The mean is {calculate_mean(numbers)}")
print(f"The median is {calculate_median(numbers)}")
print(f"The mode is {calculate_mode(numbers)}")
print(f"The range is {calculate_range(numbers)}")
print(f"The variance is {calculate_variance(numbers)}")
print(f"The standard deviation is {calculate_std(numbers)}")