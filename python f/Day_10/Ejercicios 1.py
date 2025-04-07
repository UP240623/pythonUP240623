count = 0                                                                       #1
while count < 11:
    print(count)
    count = count + 1
for i in range(0,11):
    print(i)

count = 10                                                                      #2
while -1 < count:
    print(count)
    count = count - 1
for i in range(10, -1, -1):
    print(i)

triangle = "#"                                                                  #3
for i in range(0, 7):
    print(triangle)
    triangle = triangle + "#"

square = ""                                                                     #4
for row in range(8):
    for col in range(8):
        square = square + "# "
    square = square + "\n"
print(square)

for i in range(11):                                                             #5
    print(f"{i} x {i} = {i*i}")

for i in ['Python', 'Numpy','Pandas','Django', 'Flask']:                        #6
    print(i)

for i in range(101):                                                            #7
    if i%2==0:
        print(i)

for i in range(101):                                                            #8
    if i%2==1:
        print(i)