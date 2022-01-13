import winsound
def add(x,y,z=0):
    sum=0
    sum+=x+y+z
    return sum
try:
    ch=int(input("Please enter number of argument : "))
    if ch ==2:
        n1=int(input("Please enter first number: "))
        n2=int(input("Please second number: "))
        print(add(n1,n2))
    elif ch==3:
        n1 = int(input("Please enter first number: "))
        n2 = int(input("Please second number: "))
        n3 = int(input("Please second Third number: "))
        print(add(n1,n2,n3))
    else:
        print("Sorry, ",ch, " is not valid ")

except ValueError:
    print("value Error ")
    winsound.Beep(300, 150)



