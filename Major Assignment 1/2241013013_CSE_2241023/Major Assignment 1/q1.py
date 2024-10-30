

def basic_salary(hourly_rate, hours_per_week):
    
    if hours_per_week > 40:
        overtime = overtime_salary(hourly_rate, hours_per_week)
    else:
        overtime = 0
    basic = hourly_rate * hours_per_week * 4
    return basic, overtime

def overtime_salary(hourly_rate, hours_per_week):
    
    extra_hours = hours_per_week - 40
    overtime = extra_hours * (hourly_rate * 1.5) * 4  
    return overtime

def total_salary(hourly_rate, hours_per_week):
    
    basic, overtime = basic_salary(hourly_rate, hours_per_week)
    return basic + overtime




def tax_amount(salary):
   
    if salary < 60000:
        tax = salary * 0.10
    elif 60000 <= salary <= 85000:
        tax = salary * 0.15
    else:
        tax = salary * 0.20
    return tax




def gross_salary(basic):
    
    allowances = basic * 0.20  
    gross = basic + allowances
    tax = tax_amount(basic)
    return gross - tax




def salary_bracket(gross_salary):
    
    if gross_salary < 50000:
        return "Low income"
    elif 50000 <= gross_salary <= 80000:
        return "Middle income"
    else:
        return "High income"




def employee_report(employees):
    
    for employee in employees:
        name, hourly_rate, hours_per_week = employee
        basic, overtime = basic_salary(hourly_rate, hours_per_week)
        total = total_salary(hourly_rate, hours_per_week)
        tax = tax_amount(basic)
        gross = gross_salary(basic)
        bracket = salary_bracket(gross)
        
        
        print(f"Employee Name: {name}")
        print(f"Hourly Rate: Rs. {hourly_rate}")
        print(f"Hours Worked per Week: {hours_per_week}")
        print(f"Basic Salary (per month): Rs. {basic}")
        print(f"Overtime Salary (per month): Rs. {overtime}")
        print(f"Total Salary (per month): Rs. {total}")
        print(f"Tax Amount: Rs. {tax}")
        print(f"Gross Salary: Rs. {gross}")
        print(f"Salary Bracket: {bracket}")
        print("-" * 40)





employees = []
no_of_employee = int(input("Enter how many employees you want : "))
for i in range(no_of_employee):
    print(f"Enter details for Employee {i + 1}:")
    name = input("Enter name: ")
    hourly_rate = float(input("Enter hourly rate (in Rs): "))
    hours_per_week = float(input("Enter hours worked per week: "))
    employees.append((name, hourly_rate, hours_per_week))
    print() 




employee_report(employees)
