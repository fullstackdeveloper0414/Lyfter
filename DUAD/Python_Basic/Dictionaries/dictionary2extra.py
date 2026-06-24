"""
Ejercicios extra de Diccionarios
Jaime C Smith
05/23/2026
"""

# Group employees by department.
#
# Given a list of employees where each employee has:
#   - name
#   - email
#   - department
#
# Create a dictionary that groups employees by their department.
# The result will look like:
# {
#   "Ventas": [ {...employee1...}, {...employee2...} ],
#   "TI":     [ {...employee...} ],
#   "RRHH":   [ {...employee...} ],
# }

# Example input list
employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

# Dictionary that will group employees by department
# Key: department name (string)
# Value: list of employee dictionaries belonging to that department
employees_by_department = {}

# Iterate through each employee in the list
for employee in employees:
    # Read the department of the current employee
    department = employee["department"]

    # If this department is not yet in the dictionary, initialize it with an empty list
    if department not in employees_by_department:
        employees_by_department[department] = []

    # Append the current employee to the list for this department
    employees_by_department[department].append(employee)

# Print the resulting dictionary
print("Employees grouped by department:")
print(employees_by_department)

# Optional: print in a more readable format
print("\nDetailed view:")
for department, emp_list in employees_by_department.items():
    print(f"\nDepartment: {department}")
    for emp in emp_list:
        print(f"  - {emp['name']} ({emp['email']})")
