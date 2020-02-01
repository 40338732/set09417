datalist = [1, 3, 4, 7, 2, 9,55]

biggest = datalist[2]

for val in datalist:
    if val > biggest:
        biggest = val
        print(biggest)