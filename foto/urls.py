
from django.contrib import admin
from django.urls import path,include
from foto import views


urlpatterns = [
    path('papa/',admin.site.urls),
    path('',views.home,name="home"),
    path("upload/",views.upload,name="upload"),
    path("fetch/",views.fetch,name="fetch")          
]
