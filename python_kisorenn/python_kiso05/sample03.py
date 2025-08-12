def count_up_tp(max):
    count = 1
    while count <= max:
        yield count
        count +=1

for num in count_up_tp(5):
    print(num)