#sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

age_set = set(age)                                                                           #1
if len(age) > len(age_set):
    print("List is bigger")
else:
    print("Set is bigger")

print("This is a string, which consists of text inside single, double or triple quote")      #2
print(["A list is a collection of data, ", "that is", "Ordered", "Changeable", "And allows Duplicates"])
print(("A tuple is similar to a list", "but it is unchangeable"))
print({"Finally, a set is different because it is", "Unorganized (Which is the reason you will see this text in the wrong order)", "Unchangeable", "and without duplicates"})

print(len(set("I am a teacher and I love to inspire and teach people".split())))             #3