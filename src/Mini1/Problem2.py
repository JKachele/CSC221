import math

def pizzaParty(numPeople, slices, pizzaCost):
    totalSlices = numPeople * slices
    # Cacl numPizzas by dividing slices by 8 and rounding up
    numPizzas = math.ceil(int(totalSlices / 8))
    cost = numPizzas * pizzaCost
    print(f"{numPizzas} Pizzas: ${cost:.2f}")

    # Tax is 7% or 0.07
    tax = cost * 0.07
    delivery = (cost + tax) * 0.2
    print(f"Tax: ${tax:.2f}")
    print(f"Delivery: ${delivery:.2f}")

    total = cost + tax + delivery
    print(f"Total: ${total:.2f}")
    # return total to add up for the weekend
    return total

numPeople1 = int(input())
slices1 = float(input())
pizzaCost1 = float(input())

numPeople2 = int(input())
slices2 = float(input())
pizzaCost2 = float(input())

numPeople3 = int(input())
slices3 = float(input())
pizzaCost3 = float(input())

weekendTotal = 0

# Run pizzaParty function for each day, adding the total to the weekend total
print()
print("Friday Night Party")
weekendTotal += pizzaParty(numPeople1, slices1, pizzaCost1)
print()
print("Saturday Night Party")
weekendTotal += pizzaParty(numPeople2, slices2, pizzaCost2)
print()
print("Sunday Night Party")
weekendTotal += pizzaParty(numPeople3, slices3, pizzaCost3)

print()
print(f"Weekend Total: ${weekendTotal:.2f}")
