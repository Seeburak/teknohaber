import os
from django.shortcuts import render,redirect
from appMy.models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User,auth
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
    aktifuye=Uyeler.objects.filter(islogin=True)
    
    if request.method == "POST":
      email = request.POST.get("email")
      
      contact = Bulten(email=email)
      contact.save() 

    
    context = {
        "aktifuye":aktifuye,
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
    kategoriler=Category.objects.all()
    aktifuye=Uyeler.objects.filter(islogin=True)
    if request.method == "POST":
      fname = request.POST.get("fullname")
      title = request.POST.get("title")
      email = request.POST.get("email")
      text = request.POST.get("text")
      
      contact = Contact(fullname=fname, title=title, email=email, text=text)
      contact.save() 
    context = {
        "kategoriler":kategoriler,
        "aktifuye":aktifuye,
    }
    return render(request, "contact.html", context)

def singlePage(request,hid):
    kategoriler=Category.objects.all()

    haberust1_list=Haberust1.objects.get(id=hid)
    aktifuye=Uyeler.objects.filter(islogin=True)
    comment_list=Comment.objects.filter(blog=haberust1_list)
    
    
    if request.method=="POST":
        fullname=request.POST.get("fullname")
        text=request.POST.get("comment")

        if fullname and text:
            comment=Comment.objects.create(fullname=fullname,text=text,blog=haberust1_list)
            comment.save()
        else:
            return redirect("loginPage")
        
    context = {

        "haberust1_list":haberust1_list,
        "comment_list":comment_list,
        "aktifuye":aktifuye,
        "kategoriler":kategoriler,          
    }
    return render(request, "single-page.html", context)

def hesapPage(request):
    kategoriler=Category.objects.all()
    aktifuye=Uyeler.objects.filter(islogin=True)
    uye=request.POST.get("uye")
    resimgetir=proimage.objects.filter(islogin=True)
    if request.method=="POST":
        submit = request.POST.get("submit")
        if submit == "ProfileLogout":

            Uyeler.objects.filter(islogin=True).update(islogin=False)
            proimage.objects.filter(islogin=True).update(islogin=False)
            return redirect("indexPage")
    context = {
        "aktifuye":aktifuye,
        "kategoriler":kategoriler,
        "resimgetir":resimgetir,
    }
    return render(request, "hesap.html", context)

def loginPage(request):
    kategoriler=Category.objects.all()
    aktifuye=Uyeler.objects.filter(islogin=True)


    if request.method=="POST":
        submit = request.POST.get("submit")
        username=request.POST.get("username")
        password=request.POST.get("password")
        rememberme=request.POST.get("rememberme")
        

        if not Uyeler.username==username:
            if not Uyeler.password==password:
                profile = Uyeler.objects.get(username=username, password=password)
                profile.islogin = True 
                profile.save()
                proimage.objects.filter(uyeler=username).update(islogin=True)
                messages.success(request,"Giriş Başarılı")
                return redirect("indexPage")
            else:
                messages.success( "Giriş hatalı!")
        else:
            messages.success("Giriş hatalı!")

        

    context = {
        "kategoriler":kategoriler,
        "aktifuye":aktifuye,
    }
    return render(request, "user/login.html", context)

def registerPage(request):
    kategoriler=Category.objects.all()
    
    if request.method=="POST":
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        username=request.POST.get("username")
        gizlisoru=request.POST.get("gizlisoru")
        email=request.POST.get("email")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")
        image=request.FILES.get("image")
        
        if password1 == password2:
            if not Uyeler.username==username:
            
                uyeler=Uyeler(first_name=fname, last_name=lname, username=username,gizlisoru=gizlisoru, email=email, password=password1,image=image)
                uyeler.save()
                resimler=proimage(uyeler=username, image=image, aktifresim=True, islogin=False)
                resimler.save()
                return redirect("indexPage")
            else:
                messages.error(request, "Kullanıcı adı daha önce alınmış")
        else:
               messages.error(request, "Yeni şifreler bir biriyle uyuşmuyor!")
    else:
        messages.error(request, "Boş kalan yerler var!")

    context = {
        "kategoriler":kategoriler,
    }
    return render(request, "user/register.html", context)

def menuPage(request):
    kategoriler=Category.objects.all()
    aktifuye=Uyeler.objects.filter(islogin=True)
    context = {
        "kategoriler":kategoriler,
        "aktifuye":aktifuye,
    }
    return render(request, "partials/_navbar.html", context)

def categoryPage(request,slug):
    kategoriler=Category.objects.all()
    haberust1_list=Haberust1.objects.filter(Category=slug)
    aktifuye=Uyeler.objects.filter(islogin=True)

    context = {

        "haberust1_list":haberust1_list,
        "kategoriler":kategoriler,
        "aktifuye":aktifuye
    }
    return render(request, "category.html", context)

def logoutUser(request):
   logout(request)
   return redirect("loginPage")


def hesapUpdate(request):
    kategoriler=Category.objects.all()
    aktifuye=Uyeler.objects.filter(islogin=True)
    uye=request.POST.get("uye")
    resimgetir=proimage.objects.filter(islogin=True)
    submit = request.POST.get("submit")
    if submit == "hesapGuncelle":
        if request.method=="POST":

            email=request.POST.get("email")
            password=request.POST.get("password1") 
            uyeler=Uyeler.objects.filter(islogin=True).update(email=email,password=password)
            return redirect("hesapUpdate")
    
    elif submit == "resimGuncelle":
        if request.method=="POST":
            image=request.FILES.get("image")
            uye=request.POST.get("kimbu")
            profile_list = proimage.objects.filter(uyeler=uye)
            profile_list.update(aktifresim=False,islogin=False)
            resimyukle=proimage(uyeler=uye,image=image,aktifresim=True,islogin=True)
            resimyukle.save()
            pasifresimler=proimage.objects.filter(aktifresim=False)
            pasifresimler.delete()
            return redirect("hesapUpdate") 
        
    elif submit == "ProfileLogout":
        Uyeler.objects.filter(islogin=True).update(islogin=False)
        proimage.objects.filter(islogin=True).update(islogin=False)
        return redirect("indexPage")    
        
    context = {
        "aktifuye":aktifuye,
        "kategoriler":kategoriler,
        "resimgetir":resimgetir,
    }
    return render(request, "guncelle.html", context)
    

def sifremiunuttum(request):
    kategoriler=Category.objects.all()
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        gizlisoru=request.POST.get("gizlisoru")

        
        profile = Uyeler.objects.get(username=username,email=email,gizlisoru=gizlisoru)
        profile.password="talep" 
        profile.save()
        return redirect("yenisifre")                     

    context = {
        "kategoriler":kategoriler,
    }
    return render(request, "sifremiunuttum.html", context)


def yenisifre(request):
    kategoriler=Category.objects.all()

    if request.method=="POST":
        password1=request.POST.get("password1")
        
        Uyeler.objects.filter(password="talep").update(password=password1)
        return redirect("indexPage")                

    context = {
        "kategoriler":kategoriler,
    }
    return render(request, "yenisifre.html", context)

def error_404(request):
   return render(request, "error/error404.html")
    

