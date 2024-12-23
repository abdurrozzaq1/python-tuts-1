# # # Given a side of square. Find its perimeter and area.
# # # solution
# # first_side = int(input('enter the first side: '))
# # second_side = int(input('enter the second side: '))
# # area = first_side+second_side
# # perimeter = 4*area
# # print(perimeter)


# # # Given diameter of circle. Find its length.
# # # solution
# # circle_diameter = int(input('enter the diameter of the circle: '))
# # circle_length = circle_diameter * 3.14
# # print(circle_length)


# # # Given two numbers a and b. Find their mean.
# # # solution
# # a = int(input('enter the first number: '))
# # b = int(input('enter the second number: '))
# # result = (a+b)/2
# # print(result)


# # # Given two numbers a and b. Find their sum, product and square of each number.
# # # solution
# # a = int(input('enter the first number: '))
# # b = int(input('enter the second number: '))
# # sum_num = a+b
# # a_square = a**2
# # b_square = b**2
# # print(sum_num, a_square, b_square)


# # num=[1,2,3,4]
# # new_num = num.copy()
# # new_num.append(12)
# # num.clear()
# # print(num, new_num)


# # months= ["January", "February", "March", "April", "May"]
# # new_month= months.pop(-1)
# # print(new_month, months)

# # random_num = [1,12,99, 43,100]
# # random_num.append(55)
# # random_num[1]=63
# # del random_num[-1]

# # numbers= [15, 2, 78, 34, 7, 90]
# # max(numbers)


# # numbers = [10, 20, 30, 40, 50]
# # sum_num=sum(numbers)
# # len_num =len(numbers)
# # avg_num = sum_num/len_num


# # fruits = ["banana", "apple", "cherry", "date"]
# # sorted(fruits)
# # sorted(fruits,reverse=True)



# # new_dict={
# #     'name':'Abdurrozzaq',
# #     'last_name':'Abdukhakimov',
# #     'age':20
# # }

# # new_dict['is_married']=False
# # another_dict = new_dict.pop('age','not found')
# # print(new_dict)
# # print(another_dict)





# # task 1
# num = int(input('enter a number: '))
# if num % 3 == 0 and num % 5 == 0:
#     print('the number is divisible')
# else:
#     print('try again')
    
# # task2
# fstr = input('enter a word: ')
# sstr = input('enter a word: ')

# if fstr == sstr:
#     print('they are equal')
# else:
#     print('they are not equal')
    
# # task3
# fnum = int(input('enter the first number: '))
# snum = int(input('enter the second number: '))

# if fnum>snum:
#     print('fnum is greater than snum')
# elif fnum == snum:
#     print('they are equal')
# else:
#     print('fnum is less than snum')
     
# # task4
# num = int(input('enter a number: '))
# if num > 0 : print('the number is positive') 
# else: print('the number is negative')

# # task5
# age = int(input('enter an age: '))
# if age >= 60:
#     print('this is a senior citizen')
# else:
#     print('this is a junior citizen')
    
# # task6
# num = int(input('enter a number: '))
# if num > 0 and num < 30:
#     print('the weather is warm')
# elif num >=30:
#     print('the weather is hot')
# elif num <0:
#     print('the weather is cold')
    
# # task7
# age = int(input('enter an age: '))
# dr_lisence = input("do you have a driving lisence, answer 'yes' or 'no':  ")

# if age >= 18 and dr_lisence=='yes':
#     print('You are eligible to drive a car')
# else:
#     print('You are too young to drive a car')
    
# # task8













# # list comprohension
# new_list=[]
# new_list=[i*2 for i in range(1,21) if i % 2 == 0]

# new_list2 = []
# new_list2=[i for i in range(1,16) if i%3==0]

# # dict comprohension
# import string
# letters = ['a', 'e', 'i', 'o', 'u']
# new_list3=[]
# new_list3=[(letter, string.ascii_letters.index(letter)) for letter in letters]
  
            
# list_4=[]
# list_4=[(num, num**3) for num in range(1, 11)]


# sents='This is a set comprehension example in Python'
# print(sents.split())

import math
def findS(a,b,c):
    s = (a+b+c) / 2
    result = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return result
print(findS(a=3,b=4,c=5))

def findP(a,b,c):
    return a+b+c
print(findP(a=3,b=4,c=5))

