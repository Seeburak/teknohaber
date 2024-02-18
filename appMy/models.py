from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
   baslik = models.CharField(("Başlık Deneme"), max_length=50)
   def __str__(self) -> str:
      return self.baslik

class Haber(models.Model):
   title = models.CharField(("Başlık"), max_length=150) # html input text
   text = models.TextField( verbose_name="İçerik" ) # html textarea
   date_now = models.DateTimeField(("Tarih - Saat"), auto_now=False, auto_now_add=False)
   author = models.CharField(("Yazar"), max_length=50)
   Category=models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True)

class Haberust1(models.Model):
   title = models.CharField(("Başlık"), max_length=150) # html input text
   text = models.TextField( verbose_name="İçerik" ) # html textarea
   date_now = models.DateTimeField(("Tarih - Saat"), auto_now=False, auto_now_add=False)
   author = models.CharField(("Yazar"), max_length=50)
   Category=models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True)
   image = models.ImageField(("Haber Resmi"), upload_to="haberresim", max_length=250)
   def __str__(self) -> str:
      return self.title
   
class Deneme(models.Model):
   baslik = models.CharField(("Başlık Deneme"), max_length=50)
   
class Contact(models.Model):
   fullname = models.CharField(("Ad Soyad"), max_length=50)
   title = models.CharField(("Konu"), max_length=50)
   email = models.EmailField(("Email"), max_length=254)
   text = models.TextField(("Mesaj"))
   def __str__(self) -> str:
      return self.fullname
   
class Bulten(models.Model):
   email = models.EmailField(("Email"), max_length=254)
   def __str__(self) -> str:
      return self.email
   
class Comment(models.Model):
   blog=models.ForeignKey(Haberust1,verbose_name=("Haberust1"),on_delete=models.CASCADE,null=True)
   fullname = models.CharField(("Ad Soyad"), max_length=50)
   text = models.TextField(("Yorum"))
   date_now=models.DateTimeField(("Tarih - Saat"),auto_now=False,auto_now_add=True)
   def __str__(self) -> str:
      return self.text
   
   
class Uyeler(models.Model):
   first_name = models.CharField(("Ad"), max_length=50)
   last_name = models.CharField(("Soyad"), max_length=50)
   username = models.CharField(("Username"), max_length=50)
   gizlisoru = models.CharField(("gizlisoru"), max_length=50,null=True,blank=True)
   email = models.CharField(("Email"), max_length=50)
   password = models.CharField(("Şifre"), max_length=50)
   image = models.ImageField(("Haber Resmi"), upload_to="profile/", max_length=250,null=True,blank=True)
   islogin = models.BooleanField(("Girişli Profil"), default=False)
   
   def __str__(self) -> str:
      return self.first_name
   
class proimage(models.Model):
   uyeler=models.CharField(("Üye id"), max_length=50,null=True,blank=True)
   image = models.ImageField(("Profil resmi"), upload_to="profile/")
   aktifresim=models.BooleanField(("aktif Resim"), default=False)
   islogin = models.BooleanField(("Girişli Profil"), default=False)


   
