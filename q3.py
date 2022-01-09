
li = []
for i in range(1, 4):
    name = input(f"Please Enter {i} Person Name that U want to invite: ")
    li.append(name)
    li.sort()

print("People That U have been invited is: ")
for c in li:
    print(c)

while True:

    re = input("Press no to exit Or Any key to Invite Others: ")
    if re != "no":
        for i in range(4,100):
            name = input(f"Please Enter {i} Person Name that U want to invite Or no to exit: ")
            if name !="no":
                li.append(name)
                li.sort()
            else:
                print("All people that U have been invited= ",len(li))
                for c in li:
                    print(c)

                exit(-1)
    else:
        break

print("All people that U have been invited is= ",len(li))
for c in li:
    print(c)




