import sys
contests = {}
data = input()
while not data == "end of contests":
    data = data.split(":")
    contests[data[0]] = data[1]
    data = input()
users = {}
info = input()
while not info == "end of submissions":
    contest, password, username, points = info.split("=>")
    points = int(points)
    if contest in contests and password in contests.values():
        if username not in users:
            users[username] = {}
        if contest not in users[username]:
            users[username][contest] = points
        else:
            if points > users[username][contest]:
                users[username][contest] = points
    info = input()
max_points = -sys.maxsize
max_points_user = ''
for name in users:
    points = 0
    for course in users[name]:
        points += users[name][course]
    if points > max_points:
        max_points = points
        max_points_user = name
print(f"Best candidate is {max_points_user} with total {max_points} points.")



sorted_students = sorted(users.items(), key= lambda kvp: (kvp[0],kvp[1]))
print("Ranking:")

for name, dict in sorted_students:
    sorted_results = sorted(dict.items(), key=lambda kvp: kvp[1], reverse=True)
    print(f"{name}")
    for tuple in sorted_results:
        print(f"#  {tuple[0]} -> {tuple[1]}")






