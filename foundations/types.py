

#1
first_name = "Yehuda"
last_name = "Katz"
age = 23
city = "Petach Tikva"
email = "yeudakatz@gmail.com"

print(f"""
===== User Details =====
First Name: {first_name}
Last Name: {last_name}
Age: {age}
City: {city}
Email: {email}
========================
""")


#2
birth_year = 2002
current_year = 2026
print(f"you are approximately {current_year - birth_year} years old")


#3
width = 10
height = 20
print(f"the area is {width * height} and the perimeter is {(width + height) * 2}")


#4
name = "David"
age = 25
height = 1.78
is_student = True
salary = 8500

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))
print(salary, type(salary))



#5
first_name = "Yehuda"
last_name = "Katz"
age = 23
city = "Petach Tikva"
email = "yeudakatz@gmail.com"

print(f"""
===== User Details =====
First Name: {first_name}
Last Name: {last_name}
Age: {age}
City: {city}
Email: {email}
========================
""")



#6
n1 = int(input("enter a number: "))
n2 = int(input("enter more number "))
print(f"{n1} + {n2} = {n1 + n2}")
print(f"{n1} - {n2} = {n1 - n2}")
print(f"{n1} * {n2} = {n1 * n2}")
print(f"{n1} / {n2} = {n1 / n2}")



#7
product_name = input("enter product name: ")
price = int(input("enter a price of product: "))
quantity = int(input("enter a quantity of products: "))
print(f"""
====== Purchase Receipt ======
Product: {product_name}
Price: {price}
Quantity: {quantity}
Total: {price * quantity}
==============================
""")



#9
worker_name = input("enter worker name: ")
monthly_hours = int(input("enter num of hours you work in last month: "))
money_per_hour = int(input("enter the salary per 1 hour: "))
print(f"""====== Purchase Receipt ======
Worker: {worker_name}
Monthly_hours: {monthly_hours}
Salary per hour: {money_per_hour}
Total: {monthly_hours * money_per_hour}
==============================
""")



#10
price = int(input("Enter total price: "))
tip = int(input("Enter num of percent to tip: "))
people = int(input("Enter nu of people: "))
print(f"""
total tip: {price / tip}
total price {price + tip}
total per person
""")



#11
a = 10
b = 20

flag = a
a = b
b = flag



#12
first_name = input("enter first name: ")
last_name = input("enter last name: ")
age = int(input("enter a age: "))
school_name = input("enter a school name: ")
course_name = input("enter a school name: ")
month_learn = int(input("enter month learn: "))
price_per_month = int(input("enter price per month" ))
print(f"""
================================
       STUDENT REGISTRATION
================================

Student: {first_name} {last_name}
Age: {age}
Institution: {school_name}
Course: {course_name}
Duration: {month_learn} Months
Monthly Price: {price_per_month}

Total Course Price: {price_per_month} * {month_learn}

================================
Registration completed!
================================
""")