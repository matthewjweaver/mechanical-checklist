from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^subscriptions/create/$", views.create_subscription),
]
