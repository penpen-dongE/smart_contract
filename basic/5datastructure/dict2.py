months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May'} 

print(months.get(10))       #값이 존재하지 않을 때 기본값은 None!
print(months.get(10,None)) 
print(months.get(10,0))     #값이 존재하지 않을 때 기본값을 0 으로! 
# print(months[10]) 

keyset = months.keys() 
print('keyset: '+str(keyset)) 

keylist = list(keyset) 
print('keylist: '+ str(keylist)) 

valuesall = months.values() 
print('valuesall: '+ str(valuesall)) 

valuelist = list(valuesall) 
print('valuelist: '+str(valuelist)) 

items = months.items() 
print(items)

itemslist = list(items)
print('itemslist: '+str(itemslist))