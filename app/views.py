from bs4 import MarkupResemblesLocatorWarning
from django.shortcuts import render
from . import phy

# Create your views here.
def index(request):
    return render(request,'index.html')

def expload(request,pk):
    context={}
    context['proc']=phy.getProc(pk)
    context['cols']=phy.getObsCols(pk)
    context['formcols']=phy.getFormCols(pk)
    context['obs']=None
    if request.GET.get('submit'):
        if pk==1:
            m=request.GET.get('m')
            s=request.GET.get('s')
            M=request.GET.get('M')
            c=request.GET.get('c')
            t=request.GET.get('t')
            context['obs']=phy.pr1obs(m,s,M,c,t)
        elif pk==2:
            m=request.GET.get('m')
            r=request.GET.get('r')
            h=request.GET.get('h')
            n=request.GET.get('n')
            N=request.GET.get('N')
            t=request.GET.get('t')
            context['obs']=phy.pr2obs(m,r,h,n,N,t)
        elif pk==3:
            w1=request.GET.get('w1')
            w2=request.GET.get('w2')
            z1=request.GET.get('z1')
            z2=request.GET.get('z2')
            context['obs']=phy.pr3obs(w1,w2,z1,z2)
        elif pk==4:
            w=request.GET.get('w')
            i=request.GET.get('i')
            I=request.GET.get('I')
            context['obs']=phy.pr4obs(w,i,I)
        elif pk==5:
            g=request.GET.get('g')
            u=request.GET.get('u')
            a=request.GET.get('a')
            h=request.GET.get('h')
            context['obs']=phy.pr5obs(g,u,a,h)
        elif pk==6:
            i=request.GET.get('i')
            d=request.GET.get('d')
            r=request.GET.get('r')
            context['obs']=phy.pr6obs(i,d,r)

    return render(request,'exp.html',context)