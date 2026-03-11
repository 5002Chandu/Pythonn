for n in range(1,2005):
    s=0
    t=n
    while t>0:
        r=t%10
        s+=r**3
        t//=10
    if s==n:
        print(n)