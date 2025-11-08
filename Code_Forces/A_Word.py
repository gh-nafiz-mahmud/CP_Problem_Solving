name = input()
upp = 0
low = 0

for i in name:
    if ord(i) >= 65 and ord(i) <= 90:
        upp += 1
    elif ord(i) >= 97 and ord(i) <= 122:
        low += 1
if upp > low:
    print(name.upper())
elif upp < low:
    print(name.lower())
else:
    print(name.lower())

