from django.urls import path
from . import views
urlpatterns = [
    path('',views.show),
    path('addshow/',views.addshow),
    path('update/',views.update),
    path('delete/<int:id>/', views.delete, name='delete1')
]
