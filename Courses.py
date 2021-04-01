courses = {}
commands = input()
while not commands == "end":
    commands = commands.split(" : ")
    if commands[0] not in courses:
        courses[commands[0]] = []
        courses[commands[0]].append(commands[1])
    else:
        courses[commands[0]].append(commands[1])
    commands = input()
#a = sorted(courses.items(), key=lambda kvp: len(kvp))
sorted_courses = sorted(courses.items(),key=lambda kvp: len(kvp[1]),reverse=True)


for key, value in sorted_courses:
    print(f"{key}: {len(value)}")
    members1 = sorted(value)
    members = '\n-- '.join(members1)
    print(f"-- {members}")