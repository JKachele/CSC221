from math import ceil

def paintWall(wallHeight, wallWidth, paintCost):
    area = wallHeight * wallWidth
    print(f"Wall area: {area:.1f} sq ft")

    # One gallon of paint covers 350 sq ft of wall
    paintNeeded = area / 350
    print(f"Paint needed: {paintNeeded:.3f} gallons")

    # Get cand by rounding up gallons
    cans = ceil(paintNeeded)
    print(f"Cans Needed : {cans} can(s)")

    cost = cans * paintCost
    tax = cost * 0.07    # Tax is 7% or 0.07
    total = cost + tax
    print(f"Paint Cost: ${cost:.2f}")
    print(f"Sales Tax: ${tax:.2f}")
    print(f"Total Cost: ${total:.2f}")

wallHeight1 = float(input())
wallWidth1 = float(input())
paintCost1 = float(input())

paintWall(wallHeight1, wallWidth1, paintCost1)
