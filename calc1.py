my_friends = {}
active = True
while active:
    name = input("what is your name?\n:")
    age = input("how old are you?\n:")
    home = input("where is you home?\n:")

    while True:
        my_friends[name.title()] = {"age": int(age),
                              "home": home.title()
                              }
        break

    repeat = input("Do you whant to repeat?")
    if repeat == "no":
        active = False
for friend in my_friends.items():
    print(friend)