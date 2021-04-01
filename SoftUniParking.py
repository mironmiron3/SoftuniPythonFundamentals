n = int(input())
registrar = {}
for act in range(n):
    command = input().split()
    if command[0] == "register":
        if command[1] in registrar and registrar[command[1]] != command[2]:
            print(f"ERROR: already registered with plate number {registrar[command[1]]}")
        else:
            registrar[command[1]] = command[2]
            print(f"{command[1]} registered {registrar[command[1]]} successfully")
    elif command[0] == "unregister":
        if command[1] not in registrar:
            print(f"ERROR: user {command[1]} not found")
        else:
            registrar.pop(command[1])
            print(f"{command[1]} unregistered successfully")

for key, value in registrar.items():
    print(f"{key} => {value}")