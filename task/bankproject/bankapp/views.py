from django.contrib import auth,messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
from bankapp.models import branch, userdetail,place


def home(request):
    br = branch.objects.all()
    return render(request,"home.html",{'branch':br})


def log(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('bankapp:apply')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('bankapp:log')
    return render(request, "login.html")

def regis(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpass = request.POST['cpass']
        if password == cpass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists")
                return redirect('bankapp:regis')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                messages.info(request,"Registeration successfull")
                return redirect('bankapp:log')

        else:
            messages.info(request, "Password and confirm password should be same.")
            return redirect('bankapp:regis')
    return render(request,"registeration.html")

def apply(request):
    return render(request,"apply.html")

def detail(request):
    br = branch.objects.all()
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        age = request.POST['age']
        gender = request.POST['gender']
        email = request.POST['email']
        address = request.POST['address']
        bankbranch = request.POST['bankbranch']
        Type = request.POST['Type']

        res = userdetail.objects.create(firstname=firstname,lastname = lastname, age = age , gender=gender,email=email, address= address,
)
        res.save()
        messages.info(request, "Your bank application successfully registered dude")
        return redirect('bankapp:detail')
    return render(request, "appform.html",{'branch':br})

def lout(request):
    auth.logout(request)
    return redirect('bankapp:home')

def load_branches(request):
    place_id=request.GET.get('bankbranch')
    pla=place.objects.filter(branch_id=place_id).all()
    return render(request, "dropdown_list.html",{'place':pla})
