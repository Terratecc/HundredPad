
from django.urls import path
from . import views

urlpatterns = [
		path('', views.homepage, name = "homepage"),
		path(r'<slug:slug>', views.error404, name = "error404")
]	