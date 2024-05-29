string=input('Enter your word: ')
list1=list(string.lower())
print(list1)
sortedList=sorted(list1)
a=''
for x in sortedList:
    if x not in a:
        a+=x

# print(a)


dict2={j:list1.count(j) for j in a }
print(dict2)

# for i in string:
#         count1=string.count(i)
    
#         dict1={i:count1}
#         print(dict1)