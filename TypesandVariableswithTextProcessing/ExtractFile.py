data = input()
extension = ''
name = ""
index_separating = None
for index in range(len(data), -1, -1):
    if data[index].isalnum():
        extension += data[index]
    if data[index] == ".":
        index_separating = index
        break
for index in range(index_separating, -1, -1):
    if data[index].isalnum():
        name += data[index]
    else:
        break

print(f"File name: {name[::-1]}")
print(f"File extension: {extension[::-1]}")


