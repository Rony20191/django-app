
from django.urls import  path
from . import views

urlpatterns=[

    path('',views.index, name='index'),

    path('create/',views.store,name='store'),
    path('usuario/edit/<int:id>/', views.update, name='update'),
    path('usuario/delete/<int:id>/',views.deleteView,name='delete'),
    path('listar/',views.listar,name="listar"),
    path('login/',views.login,name="login")
]