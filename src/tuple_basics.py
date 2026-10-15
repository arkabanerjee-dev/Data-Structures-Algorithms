tpl=tuple()
tpl_bro=('tom','roz','foroz')
tpl_sis=('srijs','era','lanry')
tpl_sibl=tpl_bro+tpl_sis

print("number of siblings i have: ",len(tpl_sibl))
# we cannot directly modify our tuple to add ('dad','mom')
# using append() insert() extend()
# it will throw TypeError as assignment is not allowed in tuple objects 
# lst=list(tpl_sibl)
# lst.extend(['dad','mom'])
# tpl_sibl=tuple(lst)
# print(tpl_sibl)

# another way of adding dad and mom 

tup_family=tpl_sibl+('dad','mom')
print(tup_family)
a,b,c,*g,d=tup_family
print(d,g)
del tup_family
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print('Iceland' in nordic_countries)













