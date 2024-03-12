def SurvivalDuration():
    Valid = False
    while not Valid:
        age = input("What's your age? ")
        ValidateEntry = str(age)
        for ch in ValidateEntry:
            if ch not in "0123456789":
                Valid = False
                print("Invalid Response. Please enter age in positive integer.")
                break
            else:
                Valid = True
                age = int(age)

    Valid = False
    while not Valid:
        print()
        print("Options")
        print()
        print("Months")
        print("Weeks")
        print("Days")
        print("Hours")
        print("Minutes")
        print("Seconds")
        print()
        print("Note: You can write the first letter or the full name of the time unit (Use initial Mo for Months, and Mi for Minutes).")
        option = str(input("Enter your option: ")).lower()
        ValidEntries = ["mo","months","w","weeks","d","days","h","hours","mi","minutes","s","seconds"]
        if option in ValidEntries:
            Valid = True
        else:
            print("\nInvalid Response. Please try again.")

    print()
    if option == "mo" or option == "months":
        result = age*12
        print("You lived for {0} months.".format(result))
    elif option == "w" or option == "weeks":
        result = age*52.1429
        print("You lived for {0} weeks.".format(result))
    elif option == "d" or option == "days":
        result = age*365.25
        print("You lived for {0} days.".format(result))
    elif option == "h" or option == "hours":
        result = age*365.25*24
        print("You lived for {0} hours.".format(result))
    elif option == "mi" or option == "minutes":
        result = age*365.25*24*60
        print("You lived for {0} minutes.".format(result))
    elif option == "s" or option == "seconds":
        result = age*365.25*24*60*60
        print("You lived for {0} seconds.".format(result))

SurvivalDuration()