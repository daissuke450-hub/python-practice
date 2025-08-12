# 二倍にする関数を定義
double = lambda x: x * 2

print(double(5)) # 10

# リストの各要素をラムダで変換
number = [1,2,3,4]
doubled = list(map(lambda x : x * 2, number))
print(doubled) # [2,4,6,8]