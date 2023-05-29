
from django.shortcuts import render
import numpy as np
import random

# Create your views here.
def home(request):
    
    arr_1d=np.array([1,3,7,9])
    print(arr_1d)
    a=type(arr_1d)
    print(a)
    b=arr_1d.dtype
    print(b)
    c=arr_1d.ndim
    print(c)
    d=arr_1d.size
    print(d)
    arr_2d=np.array([[1,2,3,4],[2,3,4,5]])
    print(arr_2d)
    arr_3d=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
    e=arr_2d.ndim
    f=arr_3d.ndim
    g=arr_2d.size
    h=arr_3d.size
    i=arr_2d.dtype
    j=arr_3d.dtype
    k=arr_2d.shape
    l=arr_3d.shape
    mx_1=np.ones(5)
    mx_11=np.ones(5,dtype=int)
    #2-D Array
    mx_2=np.ones((5,3))
    mx_22=np.ones((5,2),dtype=int)
    mx_3=np.zeros((5,1))
    mx_33=np.zeros((5,3),dtype=int)
    mx_4=np.empty((4,4))


    context={
        'arr_1d':arr_1d,
        'a':a,
        'b':b,'c':c,'d':d,'arr_2d':arr_2d,'arr_3d':arr_3d,'e':e,'f':f,'g':g,'h':h,'i':i,'j':j,'k':k,'l':l,'mx_1':mx_1,'mx_11':mx_11,'mx_2':mx_2,'mx_22':mx_22,'mx_3':mx_3,
        'mx_33':mx_33,'mx_4':mx_4,
    }
    
    return render(request,'home.html',context)
