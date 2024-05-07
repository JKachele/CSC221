import math

def futureInvestmentValue(investmentAmount, monthlyInterest, years):
    # Calculate future value using formula
    investmentValue = investmentAmount * math.pow(1 + monthlyInterest, years * 12)
    return investmentValue

investment = float(input("Enter Investment Amount: "))
# Get rate and devide by 100 ge get from percent to rate
annualRate = float(input("Annual Intrest Rate in percent: ")) / 100

# Loop from 1 to 20
for i in range(1,21):
    # Monthly rate = yearly rate / 12
    value = futureInvestmentValue(investment, annualRate / 12, i)
    print(f"Year {i}: Future Value: {value:.2f}")
