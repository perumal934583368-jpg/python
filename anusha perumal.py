#LAND AREA CALCULATORS 
def rectangle():
    l=float(input("Enter Length (ft): "))
    w=float(input("Enter Width (ft): "))
    area=l * w
    print(f"\nRectangle Area={area:.2f} sq.ft")
def square():
    s=float(input("Enter Side (ft): "))
    area=s * s
    print(f"\nSquare Area={area:.2f} sq.ft")
def triangle():
    b=float(input("Enter Base (ft): "))
    h=float(input("Enter Height (ft): "))
    area=0.5 * b * h
    print(f"\nTriangle Area={area:.2f} sq.ft")
def circle():
    r=float(input("Enter Radius (ft): "))
    area=math.pi * r * r
    print(f"\nCircle Area={area:.2f} sq.ft")
# UNIT CONVERTER 
def convert():
    sqft=float(input("Enter Area in Square Feet: "))
    cent=sqft / 435.6
    acre=sqft / 43560
    sqm=sqft * 0.092903
    print("\n Unit Conversion ")
    print("Square Feet :", round(sqft, 2))
    print("Square Meter:", round(sqm, 2))
    print("Cent        :", round(cent, 2))
    print("Acre        :", round(acre, 4))
#  LAND PRICE 
def price():
    area=float(input("Enter Area (sq.ft): "))
    rate=float(input("Enter Price per sq.ft (₹): "))
    total=area * rate
    print("\n Land Price")
    print("Land Area :", area, "sq.ft")
    print("Rate      : ₹", rate)
    print("Total Land Price: ₹", round(total, 2))
# PERIMETER CALCULATORS 
def rectangle_perimeter():
    l=float(input("Enter Length (ft): "))
    w=float(input("Enter Width (ft): "))
    p=2 * (l + w)
    print("\nRectangle Perimeter =", round(p, 2), "ft")
def square_perimeter():
    s=float(input("Enter Side (ft): "))
    p=4 * s
    print("\nSquare Perimeter =", round(p, 2), "ft")
def circle_circumference():
    r=float(input("Enter Radius (ft): "))
    c=2 * math.pi * r
    print("\nCircle Circumference =", round(c, 2), "ft")
# TAX CALCULATORS 
def gst():
    amount=float(input("Enter Land Cost (₹): "))
    gst_amount=amount * 0.18
    total=amount+gst_amount
    print("\n GST Calculator")
    print("GST (18%) =", round(gst_amount, 2))
    print("Total Amount =", round(total, 2))
def stamp_duty():
    value=float(input("Enter Property Value (₹): "))
    duty=value * 0.07
    print("\nStamp Duty (7%)= ₹", round(duty, 2))
def registration_fee():
    value = float(input("Enter Property Value (₹): "))
    fee = value * 0.04
    total = value + fee
    print("\nRegistration Fee (4%) = ₹", round(fee, 2))
    print("Total Cost: ₹", round(total, 2))
# LAND BUDGET CHECKER 
def budget_checker():
    budget=float(input("Enter Your Budget (₹): "))
    rate=float(input("Enter Land Price per sq.ft (₹): "))
    max_area=budget / rate
    print("\n Land Budget Checker")
    print("Your Budget       : ₹", round(budget, 2))
    print("Price per sq.ft   : ₹", round(rate, 2))
    print("Maximum Area      :", round(max_area, 2), "sq.ft")
    print("\nYou can afford approximately",
          round(max_area, 2), "sq.ft of land.")
# PLOT SPLIT CALCULATOR 
def plot_split():
    total_area=float(input("Enter Total Land Area (sq.ft): "))
    plots=int(input("Enter Number of Plots: "))
    if plots <= 0:
        print("Number of plots must be greater than 0.")
        return
    each_plot = total_area / plots
    print("\n Plot Split Calculator")
    print("Total Land Area :", round(total_area, 2), "sq.ft")
    print("Number of Plots :", plots)
    print("Area per Plot   :", round(each_plot, 2), "sq.ft")
# CONSTRUCTION BUDGET 
def construction_budget():
    area=float(input("Enter Built-up Area (sq.ft): "))
    rate=float(input("Enter Construction Cost per sq.ft (₹): "))
    total_cost=area * rate
    print("\n Construction Budget ")
    print("Built-up Area :", round(area, 2), "sq.ft")
    print("Construction Rate : ₹", round(rate, 2))
    print("Estimated Construction Cost : ₹",
          round(total_cost, 2))
#  PLOT COMPARISON 
def plot_comparison():
    print("\n PLOT 1 ")
    area1=float(input("Enter Plot 1 Area (sq.ft): "))
    price1=float(input("Enter Plot 1 Total Price (₹): "))
    print("\n PLOT 2 ")
    area2=float(input("Enter Plot 2 Area (sq.ft): "))
    price2=float(input("Enter Plot 2 Total Price (₹): "))
    rate1=price1 / area1
    rate2=price2 / area2
    print("\n Plot Comparison ")
    print("Plot 1 Price per sq.ft : ₹", round(rate1, 2))
    print("Plot 2 Price per sq.ft : ₹", round(rate2, 2))
    if rate1 < rate2:
       print("\nRecommended Plot: PLOT 1")
       print("Reason: Lower price per sq.ft.")
    elif rate2 < rate1:
       print("\nRecommended Plot: PLOT 2")
       print("Reason: Lower price per sq.ft.")
    else:
       print("\nBoth plots have the same price per sq.ft.")
