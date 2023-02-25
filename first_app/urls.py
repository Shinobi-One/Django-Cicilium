from django.urls import path
from . import views

app_name= "app"
urlpatterns = [
    path('blog',views.first_page,name='home'),
    path('blog/<slug:slug>',views.detail , name="detail")
]

