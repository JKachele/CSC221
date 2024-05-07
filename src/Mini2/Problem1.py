courseLocations = {"CS101": 3004, "CS102": 4501, "CS103": 6755, "NT110": 1244, "CM241": 1411}
courseInstructors = {"CS101": "Haynes", "CS102": "Alvarado", "CS103": "Rich", "NT110": "Burke", "CM241": "Lee"}
courseTime = {"CS101": "8:00am", "CS102": "9:00am", "CS103": "10:00am", "NT110": "11:00am", "CM241": "1:00pm"}

print("Enter a class name:")
name = input()
print("Class:", name)
print("Room:", courseLocations[name])
print("Instructor:", courseInstructors[name])
print("Time:", courseTime[name])
