from .import views
from django.conf.urls import url
from django.urls import path,include

app_name = "myapp"

urlpatterns = [
    path('crypto',views.CryptoCoinApiView.as_view()),
]