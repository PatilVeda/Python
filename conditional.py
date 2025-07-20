#"day_of_week = input("enter a days of week:   MO").upper()
#print(day_of_week)


#if day_of_week =="saturday" or day_of_week =="sunday":
 #   print("i will live devops")
#else:
 #   print("i will practice devops")


num1=int(input("enter a first number: "))
num2=int(input("enter a second number: "))

choice = input("enter the operation:  (options +,-,*,/,%)")   



if choice=="+":
    sum_of_num = num1 + num2

    print("addition",sum_of_num)
elif choice=="-":
    diff_of_num =num1 -num2
    print("substraction",diff_of_num)

elif choice=="*":
    multi_of_num =num1 *num2

    print("multiplication",multi_of_num)
elif choice=="/":
    divisio_of_num =num1 /num2

    print("division",divisio_of_num)    
else:
    print("invalid choice")