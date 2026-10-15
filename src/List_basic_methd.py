
# 1. Declare an empty list
lst1=[]

# 2. Declare a list with more than 5 items
lst2=[False,1,"mid","lala",True,0.1]

# 3. Find the length of your list
print(len(lst2))

# 4.Get the first item, the middle item and the last item of the list

print(lst2[0]," ",lst2[(len(lst2)-1)//2]," ",lst2[len(lst2)-1])

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types=["arka",19,5.8,"unmarried","kokata-b2ut73gryu"]

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Print the list using print()

print(it_companies)

# 8.Print the number of companies in the list

print(len(it_companies))

# 9.Print the first, middle and last company


print(it_companies[0]," ",it_companies[(len(it_companies)-1)//2]," ",it_companies[len(it_companies)-1])

# 10. Print the list after modifying one of the companies

it_companies[len(it_companies)-1]="Nvdia"
# print(it_companies)

# 11. Add an it company to it_companies
it_companies.append("Intel")
# print(it_companies)

# 12.Insert an IT company in the middle of the companies list

it_companies.insert(1,"Anthropic")
# print(it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)

it_companies[1]=it_companies[1].upper()
print(it_companies)

# 14. Join the it_companies with a string '#;  '

str_list="#;".join(it_companies)
print(str_list)

# 15.Check if a certain company exists in the it_companies list.

if("ANTHROPIC" in it_companies) :
    print ("true")
else :
    print("false")

# 16.Sort the list using sort() method

it_companies.sort()

# sort method do not return anything rather it reorders the existing list
print(it_companies)

# 17. Reverse the list in descending order using reverse() method 
it_companies.reverse()
print(it_companies)

# 18. Slice out the first 3 companies form the list 
print(it_companies[0:3])

# 19. Slice out the last 3 companies from the list

print(it_companies[len(it_companies)-3:])

# 20.Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# 21. Remove the middle IT company or companies from the list

del it_companies[3:5]
print(it_companies)

# 22.  Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 23. Remove the first IT company from the list 
it_company=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
print(it_company.remove("Facebook"))
 #remove method do not return the value of the item that it removed unlike pop
print(it_company)

# 24. Remove the middle IT company or companies from the list
it_company.insert(0,"Facebook")
del it_company[len(it_company)//2]
print(it_company)

# 25. Remove the last IT company from the list
it_company.pop()
print(it_company)

# 26. Remove all IT companies from the list
it_company.clear()
print(it_company)

# 27. Destroy the IT companies list
del it_company

# print(it_company) # will give name 'it_company' is not defined error

# 28. Join the following lists: front_end and back_end and assign it to a variable full_stack. 
# Then insert Python and SQL after Redux.
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end) # extend do not return anything insted extends the first list  
full_stack=front_end # shallow_copy
full_stack[4:4]=['python','Sql']
print(full_stack)






