users = fs["etc"]["users"]

print("welcome to j-pos!")
def login():
    while True:
        user = input("user:")
        passk = input("password:")
        for u in users.values():
            if u[0] == user:
                if passk == u[1]:
                    os.system("clear")
                    return u
                print("wrong password!")
                break
        else:
            print("user does not exist!")

user = login()

exec(fs["sbin"]["shell.py"])