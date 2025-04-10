# nhập vào n; 
n = int(input())     # nhập n; 
while True:
    if n > 4:
        break
    n = int(input())

tich = 1
for x in range(1, n + 1):
    tich *= x

print(tich)
