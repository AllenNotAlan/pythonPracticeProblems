#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
#(If you don’t know what a divisor is, it is a number that divides evenly into another number. 
#For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)


# x = 10
# y = 4
# divided = x / y

# print(divided % 2 != 0) 

user_num = int(input())

divisor_list = []

for x in range(1,user_num):
    if user_num % x == 0:
        divisor_list.append(x)
        # print("{} is a divisor".format(x))

print(divisor_list)