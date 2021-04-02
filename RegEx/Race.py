import re
names = input().split(", ")
contestants_scores = {}
for name in names:
    contestants_scores[name] = 0
pattern = r"[a-zA-Z]"
pattern2 = r"\d"
text = input()
while not text == "end of race":
    match = re.findall(pattern, text)
    match2 = re.findall(pattern2, text)
    match2 = list(map(lambda x: int(x), match2))
    for name in names:
        if "".join(match) == name:
            contestants_scores[name] += sum(match2)
    text = input()
sorted_contestants = sorted(contestants_scores.items(),key=lambda kvp: -kvp[1])
print(f"1st place: {sorted_contestants[0][0]}")
print(f"2nd place: {sorted_contestants[1][0]}")
print(f"3rd place: {sorted_contestants[2][0]}")



