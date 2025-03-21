word_1 = "Thirty"                                                                       #1
word_2 = "days"
word_3 = "of"
word_4 = "Python"
space = " "
sentence = word_1 + space + word_2 + space + word_3 + space + word_4
print(sentence)

word_a = "Coding"                                                                       #2
word_b = "for"
word_c = "all"
sentence_2 = word_a + space + word_b + space + word_c
print(sentence_2)

company = sentence_2                                                                    #3

print(company)                                                                          #4

print(len(company))                                                                     #5

print(company.upper())                                                                  #6

print(company.lower())                                                                  #7

print(company.capitalize())                                                             #8
print(company.title())
print(company.swapcase())

print(company[0:6])                                                                     #9

print("Coding" in company)                                                              #10

print(company.replace("Coding", "Python"))                                              #11

sentence_3 = "Python for everyone"                                                      #12
print(sentence_3.replace("everyone", "all"))

print(company.split())                                                                  #13

print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", "))            #14

print("Coding for all"[0])                                                              #15

last_index = len("Coding For All")-1                                                    #16
last_letter = "Coding for all"[last_index]
print(last_index)
print(last_letter)

print("Coding for all"[10])                                                             #17

abbreviation = ""                                                                       #18
for letter in "Python For Everyone":
    if (letter.isupper()) == True:
        abbreviation += letter
print(abbreviation)

abbreviation_02 = ""                                                                    #19
for letter in "Coding For All":
    if (letter.isupper()) == True:
        abbreviation_02 += letter
print(abbreviation_02)

print(company.find("C"))                                                                #20

print(company.find("f"))                                                                #21

print(company.rfind("i"))                                                               #22

print("You cannot end a sentence with because because because is a conjunction".find("because")) #23

print("You cannot end a sentence with because because because is a conjunction".rfind("because")) #24

print("You cannot end a sentence with because because because is a conjunction"[31:54]) #25

first_word = "Coding for all".split(" ")                                                #28
if first_word[0] == "Coding":
    print(True)
else:
    print(False)

if first_word[2] == "coding":                                                           #29
    print(True)
else:
    print(False)

print("Coding for all".expandtabs(0))                                                   #30

if "30DaysOfPython".isidentifier() == True:                                             #31
    print(True)
else:
    print(False)

if "thirty_days_of_python".isidentifier() == True:
    print(True)
else:
    print(False)

print(' # '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))                   #32

print("I am enjoying this challenge\n\nI just wonder what is next")                     #33

print("Name\t\tAge\tCountry\t\tCity\nAsabeneh\t250\tFinland\t\tHelsinki")               #34

radius = 10
area = int(3.14 * radius ** 2)
print(f"The area of a circle with radius {radius} is {area} meters square")             #35

num_1 = 8                                                                               #36
num_2 = 6
print("{} + {} = {}".format(num_1, num_2, num_1 + num_2))
print("{} - {} = {}".format(num_1, num_2, num_1 - num_2))
print("{} * {} = {}".format(num_1, num_2, num_1 * num_2))
print("{} / {} = {:.2f}".format(num_1, num_2, num_1 / num_2))
print("{} % {} = {}".format(num_1, num_2, num_1 % num_2))
print("{} // {} = {}".format(num_1, num_2, num_1 // num_2))
print("{} ** {} = {}".format(num_1, num_2, num_1 ** num_2))