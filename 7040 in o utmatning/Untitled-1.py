svar = input("Gissa nummer: ") 
tal = 3
while svar != "42":
    if svar < "42":
        print("för litet")
    if svar > "42":
        print("för stort")
    if tal > 1:
        svar = input("Du gissade fel. Gissa på ett annat tal. ")
        tal = tal - 1
    if tal < 1:
        print("Du gissade fel.")
        
print("Rätt")