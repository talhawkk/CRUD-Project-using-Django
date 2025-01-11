from django.urls import path
from . import views
urlpatterns = [
    path('',views.show),
    path('addshow/',views.addshow),
    path('update/',views.update),
]
