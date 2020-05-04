from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("", views.UsersView.as_view()),
    path("token/", views.login),
    path("me/", views.MeView.as_view()),
    path("me/favs/", views.FavsView.as_view()),
    path("me/favs/<int:pk>/", views.delete_fav),
    path("<int:pk>/", views.user_detail),
]
