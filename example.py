my_list=[1,2,3,'Ammar','Kwame',{'name':'Ammar'}]
my_dict={
    'name':'Am',
    'Surname':'Nam',
    'Age':32
}
#print (my_dict)
#print(my_list[-1],['name'],my_list[-1],['Age'])
#for i in my_list:
 #   print (i)
#for a,b in my_dict.items():
 #   print(a,b)
List=[{
    'name':'Mhd Ammar',
    'lastName':'Nammour',
    'age':32,
    'hasCoffee':False
    },
{
    'name': 'Aj',
    'lastName': 'Michael',
    'age': 10,
    'hasCoffee': False
},
{
    "name": "Ana",
    "lastName": "Pereira",
    "age": 35,
    "hadCoffee":False
},
{
    "name":"Daniel",
    "lastName":"Ziebart",
    "age":41,
    "hasCoffee": False
}
]
#print (MyDicts)
for i in list:
    print (i)
for a,b in i.items():
    if a== 'Age':
        if b<=18:
    print(f'your {a} is {b},you are not old enough to drink')
print(my_dict,MyDicts,sep="\n")

def F1(list):
    for user in list:
        if user['hasCoffee']==False:
            print(f'{user.get('name')} the list of non drinker coffee')
F1(List)