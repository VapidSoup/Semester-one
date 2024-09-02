# This program is designed for the St. John's Marina & Yacht Club to keep things organized
# Created by Dillon Regular
# Created Mat 26th

# Lets start with some inputs
SiteNum = int(input("Site Number (1-100): "))
NameMember = input("Members name: ")
PostalCode = input("Postal Code: ").upper()
StrtAddress = input("Street Address: ")
City = input("City: ")
Province = input("Province(XX): ").upper()
PhoneNumber = input("Home Phone Number (XXX XXX-XXXX): ")
CellPhone = input("Cell phone number (XXX XXX-XXXX): ")
TypeMembership = input("MemberShip Type(S/E): ")
AltMembers = int(input("The amount of additional members: "))
WeekSiteCln = input("Weekly site cleaning(Y/N): ").upper()
VideoSurv = input("Video Surveillance(Y/N): ").upper()

# Constants
ALT_MEMBERS_COST = 5
HST_RATE = .15
PROCESS_FEE = 59.99
CANC_FEE_RATE = .60

# calculations
if SiteNum % 2 == 0:
    SiteCharges = 120 + (AltMembers * ALT_MEMBERS_COST)
if SiteNum % 2 == 1:
    SiteCharges = 80 + (AltMembers * ALT_MEMBERS_COST)

if WeekSiteCln == "Y":
    CleanCost = 50
    CleanCostDsp = "YES"
else:
    CleanCost = 0
    CleanCostDsp = "NO"

if VideoSurv == "Y":
    SurvCost = 35
    VideoSurvDsp = "YES"
else:
    SurvCost = 0
    VideoSurvDsp = "NO"

ExtraCharges = CleanCost + SurvCost

SubTotal = SiteCharges + ExtraCharges

HST = SubTotal * HST_RATE

TotMonthCharges = SubTotal + HST

if TypeMembership == "S":
    TypeMembershipDsp = "Standard"
    MonthDues = 75
else:
    TypeMembershipDsp = "Executive"
    MonthDues = 150

TotMonthFees = TotMonthCharges + MonthDues

TotYearFees = TotMonthFees * 12

MonthlyPayMent = (TotYearFees + PROCESS_FEE) / 12

CancelFees = (SiteCharges * 12) * CANC_FEE_RATE


print()
print("      St. John's Marina & Yacht Club      ")
print("           Yearly Member Receipt          ")
print()
print(" ----------------------------------------- ")
print()
print(f" Client Name and Address:")
print()
print(f" {NameMember:<24s}")
print(f" {StrtAddress:<24s}")
print(f" {City:<}, {Province:>2s} {PostalCode:>6s}")
print()
print(f" Phone: {PhoneNumber:<} (H)")
print(f"        {CellPhone:<} (C)")
print()
print(f" Site #: {SiteNum:<3d} Member Type:        {TypeMembershipDsp:>9s} ")
print()
print(f" Alternate members:                     {AltMembers:>2d}")
print(f" Weekly site cleaning:                 {CleanCostDsp:>3s}")
print(f" Video surveillance:                   {VideoSurvDsp:>3s}")
print()
SiteChargesDsp = "${:,.2f}".format(SiteCharges)
print(f" Site charges:                   {SiteChargesDsp:>9s}")
ExtraChargesDsp = "${:,.2f}".format(ExtraCharges)
print(f" Extra charges:                    {ExtraChargesDsp:>7s}")
print("                                 --------- ")
SubtotalDsp = "${:,.2f}".format(SubTotal)
print(f" Subtotal:                       {SubtotalDsp:>9s}")
HSTDsp = "${:,.2f}".format(HST)
print(f" Sales tax (HST):                  {HSTDsp:>7s}")
print("                                 --------- ")
TotMonthChargesDsp = "${:,.2f}".format(TotMonthCharges)
print(f" Total monthly charges:          {TotMonthChargesDsp:>9s}")
MonthDuesDsp = "${:,.2f}".format(MonthDues)
print(f" Monthly dues:                     {MonthDuesDsp:>7s}")
print("                                 --------- ")
TotMonthFeesDsp = "${:,.2f}".format(TotMonthCharges)
print(f" Total monthly Fees:             {TotMonthFeesDsp:>9s}")
TotYearFeesDsp = "${:,.2f}".format(TotYearFees)
print(f" Total Yearly fees:             {TotYearFeesDsp:>10s}")
print()
MonthlyPayMentDsp = "${:,.2f}".format(MonthlyPayMent)
print(f" Monthly payment:                {MonthlyPayMentDsp:>9s}")
print()
print(" ----------------------------------------- ")
print()
print(" Issued: YYYY-MM-DD")
print(" HST Reg No: 549-33-5849-4720-9885 ")
print()
CancelFeesDsp = "${:,.2f}".format(CancelFees)
print(f" Cancellation fee:               {CancelFeesDsp:>9s}")