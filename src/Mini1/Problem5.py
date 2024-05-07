# Global Constants
HOMEWORK_MAX = 800.0;
QUIZZES_MAX = 400.0;
MIDTERM_MAX = 150.0;
FINAL_MAX = 200.0;
STATUSES = ("UG", "G", "DL")

studentStatus = input()
# Exit if the status is not UG, G, or DL
if studentStatus not in STATUSES:
    print("Error: student status must be UG, G or DL")
    exit(1)

# List of points for hw, quiz, midterm, and final
points = [0.0, 0.0, 0.0, 0.0]
points[0] = float(input())
points[1] = float(input())
points[2] = float(input())
points[3] = float(input())
print()

# Convert points to grades by using the constatnts
grades = [0.0, 0.0, 0.0, 0.0]
grades[0] = (points[0] / HOMEWORK_MAX) * 100
grades[1] = (points[1] / QUIZZES_MAX) * 100
grades[2] = (points[2] / MIDTERM_MAX) * 100
grades[3] = (points[3] / FINAL_MAX) * 100

# Loop through grades to cap at 100%
for i in range(4):
    if grades[i] > 100:
        grades[i] = 100

print(f"Homework: {grades[0]:2.1f}%")
print(f"Quizzes: {grades[1]:2.1f}%")
print(f"Midterm: {grades[2]:2.1f}%")
print(f"Final Exam: {grades[3]:2.1f}%")

# Get grade weights by status
if studentStatus == "UG":
    weights = (0.2, 0.2, 0.3, 0.3)
elif studentStatus == "G":
    weights = (0.15, 0.05, 0.35, 0.45)
else:
    weights = (0.05, 0.05, 0.4, 0.5)

finalGrade = 0
for i, grade in enumerate(grades):
    finalGrade += grade * weights[i]

print(f"{studentStatus} average: {finalGrade:2.1f}%")

if finalGrade >= 90:
    grade = "A"
elif finalGrade >= 80:
    grade = "B"
elif finalGrade >= 70:
    grade = "C"
elif finalGrade >= 60:
    grade = "D"
else:
    grade = "F"

print("Course grade:", grade)
