from pages import views
from posts import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePageView.as_view(), name = 'home'),
    path('about/',views.index_about, name ='about'),
]
