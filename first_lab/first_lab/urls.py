from blog import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.BlogListView.as_view(), name = 'home'),
]
