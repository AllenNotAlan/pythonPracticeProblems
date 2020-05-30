
user_num = int(input("Enter a number to see if it's a prime:"))

def divisors(user_num):

    divisor_list = []

    for x in range(1,user_num):
        if user_num % x == 0:
            divisor_list.append(x)
            # print("{} is a divisor".format(x))
    return(divisor_list)

if divisors(user_num)[0] == 1 and len(divisors(user_num)) < 2:
    print("Prime number")
else:
    print(divisors(user_num))
    print("Not a prime")