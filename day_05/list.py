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

print(it_companies.sort(reverse=True))
print(it_companies[0:3])
print(it_companies[-3:])
print(it_companies[len(it_companies) // 2])
print(it_companies.remove("Meta"))
print(it_companies.pop())
print(it_companies.pop(-1))
print(it_companies.clear())
print(it_companies)
del it_companies
#print(it_companies)  # This will raise an error since it_companies has been deleted

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(", ".join(front_end + back_end))
joined_list = front_end + back_end
print(joined_list)
full_stack = joined_list.copy()
joined_list.insert(5, 'Python')
joined_list.insert(6, 'SQL')
print(joined_list)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
sorted_ages = sorted(ages)
print(sorted_ages)
ages.reverse()
print(ages)
ages.sort(reverse=True)
print(ages)
ages_set = set(ages)
print(ages_set)

min_age = min(ages)
max_age = max(ages)
print(f"Min age: {min_age}, Max age: {max_age}")

ages.insert(0, min_age)
ages.append(max_age)
print(ages)

median_age = ages[len(ages) // 2]
print(f"Median age: {median_age}")
average_age = sum(ages) / len(ages)
print(f"Average age: {average_age}")
range_of_ages = max_age - min_age
print(f"Range of ages: {range_of_ages}")

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
mid_country = countries[len(countries) // 2]
print(f"Middle country: {mid_country}")

country_divide = len(countries) // 2
first_half = countries[:country_divide]
second_half = countries[country_divide:]
print(f"First half: {first_half}, Second half: {second_half}")    

countries_divide = len(countries) // 2
if len(countries) % 2 == 0:
    first_half = countries[:countries_divide]
    second_half = countries[countries_divide:]
else:
    first_half = countries[:countries_divide + 1]
    second_half = countries[countries_divide + 1:]
print(f"First half: {first_half}, Second half: {second_half}")

CHN, RUS, US, *Scandiv_countries = countries
print(f"CHN: {CHN}, RUS: {RUS}, US: {US}, Scandiv_countries: {Scandiv_countries}")