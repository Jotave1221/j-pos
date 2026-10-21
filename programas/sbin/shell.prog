curdir=fs
while True:
    command=input(f"{user[0]}@j-pos {curdir} $ ")
    if f"{command}.prog" in fs["bin"]:
        if fs["bin"][f"{command}.prog"][1] <= user[1]:
            exec(fs["bin"][f"{command}.prog"][0])
        else:
            if command.split()[1]=="sudo" and user[2]==1:
                while True:
                    ptry=input("(sudo) root password:")
                    if ptry==users["root"][1]:
                        puser=user
                        user=users["root"]
                        exec(fs["bin"][f"{command}.prog"][0])
                        user=puser
                        break
                    else:
                        print("(sudo) incorrect password! try again.")
            else:
                print("you forgot sudo or tryed to use it whit no permission")
    else:
        print("program does not exist!")

