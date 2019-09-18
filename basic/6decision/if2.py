score = int(input("당신의 점수는?"))

if score >= 90: 
    print(f'score: {score}') 
    print("A grade") 

if score == 100: 
    print("You are perfect.") 
elif score >= 80: 
    print("B grade") 
elif score >= 70: 
    print("C grade") 
else: 
    print("F grade")