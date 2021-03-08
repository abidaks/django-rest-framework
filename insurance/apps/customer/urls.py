from django.conf.urls import url 
from insurance.apps.customer import views 
 
urlpatterns = [ 
    url(r'^api/v1/create_customer$', views.create_customer, name='create_customer')
]