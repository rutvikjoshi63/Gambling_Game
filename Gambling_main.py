age = input("Please enter your age:  ")
if age.isdigit():
    age = int(age)
    if age >= 18:
        print("Welcome to GAMBLING. This is your LUCKY DAY!")
    elif age == 0 :
        print("You should'nt even use internet!")
        quit()
    else :
        print("You're underage. Wait for", 18-age, "Many years to be eligible. Don't forget to come back ")
else:
    print("Please enter a number only.")
    
