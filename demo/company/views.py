from django.shortcuts import render,HttpResponse,redirect
from.models import register,fileupload
# Create your views here.
def registerpage(request):
    if request.method=='POST':
        getname=request.POST.get('name')
        getaddress=request.POST.get('address')
        getusername=request.POST.get('username')
        getpassword=request.POST.get('password')
        users=register()
        users.Name=getname
        users.Address=getaddress
        users.Username=getusername
        users.Password=getpassword
        users.save()
    return render(request,'registerpage.html')
#code for userlogin
def userlogin(request):
    if request.method == 'POST':
        getusername = request.POST.get('username')
        getpassword = request.POST.get('password')
        try:
            register.objects.get(Username=getusername,Password=getpassword)
            return HttpResponse('welcome user')
        except:
            return HttpResponse('invalid user')
    return render(request,'userlogin.html')
# code for adminlog
def adminlogin(request):
    if request.method == 'POST':
        getusername=request.POST.get('username')
        getpassword=request.POST.get('password')
        if getusername=='admin' and getpassword=='admin':
            return redirect('/adminhome')
        else:
            return HttpResponse('Invalid credentials')
    return render(request,'adminlogin.html')
#code for admin home
def adminhome(request):
    return render(request,'adminhome.html')

#code for pending
def pending(request):
    details=register.objects.filter(Status=False)
    return render(request,'pendinglist.html',{'value' :details})
#code for approve
def approve(request,id):
    data=register.objects.get(id=id)
    data.Status=True
    data.save()
    return redirect('/pending')
# code for approved
def approved(request):
    details=register.objects.filter(Status=True)
    return render(request,'approvelist.html',{'value':details})


def operations(request):
    details=register.objects.all()
    return render(request,'operations.html',{'value':details})

#code for operations
def edit(request,id):
    details=register.objects.all()
    user_data=register.objects.get(id=id)
    if request.method=='POST':
        getaddress=request.POST.get('address')
        getpassword=request.POST.get('password')
        user_data.Address=getaddress
        user_data.Password=getpassword
        user_data.save()
        return redirect('/operations')
    return render(request,'operations.html',{'value' :details,'data':user_data})



