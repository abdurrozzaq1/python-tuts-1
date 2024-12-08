# Given a side of square. Find its perimeter and area.
# solution
first_side = int(input('enter the first side: '))
second_side = int(input('enter the second side: '))
area = first_side+second_side
perimeter = 4*area
print(perimeter)


# Given diameter of circle. Find its length.
# solution
circle_diameter = int(input('enter the diameter of the circle: '))
circle_length = circle_diameter* 3.14
print(circle_length)


# Given two numbers a and b. Find their mean.
# solution
a = int(input('enter the first number: '))
b = int(input('enter the second number: '))
result = (a+b)/2
print(result)


# Given two numbers a and b. Find their sum, product and square of each number.
# solution
a = int(input('enter the first number: '))
b = int(input('enter the second number: '))
sum_num = a+b
a_square = a**2
b_square = b**2
print(sum_num, a_square, b_square)

