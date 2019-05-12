from django import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("about",views.about, name="about")
]
