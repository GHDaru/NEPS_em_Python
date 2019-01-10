b = 1
for i in range(1,33):
    print("a =",(i-1)//2*2,"<-> b =",b)
    b += 1 if (b+1) % 3 != 0 else 2

