# This program was made for One Stop Insurance Company to process data files & create new ones
# created by Dillon Regular
# Created on July 31st 2023


# Imports
import FormatValues as FV
import datetime
CurrDate = datetime.datetime.now()

# Constants
HST_RATE = 00.15

# Pre loop heading.
print()
print("ONE STOP INSURANCE COMPANY")
print(f"MONTHYL PAYMENT LISTING AS OF {FV.FDateM(CurrDate)}")
print()
print("POLICY CUSTOMER             TOTAL                 TOTAL       MONTHYL")
print("NUMBER NAME                PREMIUM      HST       COST        PAYMENT")
print("======================================================================")

TotCustCtr = 0
TotPremAcc = 0
HSTAcc = 0
TotCostAcc = 0
MonPayAcc = 0

f = open("Policies.dat", "r")

for CustDataLine in f:
    CustLine = CustDataLine.split(",")


    # Detail line information
    PolNum = CustLine[0].strip()
    CustName = CustLine[2].strip() + " " + CustLine[3].strip()
    MonOrFullPay = CustLine[12].strip()
    InsurPrem = float(CustLine[14].strip())
    # Numbers & answers needed for Extra Costs
    CarsAmnt = float(CustLine[8].strip())
    LiabExtra = CustLine[9].strip()
    GlasExtra = CustLine[10].strip()
    LoanExtra = CustLine[11].strip()

    if MonOrFullPay == "Monthly":

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

        HST = TotPrem * HST_RATE

        TotCost = HST + TotPrem

        MonPay = (TotCost + 39.99) / 12

        # print the detail line
        print(f"{PolNum:<4} {CustName:<20}  {FV.FDollar2(TotPrem):>9s}   {FV.FDollar2(HST):>7s}   {FV.FDollar2(TotCost):>9s}   {FV.FDollar2(MonPay):>9s}")
        # Increment counters
        TotCustCtr += 1
        TotPremAcc += TotPrem
        HSTAcc += HST
        TotCostAcc += TotCost
        MonPayAcc += MonPay

print("======================================================================")
print(f"TOTAL POLICIES: {TotCustCtr:>3}       {FV.FDollar2(TotPremAcc):>10s} {FV.FDollar2(HSTAcc):>9s}  {FV.FDollar2(TotCostAcc):>10s}  {FV.FDollar2(MonPayAcc):>10s}")
