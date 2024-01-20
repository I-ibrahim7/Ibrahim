# sum of two numbers
num1 = 5
num2 = 10
add = (num1+num2)
print("answer: ",(add))

# using append funtion
message = "hello "
message += "world!"  
print(message)

#using bool fuction

is_python_fun = False
if is_python_fun:
    print("python is fun")
else:
    print("python is hard if you dont take is serious!")    

# using list
Fruits = ['apple', 'banana', 'orange']
print("list of fruits: ",Fruits) 
new_fruit = 'mango'
Fruits.append(new_fruit)
print("new list of fruits is: ",Fruits)

#converting float into int
price = 14.01
print("price in a float form: ", price)
integer_price = int(price)
print("price in a integer form: ", integer_price)

#creating dictionary
student_info = {
    'name': 'Ibrahim',
    'age': '18',
    'grade': '12th'
}
print(student_info)

 #complex num variable
comp_num = 5+4j
print("real part of number is: ", comp_num.real)
print("imaginary part of number is: ", comp_num.imag) 

#Combine two strings using concatenation. Use string interpolation to include the length of the resulting string in a print statement
string1 = 'here we go '
string2 = 'again'
#combining both strings
combined_string = string1 + string2
print(f"The combined string is: {combined_string} and its leghth is {len(combined_string)}")

#Create a tuple named days_of_week with the names of the days. Access and print the third day of the week.

days_of_week = ("Monday ","Tuesday ","Wednesday ","Thursday ","Friday ","Saturday ","Sunday")
print(days_of_week[0])





