import copy
dog={}
dog={'Name':'Buzo','Colour':'Golden Shine','Breed':'Retriver','Legs':'tinyBabyCatPaws','age':2}
student={
    'FirstName':'Arka',
    'LastName':'Banerjee',
    'Gender':'Male',
    'Age':19,
    'Marital Status':False, 
    'Skill':["JAVA", "C++", "PYTHON", "Data Science"], 
    'Country':'India',
    'City':'Kolkata',
    'Address': {
        'pin': 710012,
        'area': 'Chinarpark',
    } 
    
}
# print(len(student))
# print(type(student['Skill']))

# adding skills 
student_copy=copy.deepcopy(student)

student['Skill'].extend(['DBMS', 'DSA'])
# extend -> adds each element individually: [..., 'DBMS', 'DSA']
# append -> adds the whole list as ONE item: [..., ['DBMS', 'DSA']]
student_copy['Skill'].append(['DBMS', 'DSA'])

# print(student['Skill'])        
        
# to get dictionary keys and value as list 

# print(student.keys())
# print(student.values())

# changing dictionary to a list of tuples 

# print(student.items() )

student.pop('Gender')

# delete dog completely
del dog

# print(student.get('abcd'))
# get method returns 'None' in case specified key not present 

# if(student.get('Hobby') is None ): print('Not Specified')
# else: print(student.get('Hobby'))

# optimizee 
print(student.get('Hobby', 'Not Specified'))

# dictionary.update({}) allow us to perform multiple modifications at once 

student.update({'Age':20, 'Email': 'anboy@gamil.com'})

    
# setdefault(key,<optionalVal>) 
# returns existing value if key already present else return the default value 
# never overwrites the existing keys 

print(student.setdefault('Hobby','Coding'))

# as hobby do not exist it will add the hobby as a key 

# now that we have a key called Hobby, if we reuse setdefault with the  same key and different value, it wont overwrite the hobby 
print(student.setdefault('Hobby','Gaming'))

# in checks 

print('City' in student )
print('Kolkata' in student.values())
print('PYTHON' in student['Skill'])
print('python' in student['Skill'])

# Nested acccess

print(student['Address']['area'])
student['Address'].update({'pin':700001, 'state':'West Bengal'})

for key in student:
    print(student[key])







        
        
        
        
