# s="vedant"
# print(s[::-1])


#reverse string without using slicing
# def reverse_string(s):
#     return ''.join(reversed(s))
# print(reverse_string("hello"))


#checking number is prime or not
# a=int(input("enter any number"))
# if a<=1:
#     print("this is not prime number")
# else:
#     is_prime = True    
#     for i in range(2, a):
#         if a % i == 0:
#             is_prime = False
#             break

# if is_prime:
#     print("prime number")
# else:
#     print("is mot prime num ber")         





#Print the fibonaci series to Nth term


# n = int(input("enter any number"))


# a =0
# b=1
# if n <=0:
#     print("Enter the positive value")
# elif n==1:
#     print("fiboancci series")
#     print(a)
# else:
#       print("fiboancci series")
#       print(a,b, end ="")
#       for i in range(2, n):
#            c=a+b  
#       print(c, end ="")
#       a=b
#       b=c     


#check the given string or number is palindrome or not



# text=input("enter the number or string")


# reversed_text=''
# for char in text:
#     reversed_text=char + reversed_text

# if text==reversed_text:
#     print("the given item is palindrome")    
# else:
#     print("the given number is not palindrome")



#checkig the factorial


# num=int(input("enetr a number"))
# factorial=1

# if num<=1:
#     print("factorial cnt find out")

# elif num==0:
#     print("factorial is 1")
# else:
#     for i in range(1,num+1):
#         factorial *=1
#     print("factorial is:",factorial)     




# num = int(input("Enter a number: "))
# factorial = 1

# if num < 0:
#     print("Factorial does not exist for negative numbers")
# elif num == 0:
#     print("Factorial is 1")
# else:
#     for i in range(1, num + 1):
#         factorial *= i
    # print("Factorial is:", factorial)



# find the greatest common divisor
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# gcd = 1

# for i in range(1, min(a, b) + 1):
#     if a % i == 0 and b % i == 0:
#         gcd = i

# print("GCD is:", gcd)




# 
# text = input("enter the string")


# vowel="aeiouAEIOU"
# count = 0



# for char in text:
#     if char in vowel:
#         count +=1
# print("count of the vowels",count)        




#check the number wheather it is odd or even 


'''
a = int(input("enetr the number"))


if a % 2 == 0:
    print("The given number is even")
else:
    print("the number is odd")    
'''


'''
#swapping the two number without using the third

a = int(input("enter the first number  (a)",  ))
b = int(input("enter the first number  (b)",  ))


a,b=b,a


#after swapping
print("a",a)
print("b",b)
'''



