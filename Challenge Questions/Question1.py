from re import X


e=int(input())
r=int(input())
p1=int(input())
p2=int(input())
p3=int(input())
q=int(input())
x=((e-r)+2*q-(p1+p2+p3))//3
ans=((p1-q)+(p3-q)+q+x)
print(ans)
print(3*x)
