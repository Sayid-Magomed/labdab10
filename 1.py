import json

with open("1.json", "r") as file:
    data = json.load(file)

for i in data["products"]:
    print("Имя: ", i["name"])
    print("Цена: ", i["price"])
    print("Вес: ", i["weight"])
    print("Имеется" if i["available"] else "Нет в наличии!", "\n")
