n = int(input())
result = 0
for letter in range (n):
    new_letter = input()
    result += ord(new_letter)

print(f'The sum equals: {result}')
