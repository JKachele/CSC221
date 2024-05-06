import math

price1 = float(input())
width1 = int(input())
length1 = int(input())

price2 = float(input())
width2 = int(input())
length2 = int(input())

price3 = float(input())
width3 = int(input())
length3 = int(input())

# Step 1
print("Order #1")
area1 = width1 * length1
carpet1 = (area1 * 1.2) * price1

print("Room:", area1, "sq ft")
print("Carpet: $%.2f" % carpet1)

# Step 2
labor1 = area1 * 0.75
print("Labor: $%.2f" % labor1)

# Step 3
subTotal1 = carpet1 + labor1
tax1 = subTotal1 * 0.07
total1 = subTotal1 + tax1
print("Tax: $%.2f" % tax1)
print("Cost: $%.2f" % total1)

print()

# Step 1
print("Order #2")
area2 = width2 * length2
carpet2 = (area2 * 1.2) * price2

print("Room:", area2, "sq ft")
print("Carpet: $%.2f" % carpet2)

# Step 2
labor2 = area2 * 0.75
print("Labor: $%.2f" % labor2)

# Step 3
subTotal2 = carpet2 + labor2
tax2 = subTotal2 * 0.07
total2 = subTotal2 + tax2
print("Tax: $%.2f" % tax2)
print("Cost: $%.2f" % total2)

print()

# Step 1
print("Order #3")
area3 = width3 * length3
carpet3 = (area3 * 1.2) * price3

print("Room:", area3, "sq ft")
print("Carpet: $%.2f" % carpet3)

# Step 2
labor3 = area3 * 0.75
print("Labor: $%.2f" % labor3)

# Step 3
subTotal3 = carpet3 + labor3
tax3 = subTotal3 * 0.07
total3 = subTotal3 + tax3
print("Tax: $%.2f" % tax3)
print("Cost: $%.2f" % total3)

print()
totalSales = total1 + total2 + total3
print("Total Sales: $%.2f" % totalSales)
