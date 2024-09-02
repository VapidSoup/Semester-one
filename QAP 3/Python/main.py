# Program was created to help Honest Henry keep track of his sales
# Created by Dillon Regular June 16th

# Imports
import datetime
import math


# constants
TRANS_RATE = .01
LUX_RATE = .016
HST_RATE = .15
FINANCE_FEE = 39.99

# inputs and validations
while True:
    while True:
        allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
        CustFirName = input("Enter the customer’s first name(Type END to end program): ").title()
        if CustFirName == "":
            print("Error - the customer first name cannot be blank.")
        elif not set(CustFirName).issubset(allowed_char):
            print("Error - Customer first name contains invalid characters.")
        else:
            break
    if CustFirName.upper() == "END":
        break

    while True:
        allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
        CustLasName = input("Enter the customer’s last name: ").title()
        if CustLasName == "":
            print("Error - the customer last name cannot be blank.")
        elif not set(CustLasName).issubset(allowed_char):
            print("Error - Customer last name contains invalid characters.")
        else:
            break

    while True:
        StreetAddress = input("Enter the customers street address: ").title()
        if StreetAddress == "":
            print("Error - Street address cannot be blank.")
        else:
            break

    while True:
        City = input("Enter the customers city: ").title()
        if City == "":
            print("Error - City cannot be blank")
        else:
            break

    while True:
        Province = input("Enter the customers province(NL): ").upper()
        if Province == "":
            print("Error - City cannot be blank.")
        elif len(Province) > 2:
            print("Error - province is defined in two letters (NL).")
        else:
            break

    while True:
        PostalCode = input("Enter the customers Postal Code(a1a1a1): ").upper()
        if PostalCode == "":
            print("Error - The postal code cannot be blank.")
        elif len(PostalCode) != 6:
            print("Error - Postal code must be valid(a1a1a1).")
        else:
            break


    while True:
        PhoneNum = input("Enter the customer’s phone number(XXX XXX XXXX): ")
        if PhoneNum == "":
            print("Error - Phone number cannot be blank.")
        elif len(PhoneNum) != 10:
            print("Error - Phone number must be 10 digits.")
        elif not PhoneNum.isdigit():
            print("Error - Phone number must be 10 digits.")
        else:
            break

    while True:
        allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ0123456789")
        PlateNum = input("Enter the plate number (XXX999): ").upper()

        if PlateNum == "":
            print("Error - Plate number cannot be blank.")
        elif len(PlateNum) != 6:
            print("Error - Plate number must be 6 characters.")
        elif not set(PlateNum).issubset(allowed_char):
            print("Error - Plate number contains invalid characters.")
        else:
            break

    while True:
        CarMake = input("Enter the cars make(i.e Honda): ").title()

        if CarMake == "":
            print("Error – Car make cannot be blank.")
        else:
            break

    while True:
        CarModel =input("Enter the cars model(i.e Civic): ").title()

        if CarModel == "":
            print("Error – car model cannot be blank.")
        else:
            break

    while True:
        CarYear = input("Enter the year of the car: ")
        if CarYear == "":
            print("Error – car year cannot be blank.")
        elif len(CarYear) != 4:
            print("Error – car must exist in a valid year(19XX - 20XX")
        else:
            break


    while True:
        try:
            SellPrice = float(input("Enter the cars selling price(Cannot exceed $50,000): "))
        except:
            print("Error – sell price is not a valid number")
        else:
            if SellPrice > 50000.00:
                print("Error – Sell price cannot exceed $50, 000.")
            else:
                break

    while True:
        try:
            TradePrice = float(input("Enter the trade in price(Cannot exceed sell price): "))
        except:
            print("Error – Trade price is not a valid number.")
        else:
            if TradePrice > SellPrice:
                print("Error – Trade price cannot exceed sell price")
            else:
                break

    while True:
        allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
        SalesPersName = input("Enter the salespersons name: ")

        if SalesPersName =="":
            print("Error - Salespersons name cannot be blank.")
        elif not set(SalesPersName).issubset(allowed_char):
            print("Error - Salespersons name contains invalid characters.")
        else:
            break

    # Calculations-----------------------------------------------------------------

    PriceAfterTrade = SellPrice - TradePrice

    if PriceAfterTrade > 5000.00:
        LicFee = 165.00
    else:
        LicFee = 75.00

    if SellPrice <= 20000.00:
        TransFee = SellPrice * .01
    else:
        TransFee = (SellPrice * .01) + (SellPrice * LUX_RATE)

    Subtotal = PriceAfterTrade + TransFee

    HST = Subtotal * HST_RATE

    TotSalesPrice = Subtotal + HST


    CurrDate = datetime.datetime.now()
    FirstPay = (CurrDate + datetime.timedelta(days=30))

    # print statements --------------------------------------------------------

    print("")
    TodayDate = datetime.datetime.now()
    TodayDateDsp = TodayDate.strftime("%B-%d-%Y")
    print(f"Honest Harry Car Sales                            Invoice Date: {TodayDateDsp:>14}")
    print(f"Used Car Sale and Receipt                         Receipt No:      {CustFirName[0]:>1}{CustLasName[0]:>1}-{PlateNum[3:6]:>3}-{PhoneNum[6:10]:>4}")
    print("")
    SellPriceDsp = "${:,.2f}".format(SellPrice)
    print(f"                                            Sale Price:             {SellPriceDsp:>10s}")
    TradePriceDsp = "${:,.2f}".format(TradePrice)
    print(f"Sold to:                                    Trade Allowance:        {TradePriceDsp:>10s}")
    print("                                            ----------------------------------")
    PriceAfterTradeDsp = "${:,.2f}".format(PriceAfterTrade)
    print(f"     {CustFirName[0]:<1}. {CustLasName:<26}          Price after Trade:      {PriceAfterTradeDsp:>10s}")
    LicFeeDsp = "${:,.2f}".format(LicFee)
    print(f"     {StreetAddress:<29}          License Fee:            {LicFeeDsp:>10s}")
    TransFeeDsp = "${:,.2f}".format(TransFee)
    PostalCode = str(PostalCode)
    print(f"     {City.strip():<19s}, {Province:<2s} {PostalCode:<6s}         Transfer Fee:           {TransFeeDsp:>10s}")

    print("                                            ----------------------------------")
    SubtotalDsp = "${:,.2f}".format(Subtotal)
    print(f"Car Details:                                Subtotal:               {SubtotalDsp:>10s}")
    HSTDsp = "${:,.2f}".format(HST)
    print(f"                                            HST:                    {HSTDsp:>10s}")
    print(f"     {CarYear:<4s} {CarMake:<13} {CarModel:<10}          ----------------------------------")
    TotSalesPriceDsp = "${:,.2f}".format(TotSalesPrice)
    print(f"                                            Total sales price:      {TotSalesPriceDsp:>10s}")
    print("------------------------------------------------------------------------------")
    print("                     Best used cars at the best prices!")
    print("")
    print("                                  Financing       Total        Monthly")
    print("        # Years    # Payments        Fee          Price        Payment")
    print("        --------------------------------------------------------------")
    for Years in range(1, 5):
        NumOfPayments = Years * 12
        FinancingFee = Years * FINANCE_FEE
        TotPrice = TotSalesPrice + FinancingFee
        MonthlyPay = TotPrice / NumOfPayments
        FinancingFeeDsp = "${:,.2f}".format(FinancingFee)
        TotPriceDsp = "${:,.2f}".format(TotPrice)
        MonthlyPayDsp = "${:,.2f}".format(MonthlyPay)
        print(f"           {Years}           {NumOfPayments}          {FinancingFeeDsp:>7s}     {TotPriceDsp:>10s}   {MonthlyPayDsp:>10s}")
    print("        --------------------------------------------------------------")

    CurrDateDsp = CurrDate.strftime("%d-%b-%y")
    FirstPayDsp = FirstPay.strftime("%d-%b-%y")
    print(f"        Invoice date: {CurrDateDsp}          First payment date: {FirstPayDsp} ")
    print("")