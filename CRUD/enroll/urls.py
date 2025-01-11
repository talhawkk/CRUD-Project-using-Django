from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.show, name='home'),
    path('',views.addshow, name='addshow'),
    # path('update/',views.update), 
    path('delete<int:id>/', views.delete, name='delete1'),
    path('<int:id>/', views.update, name='update1')
]
