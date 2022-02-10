#URLConf in referral app.
from django.urls import path

from . import views

urlpatterns= [
    path('',views.DashBoard,name='DashBoard'),
]



