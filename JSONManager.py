import json

with open('example.json') as file:
    data = json.load(file)
    print(data["cuentaUsuarios"])

    users = data["usuarios"]
    print(users)

    user1 = users[0]
    user2 = users[1]
    print(user1)
    print(user2)

    print(user1["nombre"])
    print(user1["status"])

    print(data["usuarios"][1]["nombre"])
    print(data["usuarios"][1]["status"])

    for user in users:
        print(str(user["nombre"]) + "," + str(user["status"]))


# prove that the file is closed
print(file.closed)
