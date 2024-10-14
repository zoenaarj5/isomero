from django.urls import path

from abasomyi import views


urlpatterns = [
    path("", views.ibanze,name="main"),
    path('members/', views.bose,name="members"),
    path('members/details/<int:id>',views.umwe,name="details")
]   