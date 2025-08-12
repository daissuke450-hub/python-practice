person = {
    "名前":"花子",
    "年齢": 25,
    "出身" : "東京"
}

print(person["名前"]) #花子

# 辞書の全キー・値を取得
for key, value in person.items():
    print(key, ":", value)