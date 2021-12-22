import requests
from bs4 import BeautifulSoup
import lxml
import math

g=9.8
h=6.626*(10**(-34))
c=299792458

pracs = [
    (74,207),
    (74,571),
    (189,342),
    (195,840),
    (74,191),
    (189,343)
]

tableCols={
    1:['mass(m)','distance(s)','mass(M)','coeffecient','time','force','total mass','measured a','calculated a'],
    2:['mass suspended(kg)','radius(m)','height(m)','n','N','time','Mean avg Velocity','Moment of inertia'],
    3:['w1','w2','z1','z2','Divergence Angle'],
    4:['wavelength','current','intensity','K (energy)'],
    5:['Velocity(u)','Angle of projection','Canon Height(m)','Time of flight','Range','Max height'],
    6:['Imax','Detector distance (m)','radius(m)','numerical aperture','angle']
}

formcols={
    1:['m','s','M','c','t'],
    2:['m','r','h','n','N','t'],
    3:['w1','w2','z1','z2'],
    4:['w','i','I'],
    5:['g','u','a','h'],
    6:['i','d(mm)','r(mm)']
}

global obs1,obs2,obs3,obs4,obs5,obs6
obs1=[]
obs2=[]
obs3=[]
obs4=[]
obs5=[]
obs6=[]

def pr1obs(m,s,M,c,t):

    m=float(m)
    s=float(s)
    M=float(M)
    c=float(c)
    t=float(t)
    total=m+M
    f=(m*g)-(c*M*g)
    a=f/total
    a2=2*s/(t**2)
    obs1.append([m,s,M,c,t,f,total,a,a2])
    return obs1

def pr2obs(m,r,h,n,N,t):
    m=float(m)/1000
    r=float(r)/100
    h=float(h)/100
    n=float(n)
    N=float(N)
    t=float(t)
    w=4*math.pi*N/t
    print('w',w)
    i=(((n*m)/(n+N))*(((2*g*h)/(w**2))-(r**2)))
    print('i',i)
    obs2.append([m,r,h,n,N,t,w,i])
    return obs2

def pr3obs(w1,w2,z1,z2):
    #w=float(w)
    w1=float(w1)
    w2=float(w2)
    z1=float(z1)
    z2=float(z2)
    b=(w2-w1)/(z2-z1)
    #w0=w/(3.14*b*1000)
    obs3.append([w1,w2,z1,z2,b])
    return obs3

def pr4obs(w,i,I):
    w=float(w)
    k=h*c/w
    obs4.append([w,i,I,k])
    return obs4

def pr5obs(g,u,a,h):
    u=float(u)
    a=float(a)
    a=math.pi/(180/a)
    h=float(h)
    g=float(g)
    t=2*u*math.sin(a)/g
    r=u*u*math.sin(2*a)/g
    H=((u*u)*(math.sin(a))**2)/(2*g)
    obs5.append([u,a,h,t,r,H])
    return(obs5)

def pr6obs(i,d,r):
    i=float(i)
    d=float(d)/1000
    r=float(r)/1000
    n=r/(math.sqrt((r**2)+(d**2)))
    a=math.asin(n)
    obs6.append([i,d,r,n,a])
    return(obs6)

def getProc(id):
    source = requests.get('https://vlab.amrita.edu/?sub=1&brch='+str(pracs[id-1][0])+'&sim='+str(pracs[id-1][1])+'&cnt=2').text
    soup = BeautifulSoup(source, 'lxml')

    article = soup.find('div', class_='divContent')
    return article

def getObsCols(id):
    return tableCols[id]

def getFormCols(id):
    return formcols[id]
    
