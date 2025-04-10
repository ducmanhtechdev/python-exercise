#  nhập n; 

n  = int(input("nhập n="));
while True: 
     if (n > 2): 
        break; 
    n  = int(input("nhập n="));
    
dem = 0; 
for x in range(1,n + 1): 
    if (n % x == 0):
        dem+=1;
if (dem == 2):
    print(str(n) + " là số nguyên tố"); 