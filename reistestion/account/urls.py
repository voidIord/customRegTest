from django.urls import path
from . import views

urlpatterns = [
    path('', views.interface, name='interface'),
    path('group', views.group, name='group'),
    path('<int:pk>', views.dinamic.as_view(), name='group-detail'),
    path('<int:pk>/update', views.update.as_view(), name='group-update'),
    path('<int:pk>/delete', views.delete.as_view(), name='group-delete'),

    path('register/', views.registration_view, name='register'),
    path('image/', views.image_view, name='image'),
    path('login/', views.login_view, name='login'),
    path('accounts/login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('account/', views.account_view, name='account'),
    path('table/', views.table_view, name='TableForSemester')
]
