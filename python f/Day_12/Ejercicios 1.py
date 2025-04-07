import random
import string
def random_user_id():                                                                   #1
    characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choices(characters, k=6))
    return user_id
print(random_user_id())

digits= int(input("Amount of digits: "))                                                #2
ID= int(input("Number of ID´s: "))
def user_id_gen_by_user():
    characters = string.ascii_letters + string.digits
    IDS = [''.join(random.choices(characters, k=digits)) for _ in range(ID)]
    return IDS
generated_ids = user_id_gen_by_user()
for gen in generated_ids:
    print(gen)

def rgb_color_gen():                                                                    #3
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    return r,g,b
print(rgb_color_gen())