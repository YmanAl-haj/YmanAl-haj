while True:
    name=input("Please Write your Name Or press q to exit: ")
    if name !="q":
        print(name.capitalize())
        print("Length of your name = ",len(name))
    else:
        break