from casioplot import clear_screen, draw_string, set_pixel, show_screen
from math import sqrt, log, sin, exp, pi

_LC = (0.99999999999980993,676.5203681218851,-1259.1392167224028,
       771.32342877765313,-176.61502916214059,12.507343278686905,
       -0.13857109526572012,9.9843695780195716e-6,1.5056327351493116e-7)

def lgamma(x):
    if x < 0.5:
        return log(pi/sin(pi*x)) - lgamma(1.0-x)
    x -= 1.0
    a = _LC[0]
    t = x + 7.5
    for i in range(1,9): a += _LC[i]/(x+i)
    return 0.5*log(2*pi)+(x+0.5)*log(t)-t+log(a)

CMAPS = [
    ("cividis",
     [25.77607,-83.187239,102.370492,-58.977031,15.42921,-0.384689,-0.008973],
     [0.688122,-2.14075,2.600914,-1.404197,0.385562,0.639494,0.136756],
     [-28.262533,93.974216,-121.303164,74.863561,-22.36376,2.982654,0.29417]),
    ("inferno",
     [25.092619,-71.287667,77.157454,-41.709277,11.617115,0.105874,0.000214],
     [-12.222155,32.55388,-33.415679,17.457724,-3.947723,0.566364,0.001635],
     [-23.11565,73.588132,-82.253923,44.645117,-16.257323,4.117926,-0.03713]),
    ("magma",
     [18.664253,-50.758572,52.170684,-27.666969,8.345901,0.250486,-0.002067],
     [-11.490027,29.05388,-27.944584,14.253853,-3.596031,0.694455,-0.000688],
     [-5.570769,4.269936,12.881091,-13.646583,0.329057,2.495287,-0.009548]),
    ("mako",
     [-23.67438,57.794682,-48.335836,19.26673,-5.833466,1.620032,0.032987],
     [-2.172825,8.555513,-12.79364,8.153931,-1.651402,0.848348,0.013232],
     [14.259791,-47.319049,65.176477,-44.241782,12.702365,0.292971,0.040283]),
    ("plasma",
     [-3.623823,9.974645,-11.065106,6.094711,-2.653255,2.142438,0.064053],
     [-22.914405,71.408341,-82.644718,42.308428,-7.461101,0.244749,0.024812],
     [18.193381,-54.020563,60.093584,-28.491792,3.108382,0.742966,0.5349]),
    ("rocket",
     [-12.453563,44.789992,-57.268147,30.376433,-6.401815,1.947267,-0.003174],
     [52.250665,-158.313952,173.768416,-81.403784,15.073064,-0.476821,0.037717],
     [-10.648435,11.402042,14.869938,-21.550609,6.253872,0.400542,0.112123]),
    ("turbo",
     [-54.09554,220.424075,-334.841257,228.660253,-66.727306,7.00898,0.080545],
     [-21.578703,67.510842,-69.296265,25.101273,-4.927799,3.147611,0.069393],
     [110.735079,-305.386975,288.708703,-91.680678,-10.16298,7.655918,0.219622]),
    ("viridis",
     [-5.432077,4.751787,6.203736,-4.599932,-0.327241,0.107708,0.274455],
     [4.641571,-13.749439,14.153965,-5.758238,0.214814,1.39647,0.005768],
     [26.272108,-65.320968,56.6563,-19.291809,0.091977,1.386771,0.332664]),
]

def horner(c,t):
    v=c[0]
    for i in range(1,7): v=v*t+c[i]
    return v

def cmap(t,rc,gc,bc):
    if t<0.0: t=0.0
    elif t>1.0: t=1.0
    r=int(horner(rc,t)*255.0)
    g=int(horner(gc,t)*255.0)
    b=int(horner(bc,t)*255.0)
    if r<0: r=0
    elif r>255: r=255
    if g<0: g=0
    elif g>255: g=255
    if b<0: b=0
    elif b>255: b=255
    return (r,g,b)

n=int(input("n (1..k): "))
l=int(input("l (0..n-1): "))
m=int(input("|m| (0..l): "))
Z=float(input("Z (1=H): "))
R=float(input("R [a0] (0=auto): "))
exposure=float(input("exposure 0=auto +>bright: "))

print("CMAPS:")
for i in range(len(CMAPS)):
    print(str(i+1)+" "+CMAPS[i][0])
cm_idx=int(input("Select (1-"+str(len(CMAPS))+"): "))-1
if cm_idx<0 or cm_idx>=len(CMAPS): cm_idx=0
cm_name,RC,GC,BC=CMAPS[cm_idx]

if n<1: n=1
if l<0: l=0
if l>n-1: l=n-1
m=abs(m)
if m>l: m=l
if Z<=0.0: Z=1.0

if R<=0.0:
    r_exp=(3.0*n*n-l*(l+1))/(2.0*Z)
    if r_exp<=0.0: r_exp=3.0*n*n/Z
    R=1.5*r_exp
else:
    R=R

