dict1 = {
  'a': 4,
  'b': 16,
  'c': 3
}

dict2 = {
  'a': 8,
  'b': 2,
  'c': 3
}
count1=0
list1=list(dict1)
list2=[]
for i in dict1.values():
    count2=0
    count1+=1
    
    for j in dict2.values():
        count2+=1
        if count1==count2:
            x=i*j
            list2.append(x)

dict0={x:y for x,y in zip(list1,list2)}
print(dict0)
list0=list(dict0.values())
sum=0
for indexer in list0:
    sum+=indexer
print(sum)


