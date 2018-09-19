n=int(input())
a=0
b=0
c=n-1
d=0
lst_1=[input().split() for i in range(n)]
print(lst_1)
i=0
for i in range(n):
   # print(a,b,c)
    for j in range(n):

        if(a==d and b<=c):
            print(lst_1[a][b],end=' ')
            b=b+1
            if(b==c+1):
                a=a+1
                b=b-1
        elif(a<=c and b==c):
            print(lst_1[a][b],end=' ')
            a=a+1
            if(a>c):
                a=a-1
                b=b-1
               # print(a,b)
        elif(a==c and b>=d):

            print(lst_1[a][b],end=' ')
            b=b-1

            if(b<d):
                a=a-1
                b=b+1
             #   print(a,b)


        elif(a>d and b==d):
            print(lst_1[a][b],end=' ')
            a=a-1
            if(a<=d):
                c=c-1
                d=d+1
                a=d
                b=d
