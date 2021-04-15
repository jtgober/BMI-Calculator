# 🚨 Don't change the code below 👇
height = input("enter your height in meters: ")
weight = input("enter your weight in kilos: ")
height_in_inches = input("enter your height in inches: ")
weight_in_pounds = input("enter your weight in pounds: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

height_num = float(height)
weight_num = float(weight)


height_num_inches = float(height_in_inches)
weight_num_pounds = float(weight_in_pounds)

print(weight_num / (height_num * height_num))
result_BMI =int(weight_num / (height_num * height_num))
print(result_BMI)

converted_height = height_num_inches / 39.37
converted_weight = weight_num_pounds / 2.2

result_converted_BMI =int(converted_weight / (converted_height * converted_height))
print(result_converted_BMI)