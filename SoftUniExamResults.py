data = input()
contestants = {}
submissions = {}
while not data == "exam finished":
    data = data.split("-")
    if data[1] not in submissions and data[1] != "banned":
        submissions[data[1]] = 0
    if data[1] != "banned":
        submissions[data[1]] += 1
    if data[0] not in contestants:
        contestants[data[0]] = {}
        contestants[data[0]]["score"] = int(data[2])
    if data[1] == "banned":
        contestants.pop(data[0])
        data = input()
        continue
    if contestants[data[0]]["score"] < int(data[2]):
        contestants[data[0]]["score"] = int(data[2])


    contestants[data[0]]["language"] = data[1]
    data = input()

sorted_contestants = sorted(contestants.items(),key=lambda kvp:(-kvp[1]["score"],kvp[0]))
sorted_submissions = sorted(submissions.items(),key=lambda kvp:kvp[1],reverse=True)
print("Results:")
for key, value in sorted_contestants:
    print(f"{key} | {value['score']}")
print("Submissions:")
for key, value in sorted_submissions:
    print(f"{key} - {value}")




