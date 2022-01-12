pe=input("Please enter how many people to invite: ")
if pe.isdigit():
    pe=int(pe)
    count=0
    if pe < 10:
        while pe < 10:
            name=input("Please enter name {}: ".format(count))
            count+=1
            if count == pe :
                break
    else:
        print("Too many people ")


else:
    print("Sorry, ",pe," is not valid ")