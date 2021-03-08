from django.conf.urls import url 
from insurance.apps.policy import views 
 
urlpatterns = [ 
    url(r'^api/v1/create_policy$', views.create_policy, name='create_policy')
]