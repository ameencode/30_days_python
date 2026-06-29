empty_list = list()
list_with_elements = [1, 2, 3, 4, 5]
print(empty_list)
print(list_with_elements)
print(len(empty_list))
print(len(list_with_elements))

first_item = list_with_elements[0]
print(first_item)
middle_item = list_with_elements[len(list_with_elements) // 2]
print(middle_item)
last_item = list_with_elements[-1]
print(last_item)

mixed_types_list = ["Ameenullah", 15, 5.5, "Married", "Nigeria"]
print(mixed_types_list)

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[len(it_companies) // 2])
print(it_companies[-1])

modified_it_companies = it_companies[0] = "Meta"
print(it_companies)

added_it_companies = it_companies.append("Twitter")
print(it_companies)

it_companies[1] = it_companies[1].upper()
print(it_companies)

joined_it_companies = "#; ".join(it_companies)
print(joined_it_companies)

print("Instagram" in it_companies)
it_companies.sort()
print(it_companies)

sorted_list = sorted(it_companies)
print(sorted_list)