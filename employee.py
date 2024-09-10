# employee data
employees = [
    {"name": "Ajay Singh", "designation": "Manager", "salary": 12000, "age": 35, "department": "Sales", "experience": 10, "city": "Mumbai", "email": "singhajay@gmail.com"},
    {"name": "Ram Kumar", "designation": "Developer", "salary": 9000, "age": 28, "department": "IT", "experience": 4, "city": "Delhi", "email": "ram@gmail.com"},
    {"name": "Aman Verma", "designation": "HR", "salary": 8000, "age": 40, "department": "HR", "experience": 12, "city": "Noida", "email": "aman@gmail.com"},
    {"name": "Shreya Verma", "designation": "Designer", "salary": 15000, "age": 25, "department": "Design", "experience": 3, "city": "Noida", "email": "shreya@gmail.com"},
    {"name": "Karan Kapoor", "designation": "Analyst", "salary": 9500, "age": 30, "department": "Finance", "experience": 6, "city": "Gurugram", "email": "karan@gmail.com"}
]

# Function to filter employees based on given condition

def filter_employees(col, condition, value, order="asc"):

    # Handling numeric values (Ex:- salary, age, experience,etc)
    if col in ["salary", "age", "experience"]:
        if condition == "greater":
            filtered = [emp for emp in employees if emp[col] > value]
        elif condition == "less":
            filtered = [emp for emp in employees if emp[col] < value]
        else:
            print("Invalid condition. Use 'greater' or 'less'.")
            return []
    
    # Handling string cvalues (Ex:- name, designation, city, etc.)
    elif col in ["name", "designation", "city", "email", "department"]:
        if condition == "sort":
            if order == "asc":
                filtered = sorted(employees, key=lambda emp: emp[col])
            elif order == "desc":
                filtered = sorted(employees, key=lambda emp: emp[col], reverse=True)
            else:
                print("Invalid order. Use 'asc' or 'desc'.")
                return []
        else:
            filtered = [emp for emp in employees if value.lower() in emp[col].lower()]
    
    # If column is not valid
    else:
        print("Invalid column specified.")
        return []
    
    # Returning the filtered result
    return filtered

