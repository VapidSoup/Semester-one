# this program was created by dillon regular for the one stop insurance company to show their sales
# created on July 23rd 2023

#Library
import matplotlib.pyplot as plt

def Monthly_Sales():
    MonthlySales = []
    Months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]



    for month in Months:
        try:
            Sales = float(input(f"Enter total sales for {month}: $"))
            MonthlySales.append(Sales)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return None

    return MonthlySales

def Sales_Graph(months, sales):
    plt.figure(figsize=(10, 6))
    plt.bar(months, sales, color='purple')
    plt.xlabel("Months")
    plt.ylabel("Total Sales ($)")
    plt.title("Total Sales per Month")
    plt.grid(axis='y')
    plt.show()

def main():
    print("Please enter the total sales for each month from January to December: ")
    MonthlySales = Monthly_Sales()

    if MonthlySales:
        Months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        Sales_Graph(Months, MonthlySales)

