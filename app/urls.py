from django.urls.conf import path
from . import views

urlpatterns=[
    path('',views.index),
    path('exp/<int:pk>',views.expload),

]