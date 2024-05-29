natural_case1 = {
  'Movie name': 'James Bond 007: Skyfall',
  'Director': 'Sam Mendes',
  'Production Year': 2012,
  'Duration in minutes': 143,
  'Production countries': ['US', 'UK']
}

natural_case2 = {
  'Company name': 'Digital Career Institute',
  'Street': 'Vulkanstraße',
  'House Number': 1,
  'City': 'Berlin'
}


snack_case1={index1.replace('_',' ').lower():index2 for index1, index2 in natural_case1.items()}
print(snack_case1)







# for i,j in natural_case.items():
#       snake_case1=i.lower().replace(' ', '_') 
#       snake_case2=j
#       snake_case=dict({snake_case1:snake_case2})
#       print(snake_case)



snack_case2={i.lower().replace(' ','_'):j for i,j in natural_case2.items()}
print(snack_case2)




# for i in natural_case:
#     i=i.replace(' ', '_').lower()
#     print(i)


# snake_case = {key.replace(' ', '_').lower(): value for key, value in natural_case.items()}
# print(snake_case)




# x= natural_case.items()
# print(x)



# space=' '
# snake_case=''
# for i in natural_case:
#     i=i.items()
#     print(i.items())
#     i=i.lower()
    # if space in i:
    #     space =='_'
    # print (i)



    # #print(i)
    # for j in i:
    #     if j==' ':
    #         j='_'
    #     else:
    #         pass
    #     #print(j)
    #     snake_case+=j
    #     print (i)
        