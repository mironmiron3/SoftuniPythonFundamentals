command = input()
companies = {}
while not command == "End":
    command = command.split(" -> ")
    is_found = False
    if command[0] not in companies:
        companies[command[0]] = []
    for key, value in companies.items():
        for employee in value:
            if employee == command[1] and key == command[0]:
                is_found = True
    if not is_found:
        companies[command[0]].append(command[1])
    command = input()
sorted_companies = sorted(companies.items(), key=lambda kvp:kvp[0])
for company, employees in sorted_companies:
    print(company)
    employees_joined = '\n-- '.join(employees)
    print(f"-- {employees_joined}")


