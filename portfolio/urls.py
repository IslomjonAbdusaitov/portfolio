from django.urls import path
from .views import MainPageView, allmessagesview

urlpatterns = [
    path("", MainPageView.as_view(), name="main"),
    path("messages/", allmessagesview, name="messages"),

]