from django.urls import path
from . import views

urlpatterns=[
    path('form/basic/',views.form_basic),
    path('ship/',views.Ship_List),
    path("",views.main),
    path("select/", views.select),
    path("insert/", views.insert),
    path("update/", views.update),
    path("delete/", views.delete),
]