SCR_H=190
PY=10
SZ=SCR_H-PY
SAMP=SZ
LEG_X=SZ+4
LEG_W=10
LEG_LABEL_X=LEG_X+LEG_W+2
LEG_H=SZ

a0=1.0
EPS=1e-30
A0_M=5.29177210903e-11
A0_3=A0_M*A0_M*A0_M

p_rad=n-l-1
alpha_l=2*l+1
rho_k=2.0*Z/(n*a0)
log_norm_r=0.5*(3*log(rho_k)+lgamma(n-l)-log(2.0*n)-lgamma(n+l+1))
log_norm_y=0.5*(log((2*l+1)/(4*pi))+lgamma(l-m+1)-lgamma(l+m+1))
if m>0: log_norm_y+=0.5*log(2.0)
y_norm=exp(log_norm_y)

def al(ll,mm,x):
    pmm=1.0
    if mm>0:
        xx=1.0-x*x
        if xx<0.0: xx=0.0
        s=sqrt(xx); fact=1.0
        for i in range(1,mm+1):
            pmm*=-fact*s; fact+=2.0
    if ll==mm: return pmm
    pmmp1=x*(2*mm+1)*pmm
    if ll==mm+1: return pmmp1
    for lll in range(mm+2,ll+1):
        pll=(x*(2*lll-1)*pmmp1-(lll+mm-1)*pmm)/(lll-mm)
        pmm=pmmp1; pmmp1=pll
    return pmmp1

def lag(p,alp,x):
    if p<0: return 0.0
    L0=1.0
    if p==0: return L0
    L1=1.0+alp-x
    if p==1: return L1
    for k in range(1,p):
        L2=((2*k+1+alp-x)*L1-(k+alp)*L0)/(k+1)
        L0,L1=L1,L2
    return L1

def density(x_c,z_c):
    r2=x_c*x_c+z_c*z_c
    if r2<=1e-24:
        if l!=0: return 0.0
        rv=exp(log_norm_r)*lag(p_rad,alpha_l,0.0)
        yv=y_norm*al(l,m,1.0)
        d=rv*yv; return d*d
    r=sqrt(r2)
    rho=rho_k*r
    ea=-0.5*rho+(l*log(rho) if l>0 else 0.0)
    if ea<-700.0: return 0.0
    rv=exp(log_norm_r+ea)*lag(p_rad,alpha_l,rho)
    ct=z_c/r
    if ct<-1.0: ct=-1.0
    elif ct>1.0: ct=1.0
    yv=y_norm*al(l,m,ct)
    d=rv*yv; return d*d

step=2.0*R/(SAMP-1)
R_s=(SAMP+1)//2
peak=EPS
for sy in range(R_s):
    z_c=R-step*sy
    for sx in range(R_s):
        d=density(step*sx,z_c)
        if d>peak: peak=d

if exposure>=-0.99:
    gamma=1.0/(1.0+exposure)
else:
    gamma=100.0

def fmt_density(d):
    if d<=0.0: return "0"
    exp_n=0
    v=d
    while v>=10.0: v/=10.0; exp_n+=1
    while v<1.0: v*=10.0; exp_n-=1
    mantissa=int(round(v))
    if mantissa==10: mantissa=1; exp_n+=1
    return str(mantissa)+"e"+str(exp_n)

clear_screen()

Zs=str(int(Z)) if Z==int(Z) else str(Z)
hdr="Psi | n="+str(n)+" l="+str(l)+" m="+str(m)+" Z="+Zs+" cmap="+cm_name+" R="+str(R)+" [a0] exposure="+str(exposure)
draw_string(0,0,hdr,(0,0,160),"small")

sp=set_pixel
ss=show_screen

for sy in range(SAMP):
    z_c=R-step*sy
    py=PY+sy
    for sx in range(SAMP):
        x_c=-R+step*sx
        d=density(x_c,z_c)
        norm=d/peak
        if norm<0.0: norm=0.0
        elif norm>1.0: norm=1.0
        val=norm**gamma
        sp(sx,py,cmap(val,RC,GC,BC))
    ss()

for py in range(LEG_H):
    t=1.0-py/LEG_H
    col=cmap(t,RC,GC,BC)
    for dx in range(LEG_W):
        sp(LEG_X+dx,PY+py,col)

for i in range(5):
    t=i/4.0
    ty=PY+int((1.0-t)*(LEG_H-1))
    sp(LEG_X+LEG_W,   ty,(0,0,0))
    sp(LEG_X+LEG_W+1, ty,(0,0,0))
    if t<=0.0:
        d_tick=0.0
    else:
        d_tick=peak*(t**(1.0/gamma))/A0_3
    label=fmt_density(d_tick)+"m-3"
    ly=ty-4
    if ly<PY: ly=PY
    if ly>PY+LEG_H-8: ly=PY+LEG_H-8
    draw_string(LEG_LABEL_X,ly,label,(0,0,0),"small")

ss()

# input("\nPress any key to exit: ")