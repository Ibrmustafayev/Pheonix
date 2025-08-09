n=int(input())
x,y=[],[]
i=a=b=0
for i in range(n):
    x_,y_=map(int,input().split())
    x.append(x_)
    y.append(y_)
for i in range(0,n):
    if i+1==n:
        a+=x[i]*y[0]
        b+=y[i]*x[0]
    else:
        a+=x[i]*y[i+1]
        b+=y[i]*x[i+1]
S=abs(1/2*(a-b))
print(round(S,3))