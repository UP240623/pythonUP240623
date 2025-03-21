empty_list = list()                                                                     #1

five_item_list = [1,2,3,4,5,6]                                                          #2

print(len(five_item_list))                                                              #3

print(five_item_list[0])                                                                #4
print(five_item_list[2])
print(five_item_list[5])

mixed_data_types = ["David", 18, 1.78, "Single", "Flor de Nochebuena 86"]               #5

it_companies = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]   #6

print(it_companies)                                                                     #7

print(len(it_companies))                                                                #8

print(it_companies[0])                                                                  #9
print(it_companies[3])
print(it_companies[6])

it_companies[0] = "Sony"                                                                #10
print(it_companies)

it_companies.append("Intel")                                                               #11

it_companies.insert(1, "Ryzen")                                                            #12

it_companies[2] = it_companies[2].upper()                                               #13
print(it_companies)

joined_list = "#; ".join(it_companies)                                                  #14
print(joined_list)

print("Amazon" in it_companies)                                                         #15

it_companies.sort()                                                                     #16
print(it_companies)

it_companies.sort(reverse=True)                                                         #17
print(it_companies)

print(it_companies[0:3])                                                                #18

print(it_companies[-3:])                                                                #19

print(it_companies[3])                                                                  #20

del it_companies[4]                                                                     #21
print(it_companies)

del it_companies[0]                                                                     #22
print(it_companies)

del it_companies[3]                                                                     #23
print(it_companies)

del it_companies[len(it_companies)-1]                                                   #24
print(it_companies)

it_companies.clear()                                                                    #25
print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']                                     #26
back_end = ['Node','Express', 'MongoDB']
both_ends = front_end + back_end
print(both_ends)

full_stack = both_ends                                                                  #27
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)