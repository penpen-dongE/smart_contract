print(f'True and True:{True and True}') 
print(f'True and False:{True and False}') 
print(f'True and False:{False and False}') # and 연산에서  true and false / false and true(V)) 차이점은? 처리의 효율성!
print(f'True or True:{True or True}') 
print(f'True or False:{True or False}')     # or 연산에서 true or false(V) / false or true 차이점은? 처리의 효율성! 
print(f'False or False:{False or False}') 
print(f'not True:{not True}')               # => and 연산일 때는 false 되는 것이 앞에 오면 더 빠르고 
print(f'not False:{not False}')                # or 연산일 때는 true 되는 것이 앞에 위치하면 처리의 효율이 더 높다! 