

# câu 2; 
# nhập đầu vào (n > 200); 

n = int(input()); 


#  xử lý: 
for x  in range(1, n):
    if (x % 2 == 0): 
        print(x, end=" ")
        #số chẵn thì in ra màn hình
        a = x / 15; 
        if (a % 2 == 0):
            print()

print(n); 