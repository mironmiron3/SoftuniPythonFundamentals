n = int(input())

for i in range (97 , 97 + n ):
    for m in range (97, 97 + n):
        for k in range (97, 97 + n):
            print(chr(i) + chr(m) + chr(k))