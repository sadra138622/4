for i in range (993, 103, -10)
    m=0
    for j in range (2,i):
        if i%j==0:
            m=1
    if m!=1:
        print(i)
        break
