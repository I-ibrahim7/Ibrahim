# gettinh user input for age
user_age = input("enter your age here: ")

#changing user input to integer
age = int(user_age)

#printing message for different age groups

if age < 13:
    print("you are a child.")
elif age < 20:
    print("you are teenager.")
elif age < 60:
    print("you are adult.")
else:
    print("you are senior citizen.")
                





