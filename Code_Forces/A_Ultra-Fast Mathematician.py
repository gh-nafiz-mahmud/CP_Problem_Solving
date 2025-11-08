a_str = input().strip()
b_str = input().strip()

a = int(a_str, 2)
b = int(b_str, 2)

ans = a ^ b
print(bin(ans)[2:].zfill(len(a_str)))
