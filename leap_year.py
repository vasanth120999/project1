a=int(input())
b=int(input())
c=int(input())
if a>=b and a>=c:
    if b>c:
        print(c)
    else:
        print(b)
if b>=a and b>=c:
    if a>c:
        print(c)
    else:
        print(a)
if c>=a and c>=b:
    if a>b:
        print(b)
    else:
        print(a)
            
