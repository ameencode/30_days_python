#tuple = ()
empty_tuple = tuple()

tuple_bro = ("Rasheed", "Kamaal", "Abdullah", "Anas", "Ali")
tuple_sis = ("Fatimah", "Khadijah", "Zaynab", "Layaan", "Miraal")
siblings = tuple_bro + tuple_sis
print(siblings)
print(len(siblings))
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = ("Father", "Mother") + siblings
print(family_members)

# Another way
family_members_new = list(siblings)
family_members_new.extend(["Father", "Mother"])
family_members_new = tuple(family_members_new)
print(family_members_new)

# Unpacking a tuple
father, mother, *siblings, distant_relative = family_members
print(f"Father: {father}, Mother: {mother}, Siblings: {siblings}, Distant Relative: {distant_relative}")

fruits = ("Mango", "Banana", "Apple", "Orange", "Grapes")
vegetables = ("Carrot", "Broccoli", "Spinach", "Cabbage", "Pepper")
animal_products = ("Milk", "Cheese", "Eggs", "Yogurt", "Butter")
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
food_stuff_list = list(food_stuff_tp)
print(food_stuff_list)

middle_item = food_stuff_tp[len(food_stuff_tp) // 2]
print(f"Middle item: {middle_item}")
first_three_items = food_stuff_tp[:3]
last_three_items = food_stuff_tp[-3:]
print(f"First three items: {first_three_items}")
print(f"Last three items: {last_three_items}")

#Deleting a tuple
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)  # False
print("Iceland" in nordic_countries)  # True