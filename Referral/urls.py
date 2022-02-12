#URLConf in referral app.
from django.urls import path

from . import views

urlpatterns= [
    #/Referral/
    path('',views.DashBoard,name='DashBoard'),
    #Referral/5/
    path('<int:Job_Id>/',views.Job,name='Job_Id'),

]



