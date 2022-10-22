from django.urls import path
from . import views
# app_name = "subApp"
urlpatterns = [
    path('home/',views.firstView),
    # path('welcome/',views.welcome,name="index1")

    path('<str:name>',views.welcome,name="index")
]