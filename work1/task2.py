foods = ("Apple", "Banana", "Orange", "Mango", "Strawberry", "Grape", "Mandarin", "Strawberry")
calories = (52, 96, 62, 605, 33, 68, 50, 33)

foods_list = list(foods)
calories_list = list(calories)

print(f"5th food is {foods_list[4]} with {calories_list[4]} cal")
print( f"Second last food is {foods_list[-2]} with {calories_list[-2]} cal")

unique_foods = list(set(foods_list))
print("Unique foods:", unique_foods)

food_dict = {}
for i in range(len(foods)):
    food_dict[foods[i]] = calories[i]
print("Food dictionary:", food_dict)