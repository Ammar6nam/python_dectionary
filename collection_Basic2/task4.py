import random

animals={'Alligator':random.randint(0,10),
         'Tiger':random.randint(0,10),
         'Parrot':random.randint(0,10),
         'Hamster':random.randint(0,10),
         'Dolphin':random.randint(0,10)}

deletedElements=[x for x in animals if x[-1]=='r']
for x in deletedElements:
    del animals[x]

print(animals)




# import random



# animals={'Alligator':random.randint(0,10),
#          'Tiger':random.randint(0,10),
#          'Parrot':random.randint(0,10),
#          'Hamster':random.randint(0,10),
#          'Dolphin':random.randint(0,10)}
# d={}

# keyToRemove=[x for x in animals if x[-1]=='r']
# for y in keyToRemove:
#     del animals[y]
# print(animals)