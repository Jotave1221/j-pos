users=fs["etc"]["users"]

print("welcome to j-pos!")
def login():
    while True:
        user=input("user:")
        passk=input("password:")
        if user in users:
            if passk==users[user][1]:
                os.system("clear")
                return users[user]
            else:
                print("wrong password!")
        else:
            print("user does not exist!")

user=login()

exec(fs["sbin"]["shell.prog"])