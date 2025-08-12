try:
    x = int(input("数字を入力してください："))
    print("入力した数字は",x)
except ValueError:
    print("数字じゃありません")