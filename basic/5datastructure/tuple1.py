zoo = ('lion', 'tiger', 'cat', 'dog', 'monkey', 'cat') 

print(f'zoo: {zoo}') 

print(f'zoo[2]: {zoo[2]}') # 인덱싱 
print(f'zoo[1:]: {zoo[1:]}') # 슬라이싱 
print(f"'lion' in zoo: {'lion' in zoo}") # 멤버십 테스트 

# zoo[3] = 'spider' 

print(f"zoo.index('tiger'): {zoo.index('tiger')}") 
print(f"zoo.count('cat'): {zoo.count('cat')}")