#   INVESTMENT PROFIT & ROI 
def investment_profit():
    purchase=float(input("Enter Purchase Price (₹): "))
    selling=float(input("Enter Expected Selling Price (₹): "))
    profit=selling-purchase
    roi=(profit/purchase) * 100
    print("\n Investment Analysis ")
    print("Purchase Price :", round(purchase, 2))
    print("Selling Price  :", round(selling, 2))
    if profit > 0:
        print("Expected Profit : ₹", round(profit, 2))
        print("ROI             :", round(roi, 2), "%")
    elif profit < 0:
        print("Expected Loss   : ₹", round(abs(profit), 2))
        print("ROI             :", round(roi, 2), "%")
    else:
        print("No Profit/No Loss")
# PARKING CAPACITY
def parking_capacity():
    print("\n--- Parking Capacity Estimator ---")
    print("1. Enter Area → Find Number of Cars")
    print("2. Enter Number of Cars → Find Required Area")
    choice = input("\nEnter your choice: ")
# One car requires approximately 200 sq.ft
    if choice == "1":
        area = float(input("Enter Available Area (sq.ft): "))
        spaces = int(area / 165)
        print("\nParking Result")
        print("Available Area :", round(area, 2), "sq.ft")
        print("Estimated Cars :", spaces)
        print("\nNote: This is an approximate estimation.")
    elif choice == "2":
            cars = int(input("Enter Number of Cars: "))
            area = cars * 165
            print("\n Parking Result")
            print("Number of Cars :", cars)
            print("Required Area  :", round(area, 2), "sq.ft")
            print("\nNote: This is an approximate estimation.")
    else:
            print("\n Invalid choice")
                
# LAND DECISION ADVISOR 
def land_advisor():
    budget=float(input("Enter Your Budget (₹): "))
    area=float(input("Enter Required Land Area (sq.ft): "))
    rate=float(input("Enter Land Price per sq.ft (₹): "))
    total_cost=area * rate
    print("\n LAND DECISION ADVISOR ")
    print("Your Budget       : ₹", round(budget, 2))
    print("Required Area     :", round(area, 2), "sq.ft")
    print("Price per sq.ft   : ₹", round(rate, 2))
    print("Total Land Cost   : ₹", round(total_cost, 2))
    if total_cost <= budget:
        remaining=budget - total_cost
        print("\n DECISION: AFFORDABLE")
        print("You can afford this land.")
        print("Remaining Budget : ₹", round(remaining, 2))
    else:
        extra=total_cost - budget
        print("\n DECISION: OVER BUDGET")
        print("You need an additional ₹",round(extra, 2))
        affordable_area=budget/rate
        print("Affordable Area at this rate :",round(affordable_area, 2), "sq.ft")
while True:
    print("LAND CALCULATOR")
    print("\n Basic Calculators")
    print("1. Rectangle Area")
    print("2. Square Area")
    print("3. Triangle Area")
    print("4. Circle Area")
    print("5. Unit Converter")
    print("6. Land Price Calculator")
    print("7. Rectangle Perimeter")
    print("8. Square Perimeter")
    print("9. Circle Circumference")
    print("10. GST Calculator")
    print("11. Stamp Duty Calculator")
    print("12. Registration Fee Calculator")
    print("13. Land Budget Checker")
    print("14. Plot Split Calculator")
    print("15. Construction Budget Estimator")
    print("16. Plot Comparison")
    print("17. Investment Profit & ROI")
    print("18. Parking Capacity Estimator")
    print("19. Land Decision Advisor")
    print("20. Exit")
    choice=input("\nEnter your choice: ")
    if choice=="1":
        rectangle()
    elif choice=="2":
        square()
    elif choice=="3":
        triangle()
    elif choice=="4":
        circle()
    elif choice=="5":
        convert()
    elif choice=="6":
        price()
    elif choice=="7":
        rectangle_perimeter()
    elif choice=="8":
        square_perimeter()
    elif choice=="9":
        circle_circumference()
    elif choice=="10":
        gst()
    elif choice=="11":
        stamp_duty()
    elif choice=="12":
        registration_fee()
    elif choice=="13":
        budget_checker()
    elif choice=="14":
        plot_split()
    elif choice=="15":
        construction_budget()
    elif choice=="16":
        plot_comparison()
    elif choice=="17":
        investment_profit()
    elif choice=="18":
        parking_capacity()
    elif choice=="19":
        land_advisor()
    elif choice=="20":
        print("\nThank You for using Land Calculator")
    else:
        print("\n Invalid choice")
