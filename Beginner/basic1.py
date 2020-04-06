# odd or even

#ask user for a number, then script tells them if it's odd or even
print("Enter a number: ")
user_num = int(input())

if user_num > 0:
    if user_num % 2 == 0:
        print("{} is even".format(user_num))
    else:
        print("{} is odd".format(user_num))
else:
    print("invalid number. ")