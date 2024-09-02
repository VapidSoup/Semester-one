# This Program feature was created for the NL Chocolate Company
# Created by Dillon Regular

# imports
import datetime
import math


# constants
DAILY_RATE = 85.00
PER_KM = .17
PER_RENT_DAY = 65
HST_RATE = .15

#inputs and validations
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
        OwnedOrRent = input("Was a personal vehicle used, or was one rented(Answer O for owned, R for Rented): ").upper()
        if OwnedOrRent == "":
            print("Error - Answer cannot be blank.")
        elif not set(OwnedOrRent).issubset(allowed_ans):
            print("Error - Answer contains invalid characters.")
        else:
            break

    while True:
        if OwnedOrRent == "O":
            KMTot = float(input("Enter the total number of kilometers travelled (cannot be more than 2000Km): "))
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

    #calculations

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


