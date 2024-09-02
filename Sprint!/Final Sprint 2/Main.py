import datetime
import pyfiglet


# Function for tax calculation
def calculate_tax(income):
    tax_rate = 0.15
    tax_amount = income * tax_rate
    return tax_amount


# Function for getting the current date
def get_current_date():
    current_date = datetime.date.today()
    return current_date


while True:
    # Display the menu options
    print("Menu:")
    print("1. Enter an Employee Travel Claim")
    print("2. Fun Interview Question")
    print("3. Your employee info")
    print("4. Nametag!")
    print("5. Quit Program")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        # Perform actions for Option 1
        print("You selected Option 1: Enter an Employee Travel Claim")
        # Write your code for Option 1 here
        # imports
        import datetime
        import math

        # constants
        DAILY_RATE = 85.00
        PER_KM = .17
        PER_RENT_DAY = 65
        HST_RATE = .15

        # inputs and validations
        while True:
            while True:

                EmployeeNum = input("Enter your employee number (Type END to end program): ").upper()
                allowed_dig = set("1234567890END")
                if EmployeeNum.upper() == "END":
                    print("Thank you for using our services.")
                    break
                elif len(EmployeeNum) != 5:
                    print("Error - the employee number must be 5 digits long.")
                elif not set(EmployeeNum).issubset(allowed_dig):
                    print("Error - employee number contains invalid characters.")
                else:
                    break
            if EmployeeNum.upper() == "END":
                break

            while True:
                allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
                EmployeeFirstName = input("Enter the employees first name: ").title()
                if EmployeeFirstName == "":
                    print("Error - First name cannot be blank.")
                elif not set(EmployeeFirstName).issubset(allowed_char):
                    print("Error - First name contains invalid characters.")
                else:
                    break

            while True:
                EmployeeLastName = input("Enter the employees last name: ").title()
                if EmployeeLastName == "":
                    print("Error - Last name cannot be blank.")
                elif not set(EmployeeLastName).issubset(allowed_char):
                    print("Error - Last name contains invalid characters.")
                else:
                    break

            TripLocation = input("Enter the trip location: ").title()

            from datetime import datetime, timedelta

            while True:
                StartDateInp = input("Enter the start date in DD-Mon-YY format (I.E 12-Jan-22): ")
                try:
                    StartDate = datetime.strptime(StartDateInp, "%d-%b-%y")
                    break
                except ValueError:
                    print("Error - date format is invalid.")

            while True:
                EndDateInp = input("Enter the end date in DD-Mon-YY format (I.E 12-Jan-22): ")
                try:
                    EndDate = datetime.strptime(EndDateInp, "%d-%b-%y")
                    if EndDate <= StartDate + timedelta(days=7):
                        break
                    else:
                        print("Error - End date has to within 7 days.")
                except ValueError:
                    print("Error - date format is invalid.")

            NumDays = EndDate - StartDate
            print("Difference in days: ", NumDays.days)

            while True:
                allowed_ans = set("OR")
                OwnedOrRent = input(
                    "Was a personal vehicle used, or was one rented(Answer O for owned, R for Rented): ").upper()
                if OwnedOrRent == "":
                    print("Error - Answer cannot be blank.")
                elif not set(OwnedOrRent).issubset(allowed_ans):
                    print("Error - Answer contains invalid characters.")
                else:
                    break

            while True:
                if OwnedOrRent == "O":
                    KMTot = float(
                        input("Enter the total number of kilometers travelled (cannot be more than 2000Km): "))
                    if KMTot > 2000.00:
                        print("Error - Total amount of kilometers cannot exceed 2000.")
                    elif KMTot == "":
                        print("Error - Value cannot be blank.")
                    else:
                        break

            while True:
                allowed_claim = set("SE")
                ClaimType = input("Enter the claim type(S for standard, E for Executive): ").upper()
                if ClaimType == "":
                    print("Error - Claim type cannot be blank.")
                elif not set(ClaimType).issubset(allowed_claim):
                    print("Error - Answer contains invalid characters.")
                else:
                    break

            # calculations

            PerDiem = NumDays.days * DAILY_RATE

            if OwnedOrRent == "O":
                MileageAmt = PER_KM * KMTot
            elif OwnedOrRent == "R":
                KMTot = 0
                MileageAmt = PER_RENT_DAY * NumDays.days

            if NumDays.days > 3:
                DaysBonus = 100.00
            else:
                DaysBonus = 0

            if KMTot > 1000.00:
                KmBonus = KMTot * .21
            else:
                KmBonus = 0

            if ClaimType == "E":
                ClaimBonus = 45.00
            else:
                ClaimBonus = 0

            if datetime(StartDate.year, 12, 15) <= StartDate <= datetime(StartDate.year, 12, 22):
                HolidayBonus = NumDays.days * 50.00
            else:
                HolidayBonus = 0

            Bonus = DaysBonus + KmBonus + ClaimBonus + HolidayBonus

            ClaimAmount = PerDiem + MileageAmt + Bonus

            HST = HST_RATE * ClaimAmount

            ClaimTotal = HST + ClaimAmount

            # print statements

            print("")
            print("")
            print("Employee number:", EmployeeNum)
            print("Employees first name:", EmployeeFirstName)
            print("Employees last name:", EmployeeLastName)
            print("Location of trip:", TripLocation)
            print("")
            print(f"The start date of trip: {StartDate.date()}")
            print(f"The end date of the Trip: {EndDate.date()}")
            print(f"Number of days away: {NumDays.days}")
            print("")
            print("Used personal vehicle or rented:", OwnedOrRent)
            if OwnedOrRent == "O":
                KMTotDSP = "{:,.2f}".format(KMTot)
                print(f"Total kilometers travelled: {KMTotDSP}")
            else:
                print("Rented")
            print("")
            print("Type of claim:", ClaimType)
            print("")
            PerDiemDsp = "${:,.2f}".format(PerDiem)
            print(f"Per Diem amount: {PerDiemDsp}")
            MileageAmtDSP = "${:,.2f}".format(MileageAmt)
            print(f"The mileage cost of the trip: {MileageAmtDSP}")
            BonusDsp = "${:,.2f}".format(Bonus)
            print(f"Bonus Amount:{BonusDsp}")
            print("")
            HSTDsp = "${:,.2f}".format(HST)
            print(f"HST: {HSTDsp}")
            ClaimAmountDSP = "${:,.2f}".format(ClaimAmount)
            print(f"Claim amount: {ClaimAmountDSP}")
            ClaimTotalDSP = "${:,.2f}".format(ClaimTotal)
            print(f"Claim total: {ClaimTotalDSP}")
            print("")


    elif choice == "2":
        # Perform actions for Option 2
        print("You selected Option 2: Fun Interview Question")
        # Write your code for Option 2 here
        num_iterations = 100

        for num in range(1, num_iterations + 1):
            output = ""

            if num % 5 == 0:
                output += "Fizz"

            if num % 8 == 0:
                output += "Buzz"

            if num % 5 == 0 and num % 8 == 0:
                output = "FizzBuzz"

            if output == "":
                output = num

            if output == "Fizz":
                print(f"{num}: Fizz")
            elif output == "Buzz":
                print(f"{num}: Buzz")
            elif output == "FizzBuzz":
                print(f"{num}: FizzBuzz")
            else:
                print(num)

            if num % 10 == 0:
                print()  # Print a new line after every 10 numbers

        print("\nPress any key to continue ...")
        input()



    elif choice == "3":
        # Perform actions for Option 3
        print("")
        print("You selected Option 3: Your Employee Info")
        # Write your code for Option 3 here
        while True:
            import datetime

            # Input employee information
            print("")
            NameFirst = input("What is your first name: ").title()
            NameLast = input("What is your last name?: ").title()
            NumPhone = input("What is your phone number?(no area code): ")
            DateCurr = datetime.date.today()
            while True:
                DateStartInp = input("What is you start date?(DD-Mon-YY, ie 31-Jan-22): ")
                try:
                    DateStart = datetime.datetime.strptime(DateStartInp, "%d-%b-%y").date()
                    break
                except ValueError:
                    print("Error - date format is invalid.")

            while True:
                DateBirthInp = input("When's your Birthday?(DD-Mon-YY, ie 31-Jan-22): ")
                try:
                    DateBirth = datetime.datetime.strptime(DateBirthInp, "%d-%b-%y").date()
                    break
                except ValueError:
                    print("Error - date format is invalid.")

            AgeCurrDelta = DateCurr - DateBirth
            AgeCurr = AgeCurrDelta.days / 365
            AgeOfEmploy = DateCurr - DateStart
            # Create the message
            print("")
            print(f"Hello, {NameLast} {NameFirst}!")
            print("Your employee information:")
            print(f"Phone number: {NumPhone}")
            print(f"Today is: {DateCurr}")
            print("So if you started on", DateStart)
            print(f"you've been employed for {AgeOfEmploy.days} days, congratulations!")
            print("Your date of birth is", DateBirth, "?")
            AgeCurrDsp = "{:,.0f}".format(AgeCurr)
            print(f"so that means you are {AgeCurrDsp:<2s} years old!")
            print("")
            # Prompt to continue

            All_Choice = set("YESNO")
            MoreInfo = input("Did you want to do another person?(Yes or No): ").upper()
            if MoreInfo == "NO":
                break
            if MoreInfo == "":
                print("Error - Answer cannot be blank.")
            elif not set(MoreInfo).issubset(All_Choice):
                print("Error - Answer contains invalid characters.")



    elif choice == "4":
        # Perform actions for Option 4
        print("You selected Option 4: NameTag!")
        # Write your code for Option 4 here
        while True:
            NameText = input("Enter the the name you want on your name tag: ")
            try:
                NameArt = pyfiglet.figlet_format(NameText, font="starwars")
                print("Here is your Nametag:")
                print(NameArt)
            except pyfiglet.FigletError as e:
                print("Error - unsupported characters")
            Acceptable = set("YN")
            Another = input("would you like another nametag?(Reply Y or N)").upper()
            if Another == "N":
                break
                # This part of the program print out a cool font style ACII style writing, this is done in the star war font using the pyfiglet library.



    elif choice == "5":
        # Exit the program
        print("Exiting the program...")
        break

    else:
        # Handle invalid input
        print("Invalid choice. Please enter a valid option.")

# Example usage of the additional functions

# Calculate tax for an income of $50,000
income = 50000
tax_amount = calculate_tax(income)
print(f"Tax amount for an income of ${income} is ${tax_amount}")

# Get the current date
current_date = get_current_date()
print("Current date:", current_date)
