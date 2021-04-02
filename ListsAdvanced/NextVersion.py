existing_software = input().split(".")
new_software = []
if not int(existing_software[2]) == 9:
    existing_software[2] = str(int(existing_software[2])+1)
if int(existing_software[2]) == 9:
    existing_software[2] = str(0)
    if not int(existing_software[1]) == 9:
        existing_software[1] = str(int(existing_software[1]) + 1)
    if int(existing_software[1]) == 9:
        existing_software[1] = str(0)
        existing_software[0] = str(int(existing_software[0])+1)
print(".".join(existing_software))

example_tuple = ("exam", "purchase")
print(example_tuple)
if "purchase" in example_tuple:
    print("Yes it is ")
print(type(example_tuple))