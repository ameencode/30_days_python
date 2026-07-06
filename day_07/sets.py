it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))  # Length of the set
it_companies.add('Twitter')  # Adding an element to the set
print(it_companies)  # Displaying the set after adding an element
it_companies.update(['LinkedIn', 'Snapchat', 'TikTok'])  # Adding multiple elements to the set
print(it_companies)  # Displaying the set after adding multiple elements
it_companies.remove("IBM") # Removing an element from the set

# Removing an element from the set using discard (does not raise an error if the element is not found)
# difference between remove and discard
it_companies.discard("IBM")  # Discarding an element from the set
print(it_companies)  # Displaying the set after discarding an element

joined_set = A.union(B) # Joining two sets
print(joined_set)  # Displaying the joined set
intersection_set = A.intersection(B)  # Finding the intersection of two sets
print(intersection_set)  # Displaying the intersection set

print(A.issubset(B))  # Checking if A is a subset of B
print(A.isdisjoint(B))  # Checking if A and B are disjoint sets
joined_set2 = B.union(A)  # Joining two sets in the opposite order
print(joined_set2)  # Displaying the joined set in the opposite order

symmetric_difference = A.symmetric_difference(B)  # Finding the symmetric difference between two sets
print(symmetric_difference)  # Displaying the symmetric difference set

# Deleting the entire set
del A
del B
del it_companies

# Converting a list to a set to remove duplicates
unique_ages = set(age)
print(unique_ages)  # Displaying the unique ages after converting the list to a set
length_difference = len(age) - len(unique_ages)  # Calculating the difference in length between the original list and the unique set
print(length_difference)  # Displaying the difference in length

sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()  # Splitting the sentence into words
unique_words = set(words)  # Converting the list of words to a set to remove duplicates
print(unique_words) # Displaying the unique words after converting the list to a set
print(len(unique_words))  # Displaying the count of unique words after converting the list to a set