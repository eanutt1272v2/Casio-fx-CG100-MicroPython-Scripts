import math

def deg(r): return r*180/math.pi
def rad(d): return d*math.pi/180

def solve_triangle(a,b,c,A,B,C):

    known = sum(1 for x in [a,b,c] if x is not None)
    known_a = sum(1 for x in [A,B,C] if x is not None)

    if a is None and b and c and A:
        a = math.sqrt(b*b+c*c-2*b*c*math.cos(rad(A)))
    elif b is None and a and c and B:
        b = math.sqrt(a*a+c*c-2*a*c*math.cos(rad(B)))
    elif c is None and a and b and C:
        c = math.sqrt(a*a+b*b-2*a*b*math.cos(rad(C)))
    elif A is None and a and b and c:
        A = deg(math.acos((b*b+c*c-a*a)/(2*b*c)))
    elif B is None and a and b and c:
        B = deg(math.acos((a*a+c*c-b*b)/(2*a*c)))
    elif C is None and a and b and c:
        C = deg(math.acos((a*a+b*b-c*c)/(2*a*b)))

    if A and B and not C: C=180-A-B
    if A and C and not B: B=180-A-C
    if B and C and not A: A=180-B-C

    if a and A:
        k=a/math.sin(rad(A))
        if b is None and B: b=k*math.sin(rad(B))
        if c is None and C: c=k*math.sin(rad(C))
        if B is None and b: B=deg(math.asin(min(1,b/k)))
        if C is None and c: C=deg(math.asin(min(1,c/k)))
    return a,b,c,A,B,C

print("Enter known values (0 if unknown):")
print("Sides: a (opp A), b (opp B), c (opp C)")
a=float(input("a (0=unknown): ")) or None
b=float(input("b (0=unknown): ")) or None
c=float(input("c (0=unknown): ")) or None
A=float(input("A degrees (0=unknown): ")) or None
B=float(input("B degrees (0=unknown): ")) or None
C=float(input("C degrees (0=unknown): ")) or None

a,b,c,A,B,C = solve_triangle(a,b,c,A,B,C)
a,b,c,A,B,C = solve_triangle(a,b,c,A,B,C)

print("--- Solution ---")
print("a=",round(a,5) if a else "?")
print("b=",round(b,5) if b else "?")
print("c=",round(c,5) if c else "?")
print("A=",round(A,4),"deg" if A else "?")
print("B=",round(B,4),"deg" if B else "?")
print("C=",round(C,4),"deg" if C else "?")
if a and b and c:
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    R_circ=a*b*c/(4*area)
    r_in=area/s
    print("Area=",round(area,5))
    print("Circumradius R=",round(R_circ,5))
    print("Inradius r=",round(r_in,5))
    print("Perimeter=",round(a+b+c,5))

input("\nPress any key to exit: ")

