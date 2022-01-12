
total=0
while total <=50:
    num=input("Please Enter number: ")
    if num.isdigit():
        num = int(num)
        total+=num
        print("The Total is: {} ".format(total))
    else:
        print("Sorry, ", num, " is not valid ")