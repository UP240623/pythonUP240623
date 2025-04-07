sum = 0                                                                             #1
for i in range(101):
    sum += i
print(sum)

sum_even = 0                                                                        #2
sum_odd = 0
for i in range(101):
    if i%2==0:
        sum_even+=i
    elif i%2==1:
        sum_odd+=i
print(sum_even)
print(sum_odd)