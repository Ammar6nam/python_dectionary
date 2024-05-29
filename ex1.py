ourList = {
    'Tomato':{
        'Name':'Tomato',
        'Quantity_g':500,
        'Price_€':1.99
    },
    
    'Onion':{
        'Name':'Onion',
        'Quantity_g':100,
        'Price_€':0.60
    },
    
    'Rice':{
        'Name':'Rice',
        'Quantity_g':400,
        'Price_€':1.5
    },

    'Chicken':{
        'Name':'Chicken',
        'Quantity_g':600,
        'Price_€':7.88
    },
    
    'Bread':{
        'Name':'Bread',
        'Quantity_g':100,
        'Price_€':0.40
    },

    'Milk':{
        'Name':'Milk',
        'Quantity_L':200,
        'Price_€':1.40
    },
    
    'Coffee':{
        'Name':'Coffee',
        'Quantity_L':500,
        'Price_€':3.99
    }


}
#print('The first list:',ourList,sep='\n')
TotalPrice=ourList['Bread']['Price_€']+ourList['Onion']['Price_€']+ourList['Rice']['Price_€']+ourList['Tomato']['Price_€']+ourList['Chicken']['Price_€']+ourList['Milk']['Price_€']+ourList['Coffee']['Price_€']
#print('The Total price is:',TotalPrice,'€',sep=' ')
newList={
    'Banana':{
        'Name':'Banana',
        'Quantity_g':500,
        'Price_€':1.10
    },
    'Ananas':{
        'Name':'Ananas',
        'Quantity_g':600,
        'Price_€':2.6
    },
    'Apple':{
        'Name':'Apple',
        'Quantity_g':600,
        'Price_€':2.6
    }
}
ourList.update(newList)
#print('New List:',newList,sep='\n')
print('Our List updated:',ourList,sep="\n")
DletedElementList= ourList.pop('Milk')
print('Our List updated after delet Milk:',ourList,sep="\n")
ourList['Tomato']['Quantity_g']=400
print('Our List updated ever!:',ourList,sep="\n")