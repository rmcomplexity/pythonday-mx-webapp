from django.urls import path
from vanilla.apps.articulos import views

app_name = "articulos"

urlpatterns = [
    path('', views.ArticulosAPIView.as_view(), name="index")
]
