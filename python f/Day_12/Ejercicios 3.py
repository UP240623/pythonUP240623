import random
import string
def shuffle_list(list):                                                                 #1
    random.shuffle(list)
    return list
print(shuffle_list([1,2,3,4,5,6,7,8,9]))

def unique_rgn():                                                                       #2
    return random.sample(range(10), 7)
print(unique_rgn())