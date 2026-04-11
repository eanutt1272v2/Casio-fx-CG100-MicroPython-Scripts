from matplotlib.pyplot import plot, axis, grid, text, show

while True:
    print("1=AP  2=GP  3=Recurrence  4=Series sums  0=quit")
    mode=input("> ")
    if mode=="0": break
    if mode=="1":
        a=float(input("First term a: ")); d=float(input("Common diff d: "))
        n=int(input("Number of terms n: "))
        terms=[a+d*i for i in range(n)]
        Sn=n/2*(2*a+(n-1)*d)
        print("a_n =",round(terms[-1],6))
        print("S_n =",round(Sn,6))
        print("Formula: a +",d,"(n-1)")
        xs=list(range(1,n+1))
        plot(xs,terms,"blue"); axis([0,n+1,min(terms)-1,max(terms)+1])
        text(1,terms[0],"AP a="+str(a)+" d="+str(d)); grid("on"); show()
    elif mode=="2":
        a=float(input("First term a: ")); r=float(input("Common ratio r: "))
        n=int(input("Number of terms n: "))
        terms=[a*r**i for i in range(n)]
        if abs(r)!=1:
            Sn=a*(1-r**n)/(1-r)
        else:
            Sn=a*n
        print("a_n =",round(terms[-1],8))
        print("S_n =",round(Sn,8))
        if abs(r)<1:
            print("S_inf =",round(a/(1-r),8))
        xs=list(range(1,n+1))
        plot(xs,terms,"red"); axis([0,n+1,min(terms)-abs(min(terms))*0.1,max(terms)*1.1])
        text(1,terms[0],"GP a="+str(a)+" r="+str(r)); grid("on"); show()
    elif mode=="3":
        print("Define u(n) in terms of u(n-1). e.g. Fibonacci")
        a0=float(input("u(0): ")); a1=float(input("u(1): "))
        n=int(input("Terms to compute: "))

        coeff1=float(input("coeff of u(n-1) (e.g.1 for Fib): "))
        coeff2=float(input("coeff of u(n-2) (e.g.1 for Fib): "))
        const=float(input("constant term (0 for Fib): "))
        terms=[a0,a1]
        for i in range(2,n):
            terms.append(coeff1*terms[-1]+coeff2*terms[-2]+const)
        print("Last 5:",terms[-5:])
        xs=list(range(n))
        plot(xs,terms,"green"); axis("auto"); grid("on")
        text(0,terms[0],"Recurrence"); show()
    elif mode=="4":
        print("Known series sums:")
        n=int(input("n: "))
        print("Sum 1..n =",n*(n+1)//2)
        print("Sum 1^2..n^2 =",n*(n+1)*(2*n+1)//6)
        print("Sum 1^3..n^3 =",(n*(n+1)//2)**2)
        print("Sum k*r^(k-1) geometric deriv:")
        r=float(input("r (for sum k*r^k): "))
        if abs(r)<1:
            print("Sum k*r^k (inf) =",r/(1-r)**2)
        s=sum(k*r**k for k in range(1,n+1))
        print("Sum k*r^k to n =",round(s,6))
    input("EXE")

input("\nPress any key to exit: ")

