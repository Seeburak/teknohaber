from django.shortcuts import render,redirect
from appMy.models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def indexPage(request):
    haber_list=Haber.objects.all()
    category_list=Category.objects.all()
    haberust1_list=Haberust1.objects.all()
    haberust1_spor=Haberust1.objects.filter(Category=1)[1:]
    haberust1_sinema=Haberust1.objects.filter(Category=9)[1:]
    haberust1_oyun=Haberust1.objects.filter(Category=7)[1:]
    haberust1_mobil=Haberust1.objects.filter(Category=3)[1:]
    haberust1_yz=Haberust1.objects.filter(Category=8)
    haberust1_donanim=Haberust1.objects.filter(Category=5)
    haberust1_sag=Haberust1.objects.all()[:4]
    haberust1_slider=Haberust1.objects.all()[4:]
    haberust1_manset=Haberust1.objects.all()[4:16]
    kategoriler=Category.objects.all()
    
    if request.method == "POST":
      email = request.POST.get("email")
      
      contact = Bulten(email=email)
      contact.save() 

    
    context = {
        "haber_list":haber_list,
        "category_list":category_list,
        "haberust1_list":haberust1_list,
        "haberust1_spor":haberust1_spor,
        "haberust1_sinema":haberust1_sinema,
        "haberust1_oyun":haberust1_oyun,
        "haberust1_mobil":haberust1_mobil,
        "haberust1_yz":haberust1_yz,
        "haberust1_donanim":haberust1_donanim,
        "haberust1_sag":haberust1_sag,
        "haberust1_slider":haberust1_slider,
        "haberust1_manset":haberust1_manset,
        "kategoriler":kategoriler,
    }
    return render(request, "index.html", context)

def contactPage(request):
    if request.method == "POST":
      fname = request.POST.get("fullname")
      title = request.POST.get("title")
      email = request.POST.get("email")
      text = request.POST.get("text")
      
      contact = Contact(fullname=fname, title=title, email=email, text=text)
      contact.save() 
    context = {}
    return render(request, "contact.html", context)

def singlePage(request,hid):

    haberust1_list=Haberust1.objects.get(id=hid)
    
    comment_list=Comment.objects.filter(blog=haberust1_list)
    
    
    if request.method=="POST":
        fullname=request.POST.get("fullname")
        text=request.POST.get("comment")

        if fullname and text:
            comment=Comment.objects.create(fullname=fullname,text=text,blog=haberust1_list)
            comment.save()
        
    context = {

        "haberust1_list":haberust1_list,
        "comment_list":comment_list,          
    }
    return render(request, "single-page.html", context)

def hesapPage(request):
    context = {}
    return render(request, "hesap.html", context)
def loginPage(request):
    
    if request.method=="POST":
        
        username=request.POST.get("username")
        password=request.POST.get("password")
        rememberme=request.POST.get("rememberme")
        
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)

            if rememberme:
                request.session.set_expiry(604800)
         
            return redirect("profilePage")
        else:
            messages.error(request, "Kullancı adı veya şifre yanlış!")

    
    context = {}
    return render(request, "user/login.html", context)

def registerPage(request):
    
    fname=request.POST.get("fname")
    lname=request.POST.get("lname")
    username=request.POST.get("username")
    email=request.POST.get("email")
    password1=request.POST.get("password1")
    password2=request.POST.get("password2")
    
    site = request.POST.get("check-site")
    kvkk = request.POST.get("check-kvkk")
    
    if fname and lname and username and email and password1:
        if password1==password2:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    for k in password1:
                        if k.isnumeric(): num_bool=True
                        if k.isupper(): up_bool=True
                            
                    if len(password1)>8 and num_bool and up_bool:
                        user=User.objects.create_user(first_name=fname, last_name=lname, username=username, email=email, password=password1)
                        user.save()
                        return redirect("loginPage")
                    else:
                        messages.error(request, "Şifre oluşturma hatası.(en az 8 karakter, 1 büyük harf, 1 rakam)") 
                else:
                    messages.error(request, "E posta kayıtlı")     
            else:
                messages.error(request, "Kullanıcı adı mevcut")         
        else:
         messages.error(request, "şifreler aynı değil")                
    else:
        messages.error(request, "Boş kalan yerleri doldurunuz")  
    
    context = {}
    return render(request, "user/register.html", context)

def menuPage(request):
    kategoriler=Category.objects.all()
    context = {
        "kategoriler":kategoriler,
    }
    return render(request, "partials/_navbar.html", context)

def categoryPage(request,slug):
    haberust1_list=Haberust1.objects.filter(Category=slug)
    # category=Category.objects.get(baslik=slug)
    context = {
        # "category":category,
        "haberust1_list":haberust1_list,
    }
    return render(request, "category.html", context)

def uyelerPage(request):
    if request.method=="POST":
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")
        image=request.FILES.get("image")
        
        uyeler=Uyeler(first_name=fname, last_name=lname, username=username, email=email, password=password1,image=image)
        uyeler.save()
        return redirect("uyelerPage")
    context = {}
    return render(request, "/", context)