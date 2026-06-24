# Ejercicios de Sintaxis
# Jaime C Smith
# 05/21/2026

"""
Given n grades for a student, this program calculates:
- How many grades are passing (>= 70).
- How many grades are failing (< 70).
- The average of all grades.
- The average of passing grades.
- The average of failing grades.
"""

# 1. Initialize counters and accumulators
grade_counter = 1

total_grades = int(input("Enter the total number of grades: "))

passed_count = 0
failed_count = 0

passed_sum = 0.0
failed_sum = 0.0
total_sum = 0.0

# 2. Loop through all grades
while grade_counter <= total_grades:
    print(f"\nEnter grade number {grade_counter}:")
    current_grade = float(input("Grade: "))

    # Add to total sum for overall average
    total_sum += current_grade

    # Classify as passed or failed
    if current_grade < 70:
        failed_count += 1
        failed_sum += current_grade
    else:
        passed_count += 1
        passed_sum += current_grade

    grade_counter += 1

# 3. Compute averages, avoiding division by zero
overall_average = total_sum / total_grades if total_grades > 0 else 0

passed_average = (
    passed_sum / passed_count if passed_count > 0 else 0
)

failed_average = (
    failed_sum / failed_count if failed_count > 0 else 0
)

# 4. Show results
print("\nResults")
print("-------")
print("Number of passing grades (>= 70):", passed_count)
print("Number of failing grades (< 70):", failed_count)
print("Average of all grades:", overall_average)
print("Average of passing grades:", passed_average)
print("Average of failing grades:", failed_average)