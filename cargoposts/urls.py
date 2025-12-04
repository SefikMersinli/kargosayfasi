from django.urls import path
from . import views

urlpatterns = [
    path('kargolar/', views.cargo_list, name="cargo_list"),
    path('kargolar/olustur/', views.cargo_create, name="cargo_create"),
    path('kargolar/<str:takip_no>/', views.cargo_info, name="cargo_info"),
]
