burgers = ["beef", "chicken", "spicy bean"]
toppings = ["cheese", "egg", "beans", "spam"]

meals = [(burger, topping) for burger in burgers for topping in toppings]
print(meals)

print()
#
# for burger in burgers:
#     for topping in toppings:
#         print((burger, topping))


for meals in [[(burger, topping) for burger in burgers] for topping in toppings]:
    print(meals)