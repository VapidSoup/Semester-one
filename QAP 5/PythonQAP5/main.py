# This program was made for One Stop Insurance Company to process data files & create new ones
# created by Dillon Regular
# Created on July 31st 2023


# Imports
import FormatValues as FV
import datetime
CurrDate = datetime.datetime.now()

# Pre loop heading.
print()
print("ONE STOP INSURANCE COMPANY")
print(f"POLICY LISTING AS OF {FV.FDateM(CurrDate)}")
print()
print("POLICY CUSTOMER                POLICY     INSURANCE     EXTRA      TOTAL")
print("NUMBER NAME                     DATE       PREMIUM      COSTS     PREMIUM")
print("=========================================================================")

TotCustCtr = 0
InsurPremAcc = 0
ExtraCostAcc = 0
TotPremAcc = 0

f = open("Policies.dat", "r")

for CustDataLine in f:
    CustLine = CustDataLine.split(",")


    # Detail line information
    PolNum = CustLine[0].strip()
    CustName = CustLine[2].strip() + " " + CustLine[3].strip()
    PolDate = CustLine[1].strip()
    PolDate = datetime.datetime.strptime(PolDate, "%Y-%m-%d")
    InsurPrem = float(CustLine[14].strip())
    # Numbers & answers needed for Extra Costs
    CarsAmnt = float(CustLine[8].strip())
    LiabExtra = CustLine[9].strip()
    GlasExtra = CustLine[10].strip()
    LoanExtra = CustLine[11].strip()

    # Calculation required

    if LiabExtra == "Y":
        LiabCost = 130.00
    else:
        LiabCost = 0

    if GlasExtra == "Y":
        GlasCost = 86.00
    else:
        GlasCost = 0

    if LoanExtra == "Y":
        LoanCost = 58.00
    else:
        LoanCost = 0

    LiabCostTot = LiabCost * CarsAmnt
    GlasCostTot = GlasCost * CarsAmnt
    LoanCostTot = LoanCost * CarsAmnt

    ExtraCost = LiabCostTot + GlasCostTot + LoanCostTot

    TotPrem = ExtraCost + InsurPrem

    # print the detail line
    print(f" {PolNum:<4}  {CustName:<20}   {FV.FDateS(PolDate)}  {FV.FDollar2(InsurPrem):>9s}  {FV.FDollar2(ExtraCost):>9s}  {FV.FDollar2(TotPrem):>9s}")
    # Increment counters
    TotCustCtr += 1
    InsurPremAcc += InsurPrem
    ExtraCostAcc += ExtraCost
    TotPremAcc += TotPrem

print("=========================================================================")
print(f"TOTAL POLICIES: {TotCustCtr:>3}                      {FV.FDollar2(InsurPremAcc):>10s} {FV.FDollar2(ExtraCostAcc):>10s} {FV.FDollar2(TotPremAcc):>10s}")
