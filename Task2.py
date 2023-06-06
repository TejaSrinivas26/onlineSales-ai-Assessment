import csv

# Read Departments data from CSV
with open('departments.csv', 'r') as file:
    departments_data = list(csv.DictReader(file))

# Read Employees data from CSV
with open('employees.csv', 'r') as file:
    employees_data = list(csv.DictReader(file))

# Read Salaries data from CSV
with open('salaries.csv', 'r') as file:
    salaries_data = list(csv.DictReader(file))

# Create a dictionary to store department-wise salaries
department_salaries = {}

# Calculate average monthly salary for each department
for department in departments_data:
    department_name = department['NAME']
    department_id = department['ID']
    department_salaries[department_name] = []
    
    # Get employees in the current department
    department_employees = [employee for employee in employees_data if employee['DEPT ID'] == department_id]
    
    # Get salaries of employees in the current department
    department_salary_amounts = [int(salary['AMT (USD)']) for salary in salaries_data if salary['EMP_ID'] in [employee['ID'] for employee in department_employees]]
    
    # Calculate average monthly salary for the department
    avg_salary = sum(department_salary_amounts) / len(department_salary_amounts)
    
    department_salaries[department_name] = avg_salary

# Sort departments by average monthly salary in descending order
sorted_departments = sorted(department_salaries.items(), key=lambda x: x[1], reverse=True)

# Get top 3 departments with highest average monthly salary
top_3_departments = sorted_departments[:3]

# Generate the report
print("Top 3 Departments by Average Monthly Salary:")
print("-------------------------------------------")
print("DEPT_NAME\t\tAVG_MONTHLY_SALARY")
print("-------------------------------------------")
for department, avg_salary in top_3_departments:
    print(f"{department}\t\t{avg_salary:.2f}")
