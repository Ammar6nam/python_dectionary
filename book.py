books = {
  'Harry Potter And The Sorcerer\'s Stone': 1241100000,
  'Harry Potter And The Chamber Of Secrets': 771300000,
  'Harry Potter And The Prisoner Of Azkaban': 65210000,
  'Harry Potter And The Goblet Of Fire': 645600000,
  'Harry Potter And The Order Of The Phoenix': 635600000,
  'Harry Potter And The Half Blood Prince': 661300000,
  'Harry Potter And The Deathly Hallows ': 652200000,
}

sortedBooks=sorted(books.items())
#print(sortedBooks)

result1=[]
result3=[]

for i,j in books.items():
    # i1=i.index()
    # print(i1)
    result1.append(j)
result2=reversed((sorted(result1)))
for x in result2:
    result3.append(x)
#print(result3)
index=0
numbersList=[]
while index < 3:
    numbersList.append(result3[index])
    index+=1
#print(result)
namesList=[]
reversedDictBooks={str(y):x for x,y in books.items()}
#print(reversedDictBooks)

for index1 in numbersList:
    namesList.append (reversedDictBooks[str(index1)])
#print(namesList)

index2=0
while index2<3:
    print(f'{index2+1}. {namesList[index2]}: {numbersList[index2]} ')
    index2+=1

finalDictinary={a:b for a in namesList for b in numbersList}
print(finalDictinary)


# Create a dictionary to map numbers to book titles
# number_to_title = {copies_sold: title for title, copies_sold in books.items()}
# print(number_to_title)
# print('\n')
# print(books)

# Find the names of books for the highest numbers
# top_books = [number_to_title[number] for number in result]

# Display the names of the top books
# for book in top_books:
#     print(book)

# oppesit={j:i for i,j in books.items()}
# print(oppesit)

