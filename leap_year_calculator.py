print("Welcome.\nThis program can tell if the entered year is a leap year or not.\nLet's try it!")
year = int(input("Enter a year: "))
if year<1582: #if it's below 1582
    print("The year you entered isn't within the Gregorian calendar period.\nPlease try some other year above 1582")
elif year%4!=0: #if it can't be evenly divided by 4
    print(year,"is a comman year.")
elif year%4==0: #if it can be devided by 4
    if year%100!=0:#if it can't be evenly divided by 100
        print(year,"is a leap year.")
    elif year%400==0:#if it can be evenly divided by 400
        print(year,"is a comman year.")
else:
    print(year,"is a leap year.")
#The year can be evenly divided by 4 it's a leap year unless:
#The year can be evenly divided by 100 it is not a leap year, unless:
#The year is also evenly divisible by 400. Then it is a leap year.
#byIremBuseOzkose  07/27/2022
