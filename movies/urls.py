from django.urls import path
from . import views

urlpatterns = [
    path("", views.login), 
    path("index.html", views.index), 
    path("hakkimizda.html", views.hakkimizda ),
    path("kişimail.html", views.kişimail ),
    path("kamerakayit.html", views.kamerakayit ),
    path("kayitweb.html", views.kayitweb ),
    path("smtp.html", views.smtp ),
    path("mail.html", views.mail ),
    path("login.html", views.login ),
    path("404.html", views.hata ),
    path("cikis.html", views.cikis ),
    path("forgot-password.html", views.sifreu ),
    path("forgot_password.html", views.forgot_password ),
    path("admin_login.html", views.admin_login ),
  
    
]

