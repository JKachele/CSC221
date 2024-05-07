wages = int(input())
intrest = int(input())
unemployment = int(input())
status = int(input())
withheld = int(input())
print()

# Part 1
agi = wages + intrest + unemployment
print(f"AGI: ${agi:,}")
# Exit if agi is over 120,000
if agi > 120000:
    print("Income too high to use this form")
    exit(1)

# Part 2
# Get deductions based on status, if not 2, must be 1
if status == 2:
    deduction = 24000
else :
    deduction = 12000

taxable = agi - deduction
if taxable < 0:
    taxable = 0

print(f"Deduction: ${deduction:,}")
print(f"Taxable income: ${taxable:,}")

# Get tax brackets based on income and status
if (status == 2):
    if taxable <= 20000:
        tax = taxable * 0.1
    elif taxable <= 80000:
        tax = 2000 + ((taxable - 20000) * 0.12)
    else:
        tax = 9200 + ((taxable - 80000) * 0.22)
else:    
    if taxable <= 10000:
        tax = taxable * 0.1
    elif taxable <= 40000:
        tax = 1000 + ((taxable - 10000) * 0.12)
    elif taxable <= 85000:
        tax = 4600 + ((taxable - 40000) * 0.22)
    else:
        tax = 14500 + ((taxable - 85000) * 0.24)
    
tax = round(tax)
print(f"Federal Tax: ${tax:,}")

taxDue = tax - withheld
# If tax is positibe, tax is owed, if negative, tax is returned
if taxDue >= 0:
    print(f"Tax due: ${taxDue:,}")
else:
    refund = taxDue * -1
    print(f"Tax refund: ${refund:,}")

