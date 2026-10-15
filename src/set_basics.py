# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add("Twitter")

# to add multiple companies at once to the set
it_companies.update(['Adobe', 'Anthropic', 'OpenAI'])

print(it_companies)

# to remove one randome it company from the set
it_companies.pop()

# What is the difference between remove and discard
# if sepcified elemet not found remove() raises an error 
# while discard do not raise any error and handles the situation 

# to join A and B

C=A.union(B)
# union only returns a new set  with all elements of A and B joined together without repeatation 
# print(C)

# A intersection B

C=A.intersection(B)
# common elements
# print(C)

# Is A subset of B
print(A.issubset(B))
#Is B subset of A
print(B.issubset(A))
# Is B suprset of A
print(B.issuperset(A))

# Are A and B disjoint sets
# if A and B had nothing in common - they are disjoints 
print(A.isdisjoint(B))

# What is the symmetric difference between A and B
print(A.symmetric_difference(B))
# it returns all items exept the one that are common in both sets A and B
del A
del B
age_set=set(age)
print(len(age)-len(age_set))

# I am a teacher and I love to inspire and teach people.
#  How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
list_words=sentence.replace(".", "").split()
unique_words=set(list_words)
# the set() function will remove all the duplicate elements and add each element only once
#  to the set and return the unique elements in the set 
print(unique_words)

