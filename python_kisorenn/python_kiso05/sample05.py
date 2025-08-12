numbers = [1,5,2,9,3]

# 偶数だけ抽出
evens = list(filter(lambda x : x % 2 == 0,numbers))
print(evens)

# 降順ソート
desc = sorted(numbers, reverse=True)
print(desc)