from django.urls import path 
from . import views 

app_name = 'codesnippets'

urlpatterns = [
    path('', views.AllCode.as_view(), name='home'),
    path('new/', views.CreateCode.as_view(), name='new-code'),
    path('view/<int:pk>', views.ViewCode.as_view(), name='view-code'),
    path('update/<int:pk>', views.UpdateCode.as_view(), name='update-code'),
    path('delete/<int:pk>', views.DeleteCode.as_view(), name='delete-code'),
]
