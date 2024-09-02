# This program was created for One Stop Insurance Company to enter and calculate new insurance info for its customers
# Created By Dillon Regular
# Created on July 23rd, 2023

# Imports
import FormatValues as FV
import datetime
CurrDate = datetime.datetime.now()

import dateutil
from dateutil.relativedelta import *


# Fun functions & lists

cadProv = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'ON', 'PE', 'QC', 'SK']


def is_valid_number(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False


validAnswer = ['Y', 'N']

fullOrMonthly = ['Full', 'Monthly']

# read text file.
f = open('OSICDef.dat', 'r')
NEXT_POLICY_NUM = int(f.readline())
BASIC_PREM = float(f.readline())
ADD_CARS_DISC = float(f.readline())
EXTRA_LIAB_COV = float(f.readline())
GLAS_COV = float(f.readline())
CAR_LOAN_COV = float(f.readline())
HST_RATE = float(f.readline())
PROC_FEE_MON_PAY = float(f.readline())
f.close()

# user Inputs & validations

while True:
    CustFirNam = input("Enter the customers first name: ").title()
    CustLasNam = input("Enter the customers last name: ").title()
    CustAdd = input("Enter the customers address: ").title()
    while True:
        CustProv = input("Enter the customers province(XX format): ").upper()
        if CustProv not in cadProv:
            print("Error - Must be a valid province in XX form.")
        else:
            break
    CustPostCod = input("Enter the customers postal code(X1X1X1): ").upper()
    CustPhonNum = input("Enter the customers phone number(1234567890): ")
    while True:
        AmntCarsInsur = int(input("Enter the amount of cars getting insured: "))
        if not is_valid_number(AmntCarsInsur):
            print("Error - must be a valid number")
        else:
            break
    while True:
        ExtraLiab = input("Would the customer like extra liability insurance, up to $1m?(Y or N): ").upper()
        if ExtraLiab not in validAnswer:
            print("Error - Must answer with Y or N.")
        if ExtraLiab == "":
            print("Error - cannot be blank")
        else:
            break
    while True:
        GlasCov = input("Would the customer like glass coverage?(Y or N): ").upper()
        if GlasCov not in validAnswer:
            print("Error - Must answer with Y or N.")
        if GlasCov == "":
            print("Error - cannot be blank")
        else:
            break
    while True:
        LoanCar = input("Would the customer like a loaner car?(Y or N): ").upper()
        if LoanCar not in validAnswer:
            print("Error - Must answer with Y or N.")
        if LoanCar == "":
            print("Error - cannot be blank")
        else:
            break
    while True:
        FullOrMon = input("Would the customer like to pay in full or by monthly payments?(Full or Monthly): ").title()
        if FullOrMon not in fullOrMonthly:
            print("Error - Must answer with Full or Monthly.")
        if FullOrMon == "":
            print("Error - cannot be blank")
        else:
            break

    # it is ze calculations yes
    ExtraCarDisc = 869.00 - (869.00 * 0.25)
    InsurPremCost = 869.00 + ((AmntCarsInsur - 1) * ExtraCarDisc)
    if ExtraLiab == "Y":
        ExtraLiabCost = AmntCarsInsur * 130.00
    else:
        ExtraLiabCost = 0
    if GlasCov == "Y":
        GlasCovCost = AmntCarsInsur * 86.00
    else:
        GlasCovCost = 0
    if LoanCar == "Y":
        LoanCarCost = AmntCarsInsur * 58.00
    else:
        LoanCarCost = 0

    ExtraCostTot = ExtraLiabCost + GlasCovCost + LoanCarCost + InsurPremCost

    InsurPremTot = BASIC_PREM + ExtraCostTot

    HST = InsurPremTot * HST_RATE

    CostTot = HST + InsurPremTot

    if FullOrMon == "Monthly":
        MonPay = (PROC_FEE_MON_PAY + CostTot) / 8
    if FullOrMon == "Full":
        MonPay = 0



    InvoiDate = CurrDate

    NextPayDate = CurrDate.replace(day=1) + relativedelta(months=1)

    # lets print a receipt
    print()
    print(" "*31, "ONE STOP INSURANCE")
    print("-"*80)
    print(" Customer information                               Payment Information")
    print("-" * 80)
    print(f" Name: {CustFirNam + ' ' + CustLasNam:<20}               | Cars being insured:               {AmntCarsInsur:>2}")
    print(f" Address: {CustAdd:<20}            | Insurance premium Cost:   {FV.FDollar2(InsurPremCost):>10s}")
    print(f" Province: {CustProv:<2}                             | Extra liability cost:     {FV.FDollar2(ExtraLiabCost):>10s}  ")
    print(f" Postal code: {CustPostCod:<7}                     | Glass coverage cost:      {FV.FDollar2(GlasCovCost):>10s}")
    print(f" Phone Number: {CustPhonNum:<10}                 | Loaner car cost:          {FV.FDollar2(LoanCarCost):>10s}")
    print(f"                                          | Total cost of extras:     {FV.FDollar2(ExtraCostTot):>10s}")
    print(f"                                          | Insurance premium total:  {FV.FDollar2(InsurPremTot):>10s}")
    print(f"                                          | HST:                      {FV.FDollar2(HST):>10s}")
    print(f"                                          | Total cost:               {FV.FDollar2(CostTot):>10s}")
    print("-" * 80)
    if FullOrMon == "Monthly":
        print(f" The monthly payment for the next 8 months: {FV.FDollar2(MonPay):<10s} ")
        print(f" First day of payment: {FV.FDateM(NextPayDate)}")
    if FullOrMon == "Full":
        print(f" Customer is to pay {FV.FDollar2(CostTot)}")
    print("-" * 80)
    print(f" Invoice Date: {FV.FDateM(InvoiDate)}")
    print(" "*35, "Thank you!")
    print()
    print()

    # save values to the file

    f = open("Policies.dat", "a")
    f.write(f"{NEXT_POLICY_NUM}, ")
    f.write(f"{InvoiDate}, ")
    f.write(f"{CustFirNam}, ")
    f.write(f"{CustLasNam}, ")
    f.write(f"{CustAdd}, ")
    f.write(f"{CustProv}, ")
    f.write(f"{CustPostCod}, ")
    f.write(f"{CustPhonNum}, ")
    f.write(f"{AmntCarsInsur}, ")
    f.write(f"{ExtraLiab}, ")
    f.write(f"{GlasCov}, ")
    f.write(f"{LoanCar}, ")
    f.write(f"{FullOrMon}, ")
    f.write(f"{FV.FDollar2(MonPay)}, ")
    f.write(f"{InsurPremTot}\n")
    f.close()
    print("Customer data successfully saved ...")
    print()
    NEXT_POLICY_NUM += 1

    f = open('OSICDef.dat', 'w')
    f.write(f"{str(NEXT_POLICY_NUM)}\n")
    f.write(f"{str(BASIC_PREM)}\n")
    f.write(f"{str(ADD_CARS_DISC)}\n")
    f.write(f"{str(EXTRA_LIAB_COV)}\n")
    f.write(f"{str(GLAS_COV)}\n")
    f.write(f"{str(CAR_LOAN_COV)}\n")
    f.write(f"{str(HST_RATE)}\n")
    f.write(f"{str(PROC_FEE_MON_PAY)}\n")
    f.close()

    Cont = input("Would you like to enter another policy?(Y or N): ").upper()
    if Cont not in validAnswer:
        print("Error - Must answer with Y or N.")
    if Cont == "N":
        break

