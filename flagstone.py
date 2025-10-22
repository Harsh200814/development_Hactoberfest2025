n,m,a=map(int,input().split())
if a>=m and a>=n :
    print(1)
elif a>m and a<n :
    if n%a==0 :
        print(int(n/a))
    else:
        print((n//a+1))
elif a>n and a<m :
    if m%a==0 :
        print(int(m/a))
    else:
        print((m//a+1))
else:
    if m%a==0 and n%a==0 :
        print(int((m/a)*(n/a)))
    elif m//a==m/a and n//a!=n/a:
        print((m//a)*(n//a+1))
    elif m//a!=m/a and n//a==n/a:
        print((m//a+1)*(n//a))
    else:
        print((m//a+1)*(n//a+1))
